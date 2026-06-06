import json
import logging
import re

import anthropic

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = (
    "Ты строгий но доброжелательный преподаватель Python. "
    "Проверяй код начинающих, давай конкретный фидбек на русском языке."
)

PASSING_GRADES = {"Отлично", "Хорошо"}


def _build_user_prompt(user_code: str, task: dict) -> str:
    return (
        f"Задача: {task['description']}\n"
        f"Пример входных данных: {task['example_input']}\n"
        f"Ожидаемый результат: {task['example_output']}\n"
        f"Код студента:\n{user_code}\n\n"
        "Ответь строго в JSON формате без лишнего текста:\n"
        "{\n"
        "  'is_correct': true/false,\n"
        "  'score': число от 0 до 10,\n"
        "  'feedback': 'подробный фидбек на русском',\n"
        "  'improvements': 'что можно улучшить',\n"
        "  'grade': 'Отлично / Хорошо / Нужно доработать / Не принято'\n"
        "}"
    )


def _parse_json_response(text: str) -> dict:
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        text = text.replace("'", '"')
        text = re.sub(r"\btrue\b", "true", text, flags=re.IGNORECASE)
        text = re.sub(r"\bfalse\b", "false", text, flags=re.IGNORECASE)
        return json.loads(text)


def _score_for_grade(grade: str) -> int:
    if grade == "Отлично":
        return 30
    if grade == "Хорошо":
        return 20
    return 0


async def check_code(
    user_code: str,
    task: dict,
    *,
    api_key: str,
    model: str = "claude-sonnet-4-6",
) -> dict:
    """
    Проверяет код студента через Claude API.

    Returns:
        dict с ключами: is_correct, score, feedback, improvements, grade, points
    """
    default_error = {
        "is_correct": False,
        "score": 0,
        "feedback": "Не удалось проверить код. Попробуй ещё раз позже.",
        "improvements": "",
        "grade": "Не принято",
        "points": 0,
    }

    try:
        client = anthropic.AsyncAnthropic(api_key=api_key)
        message = await client.messages.create(
            model=model,
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            messages=[
                {"role": "user", "content": _build_user_prompt(user_code, task)},
            ],
        )

        raw_text = message.content[0].text
        result = _parse_json_response(raw_text)

        grade = result.get("grade", "Не принято")
        if grade not in {"Отлично", "Хорошо", "Нужно доработать", "Не принято"}:
            grade = "Не принято"

        is_correct = bool(result.get("is_correct", False))
        if grade in PASSING_GRADES:
            is_correct = True

        score = int(result.get("score", 0))
        score = max(0, min(10, score))

        return {
            "is_correct": is_correct,
            "score": score,
            "feedback": result.get("feedback", ""),
            "improvements": result.get("improvements", ""),
            "grade": grade,
            "points": _score_for_grade(grade) if is_correct else 0,
        }
    except json.JSONDecodeError as e:
        logger.error("Ошибка парсинга JSON от Claude: %s", e)
        default_error["feedback"] = "Ошибка обработки ответа AI. Попробуй отправить код снова."
        return default_error
    except anthropic.APIError as e:
        logger.error("Ошибка Anthropic API: %s", e)
        default_error["feedback"] = f"Ошибка API: {e.message if hasattr(e, 'message') else e}"
        return default_error
    except Exception as e:
        logger.error("Неожиданная ошибка check_code: %s", e)
        return default_error
