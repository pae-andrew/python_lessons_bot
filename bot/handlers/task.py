import logging
import html

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

import database as db
from config import Config
from content.curriculum import format_lesson_path, get_lesson, get_next_lesson
from handlers.helpers import can_advance_lesson, get_current_position, truncate_message
from handlers.keyboards import after_task_keyboard, main_menu_keyboard
from handlers.states import TaskStates
from services.ai_checker import PASSING_GRADES, check_code

logger = logging.getLogger(__name__)
router = Router()

def clean_ai_response(text: str) -> str:
    text = text.replace("&quot;", '"')
    text = text.replace("&#x27;", "'")
    text = text.replace("&amp;", "&")
    text = text.replace("&lt;", "<")
    text = text.replace("&gt;", ">")
    return text

def _extract_code(text: str) -> str:
    if text.startswith("```"):
        lines = text.split("\n")
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        return "\n".join(lines)
    return text


@router.message(Command("task"))
async def cmd_task(message: Message, state: FSMContext) -> None:
    position = await get_current_position(message.from_user.id)
    if not position:
        await message.answer("Сначала нажми /start.")
        return
    module_id, lesson_id = position
    await _begin_task(message, state, module_id, lesson_id)


@router.callback_query(F.data.startswith("start_task:"))
async def callback_start_task(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.answer()
    parts = callback.data.split(":")
    module_id, lesson_id = int(parts[1]), int(parts[2])
    await _begin_task(callback.message, state, module_id, lesson_id)


async def _begin_task(
    message: Message, state: FSMContext, module_id: int, lesson_id: int
) -> None:
    try:
        lesson = get_lesson(module_id, lesson_id)
        if not lesson:
            await message.answer("Урок не найден.")
            return

        task = lesson["task"]
        text = (
            f"💻 <b>Практическая задача</b>\n"
            f"{format_lesson_path(module_id, lesson_id)}\n\n"
            f"{html.escape(task['description'])}\n\n"
            f"<b>Пример входных данных:</b>\n<code>{html.escape(task['example_input'])}</code>\n\n"
            f"<b>Ожидаемый результат:</b>\n<pre>{html.escape(task['example_output'])}</pre>\n\n"
            f"💡 Подсказка: {html.escape(task['solution_hint'])}\n\n"
            "Отправь свой код сообщением (можно в блоке ```python)."
        )

        await state.set_state(TaskStates.waiting_code)
        await state.update_data(module_id=module_id, lesson_id=lesson_id)
        await message.answer(truncate_message(text), parse_mode="HTML")
    except Exception as e:
        logger.error("Ошибка начала задачи: %s", e, exc_info=True)
        await message.answer("Не удалось загрузить задачу.")


@router.message(TaskStates.waiting_code, F.text)
async def receive_code(message: Message, state: FSMContext, config: Config) -> None:
    try:
        data = await state.get_data()
        module_id = data.get("module_id")
        lesson_id = data.get("lesson_id")

        if not module_id or not lesson_id:
            await message.answer("Сессия задачи истекла. Нажми /task снова.")
            await state.clear()
            return

        lesson = get_lesson(module_id, lesson_id)
        if not lesson:
            await message.answer("Урок не найден.")
            await state.clear()
            return

        user_code = _extract_code(message.text)
        if not user_code.strip():
            await message.answer("Код пустой. Отправь решение задачи.")
            return

        await message.answer("⏳ Проверяю код через AI...")

        result = await check_code(
            user_code,
            lesson["task"],
            api_key=config.anthropic_api_key,
            model=config.claude_model,
        )

        grade = result["grade"]
        task_passed = grade in PASSING_GRADES
        points = result["points"]

        await db.upsert_lesson_progress(
            message.from_user.id,
            module_id,
            lesson_id,
            task_passed=task_passed,
            score_delta=points,
        )
        if points:
            await db.add_score(message.from_user.id, points)

        if task_passed:
            progress = await db.get_lesson_progress(
                message.from_user.id, module_id, lesson_id
            )
            if progress and progress["test_passed"] and progress["task_passed"]:
                await db.mark_lesson_completed(
                    message.from_user.id, module_id, lesson_id
                )

        can_next = await can_advance_lesson(
            message.from_user.id, module_id, lesson_id
        )

        response = (
            f"💻 Результат проверки\n\n"
            f"Оценка: {result['grade']} ({result['score']}/10)\n"
            f"⭐ Начислено баллов: {points}\n\n"
            f"📝 {clean_ai_response(result['feedback'])}\n"
        )
        if result.get("improvements"):
            response += f"\n💡 Улучшения: {clean_ai_response(result['improvements'])}\n"

        if task_passed:
            response += "\n✅ Задача принята!"
            if can_next:
                response += "\n➡️ Можешь перейти к следующему уроку (/next)."
        else:
            response += (
                "\n❌ Для зачёта нужна оценка «Хорошо» или «Отлично». Попробуй ещё!"
            )

        await state.clear()
        await message.answer(
            truncate_message(response),
            reply_markup=after_task_keyboard(module_id, lesson_id, can_next=can_next),
        )
    except Exception as e:
        logger.error("Ошибка проверки кода: %s", e)
        await message.answer("Ошибка при проверке кода. Попробуй позже.")
        await state.clear()


@router.message(Command("next"))
async def cmd_next(message: Message) -> None:
    await _advance(message, message.from_user.id)


@router.callback_query(F.data == "next_lesson")
async def callback_next_lesson(callback: CallbackQuery) -> None:
    await callback.answer()
    await _advance(callback.message, callback.from_user.id)


async def _advance(message: Message, user_id: int) -> None:
    try:
        position = await get_current_position(user_id)
        if not position:
            await message.answer("Сначала нажми /start.")
            return

        module_id, lesson_id = position
        can_next = await can_advance_lesson(user_id, module_id, lesson_id)

        if not can_next:
            await message.answer(
                "🔒 Следующий урок заблокирован.\n\n"
                "Нужно сдать тест (минимум 2/3) и задачу (оценка «Хорошо» или выше)."
            )
            return

        next_pos = get_next_lesson(module_id, lesson_id)
        if not next_pos:
            await message.answer(
                "🎉 Ты прошёл все доступные уроки! Скоро добавим новые модули.",
                reply_markup=main_menu_keyboard(),
            )
            return

        user = await db.advance_lesson(user_id)
        if not user:
            await message.answer("Ошибка обновления прогресса.")
            return

        from handlers.lesson import send_current_lesson

        await message.answer(
            f"➡️ Переход к модулю {user['current_module']}, "
            f"урок {user['current_lesson']}!"
        )
        await send_current_lesson(message, user_id)
    except Exception as e:
        logger.error("Ошибка перехода к следующему уроку: %s", e)
        await message.answer("Не удалось перейти к следующему уроку.")
