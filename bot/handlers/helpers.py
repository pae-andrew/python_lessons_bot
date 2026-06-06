MAX_MESSAGE_LENGTH = 4000

MARKDOWN_V1_SPECIAL = ("\\", "_", "*", "`", "[")


def truncate_message(text: str, limit: int = MAX_MESSAGE_LENGTH) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 3] + "..."


def escape_markdown_v1(text: str) -> str:
    """Экранирует символы для Telegram legacy Markdown."""
    for char in MARKDOWN_V1_SPECIAL:
        text = text.replace(char, f"\\{char}")
    return text


async def get_current_position(user_id: int) -> tuple[int, int] | None:
    from database import get_user

    user = await get_user(user_id)
    if not user:
        return None
    return user["current_module"], user["current_lesson"]


async def can_advance_lesson(user_id: int, module_id: int, lesson_id: int) -> bool:
    from database import get_lesson_progress

    progress = await get_lesson_progress(user_id, module_id, lesson_id)
    if not progress:
        return False
    return bool(progress["test_passed"]) and bool(progress["task_passed"])
