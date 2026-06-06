import logging

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

import database as db
from content.curriculum import (
    count_total_lessons,
    format_lesson_path,
    get_module_title,
)
from handlers.helpers import truncate_message
from handlers.keyboards import main_menu_keyboard

logger = logging.getLogger(__name__)
router = Router()


async def build_progress_message(user_id: int) -> str:
    stats = await db.get_user_stats(user_id)
    if not stats:
        return "Пользователь не найден. Нажми /start."

    user = stats["user"]
    module_id = user["current_module"]
    lesson_id = user["current_lesson"]
    total_lessons = count_total_lessons()

    lines = [
        "⭐ **Мой прогресс**",
        "",
        f"📍 Текущая позиция: модуль {module_id}, урок {lesson_id}",
        f"📚 {get_module_title(module_id)} — {format_lesson_path(module_id, lesson_id)}",
        f"🏆 Общий счёт: **{user['total_score']}** баллов",
        f"✅ Пройдено уроков: {stats['completed_count']}/{total_lessons}",
        "",
        "**Детали по урокам:**",
    ]

    if not stats["progress_rows"]:
        lines.append("Пока нет результатов — начни с /lesson!")
    else:
        for row in stats["progress_rows"]:
            m, l = row["module_id"], row["lesson_id"]
            test_icon = "✅" if row["test_passed"] else "❌"
            task_icon = "✅" if row["task_passed"] else "❌"
            lines.append(
                f"• {format_lesson_path(m, l)} — "
                f"🧪 {test_icon} 💻 {task_icon} ⭐ {row['score']}"
            )

    return "\n".join(lines)


@router.message(Command("progress"))
async def cmd_progress(message: Message) -> None:
    try:
        user = await db.get_user(message.from_user.id)
        if not user:
            await message.answer("Сначала нажми /start для регистрации.")
            return

        text = await build_progress_message(message.from_user.id)
        await message.answer(
            truncate_message(text),
            reply_markup=main_menu_keyboard(),
            parse_mode="Markdown",
        )
    except Exception as e:
        logger.error("Ошибка /progress: %s", e)
        await message.answer("Не удалось загрузить прогресс.")
