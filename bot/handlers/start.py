import logging

from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message

import database as db
from handlers.helpers import truncate_message
from handlers.keyboards import main_menu_keyboard

logger = logging.getLogger(__name__)
router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    try:
        user = await db.get_or_create_user(
            message.from_user.id,
            message.from_user.username,
        )
        text = (
            f"Привет, {message.from_user.first_name}! 👋\n\n"
            "Я бот для обучения программированию на **Python**.\n\n"
            "📚 Уроки с теорией и примерами\n"
            "🧪 Тесты для закрепления\n"
            "💻 Практические задачи с проверкой через AI\n"
            "⭐ Баллы за правильные ответы\n\n"
            f"Твой текущий прогресс: модуль {user['current_module']}, "
            f"урок {user['current_lesson']}\n"
            f"⭐ Баллы: {user['total_score']}\n\n"
            "Выбери действие:"
        )
        await message.answer(
            truncate_message(text),
            reply_markup=main_menu_keyboard(),
            parse_mode="Markdown",
        )
    except Exception as e:
        logger.error("Ошибка /start: %s", e)
        await message.answer("Произошла ошибка. Попробуй позже.")


@router.callback_query(F.data == "start_learning")
async def callback_start_learning(callback: CallbackQuery) -> None:
    await callback.answer()
    from handlers.lesson import send_current_lesson

    await send_current_lesson(callback.message, callback.from_user.id, edit=True)


@router.callback_query(F.data == "show_progress")
async def callback_show_progress(callback: CallbackQuery) -> None:
    await callback.answer()
    from handlers.progress import build_progress_message

    text = await build_progress_message(callback.from_user.id)
    await callback.message.answer(truncate_message(text), parse_mode="Markdown")
