import logging

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

import database as db
from content.curriculum import get_lesson
from handlers.helpers import escape_markdown_v1, get_current_position, truncate_message
from handlers.keyboards import after_test_keyboard, test_question_keyboard
from handlers.states import TestStates

logger = logging.getLogger(__name__)
router = Router()

TEST_PASS_THRESHOLD = 2
POINTS_PER_CORRECT = 10


async def _send_question(
    message: Message, module_id: int, lesson_id: int, question_idx: int
) -> None:
    lesson = get_lesson(module_id, lesson_id)
    if not lesson:
        await message.answer("Урок не найден.")
        return

    questions = lesson["test"]
    if question_idx >= len(questions):
        return

    q = questions[question_idx]
    labels = ["A", "B", "C", "D"]
    options_text = "\n".join(
        f"{labels[i]}. {escape_markdown_v1(opt)}" for i, opt in enumerate(q["options"])
    )
    text = (
        f"🧪 **Тест — вопрос {question_idx + 1}/{len(questions)}**\n\n"
        f"{escape_markdown_v1(q['question'])}\n\n"
        f"{options_text}"
    )
    await message.answer(
        truncate_message(text),
        reply_markup=test_question_keyboard(
            module_id, lesson_id, question_idx, q["options"]
        ),
        parse_mode="Markdown",
    )


@router.message(Command("test"))
async def cmd_test(message: Message, state: FSMContext) -> None:
    position = await get_current_position(message.from_user.id)
    if not position:
        await message.answer("Сначала нажми /start.")
        return
    module_id, lesson_id = position
    await _begin_test(message, state, message.from_user.id, module_id, lesson_id)


@router.callback_query(F.data.startswith("start_test:"))
async def callback_start_test(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.answer()
    parts = callback.data.split(":")
    module_id, lesson_id = int(parts[1]), int(parts[2])
    await _begin_test(
        callback.message, state, callback.from_user.id, module_id, lesson_id
    )


async def _begin_test(
    message: Message,
    state: FSMContext,
    user_id: int,
    module_id: int,
    lesson_id: int,
) -> None:
    try:
        lesson = get_lesson(module_id, lesson_id)
        if not lesson:
            await message.answer("Урок не найден.")
            return

        await state.set_state(TestStates.in_progress)
        await state.update_data(
            module_id=module_id,
            lesson_id=lesson_id,
            question_idx=0,
            correct_count=0,
            total_questions=len(lesson["test"]),
        )
        await _send_question(message, module_id, lesson_id, 0)
    except Exception as e:
        logger.error("Ошибка начала теста: %s", e)
        await message.answer("Не удалось начать тест.")


@router.callback_query(F.data.startswith("test_answer:"))
async def callback_test_answer(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.answer()
    try:
        current_state = await state.get_state()
        if current_state != TestStates.in_progress:
            await callback.message.answer("Тест не активен. Нажми /test или «Пройти тест».")
            return

        parts = callback.data.split(":")
        module_id = int(parts[1])
        lesson_id = int(parts[2])
        question_idx = int(parts[3])
        chosen = int(parts[4])

        data = await state.get_data()
        if question_idx != data.get("question_idx", 0):
            return

        lesson = get_lesson(module_id, lesson_id)
        if not lesson:
            await callback.message.answer("Урок не найден.")
            await state.clear()
            return

        questions = lesson["test"]
        correct = questions[question_idx]["correct"]
        is_correct = chosen == correct
        correct_count = data.get("correct_count", 0) + (1 if is_correct else 0)

        feedback = "✅ Верно!" if is_correct else "❌ Неверно."
        await callback.message.answer(feedback)

        next_idx = question_idx + 1
        total = data.get("total_questions", len(questions))

        if next_idx < total:
            await state.update_data(question_idx=next_idx, correct_count=correct_count)
            await _send_question(callback.message, module_id, lesson_id, next_idx)
            return

        await state.clear()
        test_passed = correct_count >= TEST_PASS_THRESHOLD
        points = correct_count * POINTS_PER_CORRECT

        await db.upsert_lesson_progress(
            callback.from_user.id,
            module_id,
            lesson_id,
            test_passed=test_passed,
            score_delta=points,
        )
        if points:
            await db.add_score(callback.from_user.id, points)

        result_text = (
            f"🧪 **Результаты теста**\n\n"
            f"Правильных ответов: {correct_count}/{total}\n"
            f"⭐ Начислено баллов: {points}\n\n"
        )
        if test_passed:
            result_text += "✅ Тест сдан! Можно переходить к задаче."
        else:
            result_text += (
                f"❌ Для зачёта нужно минимум {TEST_PASS_THRESHOLD}/{total}. "
                "Попробуй ещё раз!"
            )

        await callback.message.answer(
            truncate_message(result_text),
            reply_markup=after_test_keyboard(module_id, lesson_id, test_passed),
            parse_mode="Markdown",
        )
    except Exception as e:
        logger.exception("Ошибка обработки ответа теста: %s", e)
        await callback.message.answer("Ошибка при проверке ответа.")
        await state.clear()
