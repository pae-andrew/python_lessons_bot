import logging

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

import database as db
from content.curriculum import get_course_name
from handlers.helpers import truncate_message
from handlers.keyboards import main_menu_keyboard

logger = logging.getLogger(__name__)
router = Router()


def course_selection_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🐍 Python с нуля", callback_data="select_course:1")],
        [InlineKeyboardButton(text="📊 Python для аналитики", callback_data="select_course:2")],
    ])


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    try:
        user = await db.get_or_create_user(
            message.from_user.id,
            message.from_user.username,
        )
        course_id = user.get("current_course", 1)
        course_name = get_course_name(course_id)

        text = (
            f"Привет, {message.from_user.first_name}! 👋\n\n"
            "Я бот для обучения **Python**.\n\n"
            "📚 Уроки с теорией и примерами\n"
            "🧪 Тесты для закрепления\n"
            "💻 Практические задачи с проверкой через AI\n"
            "⭐ Баллы за правильные ответы\n\n"
            f"Текущий курс: **{course_name}**\n"
            f"Прогресс: модуль {user['current_module']}, урок {user['current_lesson']}\n"
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


@router.callback_query(F.data == "change_course")
async def callback_change_course(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.answer(
        "Выбери курс:\n\n"
        "⚠️ При смене курса прогресс в новом курсе начнётся с начала.\n"
        "Баллы сохраняются.",
        reply_markup=course_selection_keyboard(),
    )


@router.callback_query(F.data.startswith("select_course:"))
async def callback_select_course(callback: CallbackQuery) -> None:
    await callback.answer()
    try:
        course_id = int(callback.data.split(":")[1])
        user = await db.set_course(callback.from_user.id, course_id)
        course_name = get_course_name(course_id)

        await callback.message.answer(
            f"✅ Курс выбран: **{course_name}**\n\n"
            "Начинаем с первого урока!\n"
            "Нажми /lesson чтобы начать.",
            parse_mode="Markdown",
            reply_markup=main_menu_keyboard(),
        )
    except Exception as e:
        logger.error("Ошибка select_course: %s", e)
        await callback.message.answer("Ошибка при смене курса. Попробуй позже.")
