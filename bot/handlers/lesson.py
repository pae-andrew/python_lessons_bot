import logging

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

import database as db
from content.curriculum import format_lesson_path, get_lesson, get_module_title
from handlers.helpers import get_current_position, truncate_message
from handlers.keyboards import after_theory_keyboard, lesson_actions_keyboard

logger = logging.getLogger(__name__)
router = Router()


async def send_current_lesson(
    message: Message, user_id: int, *, edit: bool = False
) -> None:
    try:
        position = await get_current_position(user_id)
        if not position:
            await message.answer("Сначала нажми /start для регистрации.")
            return

        module_id, lesson_id = position
        lesson = get_lesson(module_id, lesson_id)

        if not lesson:
            text = (
                "🎉 Поздравляю! Ты прошёл все доступные уроки.\n"
                "Скоро добавим новые модули!"
            )
            if edit:
                await message.edit_text(text)
            else:
                await message.answer(text)
            return

        module_title = get_module_title(module_id)
        header = (
            f"📚 **{module_title}**\n"
            f"**{format_lesson_path(module_id, lesson_id)}**\n\n"
        )
        text = truncate_message(header + lesson["theory"])

        progress = await db.get_lesson_progress(user_id, module_id, lesson_id)
        if progress and progress["test_passed"] and progress["task_passed"]:
            keyboard = lesson_actions_keyboard(module_id, lesson_id)
        else:
            keyboard = after_theory_keyboard(module_id, lesson_id)

        if edit:
            try:
                await message.edit_text(
                    text, reply_markup=keyboard, parse_mode="Markdown"
                )
            except Exception:
                await message.answer(
                    text, reply_markup=keyboard, parse_mode="Markdown"
                )
        else:
            await message.answer(text, reply_markup=keyboard, parse_mode="Markdown")
    except Exception as e:
        logger.error("Ошибка send_current_lesson: %s", e)
        await message.answer("Не удалось загрузить урок. Попробуй позже.")


@router.message(Command("lesson"))
async def cmd_lesson(message: Message) -> None:
    await send_current_lesson(message, message.from_user.id)


@router.callback_query(F.data.startswith("show_lesson:"))
async def callback_show_lesson(callback: CallbackQuery) -> None:
    await callback.answer()
    await send_current_lesson(callback.message, callback.from_user.id, edit=True)
