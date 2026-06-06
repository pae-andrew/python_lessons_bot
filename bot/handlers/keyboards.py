from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📚 Начать обучение",
                    callback_data="start_learning",
                )
            ],
            [
                InlineKeyboardButton(
                    text="⭐ Мой прогресс",
                    callback_data="show_progress",
                )
            ],
        ]
    )


def after_theory_keyboard(module_id: int, lesson_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🧪 Пройти тест",
                    callback_data=f"start_test:{module_id}:{lesson_id}",
                )
            ],
            [
                InlineKeyboardButton(
                    text="⭐ Мой прогресс",
                    callback_data="show_progress",
                )
            ],
        ]
    )


def after_test_keyboard(
    module_id: int, lesson_id: int, test_passed: bool
) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(
                text="💻 Получить задачу",
                callback_data=f"start_task:{module_id}:{lesson_id}",
            )
        ],
    ]
    if test_passed:
        buttons.append(
            [
                InlineKeyboardButton(
                    text="🔄 Пройти тест заново",
                    callback_data=f"start_test:{module_id}:{lesson_id}",
                )
            ]
        )
    else:
        buttons.insert(
            0,
            [
                InlineKeyboardButton(
                    text="🔄 Пройти тест заново",
                    callback_data=f"start_test:{module_id}:{lesson_id}",
                )
            ],
        )
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def after_task_keyboard(
    module_id: int, lesson_id: int, *, can_next: bool
) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(
                text="🔄 Отправить код снова",
                callback_data=f"start_task:{module_id}:{lesson_id}",
            )
        ],
    ]
    if can_next:
        buttons.insert(
            0,
            [
                InlineKeyboardButton(
                    text="➡️ Следующий урок",
                    callback_data="next_lesson",
                )
            ],
        )
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def test_question_keyboard(
    module_id: int, lesson_id: int, question_idx: int, options: list[str]
) -> InlineKeyboardMarkup:
    labels = ["A", "B", "C", "D"]
    row = []
    keyboard_rows = []

    for i, option in enumerate(options):
        label = labels[i] if i < len(labels) else str(i + 1)
        row.append(
            InlineKeyboardButton(
                text=label,
                callback_data=f"test_answer:{module_id}:{lesson_id}:{question_idx}:{i}",
            )
        )
        if len(row) == 2:
            keyboard_rows.append(row)
            row = []

    if row:
        keyboard_rows.append(row)

    return InlineKeyboardMarkup(inline_keyboard=keyboard_rows)


def lesson_actions_keyboard(module_id: int, lesson_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🧪 Тест",
                    callback_data=f"start_test:{module_id}:{lesson_id}",
                ),
                InlineKeyboardButton(
                    text="💻 Задача",
                    callback_data=f"start_task:{module_id}:{lesson_id}",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="➡️ Следующий урок",
                    callback_data="next_lesson",
                )
            ],
            [
                InlineKeyboardButton(
                    text="⭐ Мой прогресс",
                    callback_data="show_progress",
                )
            ],
        ]
    )
