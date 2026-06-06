"""Учебная программа: модули, уроки, тесты и задачи."""

from content.analytics_curriculum import ANALYTICS_CURRICULUM

CURRICULUM: dict[int, dict] = {
    1: {
        "title": "Основы Python",
        "lessons": {
            1: {
                "title": "print() и переменные",
                "theory": (
                    "📚 **Урок 1.1: print() и переменные**\n\n"
                    "Функция `print()` выводит текст и значения на экран. "
                    "Переменная — это имя, которое хранит данные.\n\n"
                    "Пример:\n"
                    "```python\n"
                    "name = \"Анна\"\n"
                    "age = 25\n"
                    "print(\"Привет,\", name)\n"
                    "print(\"Тебе\", age, \"лет\")\n"
                    "```\n\n"
                    "Вывод:\n"
                    "```\n"
                    "Привет, Анна\n"
                    "Тебе 25 лет\n"
                    "```\n\n"
                    "Переменным можно присваивать новые значения:\n"
                    "```python\n"
                    "x = 10\n"
                    "x = x + 5\n"
                    "print(x)  # 15\n"
                    "```"
                ),
                "test": [
                    {"question": "Что делает функция print()?", "options": ["Считывает данные с клавиатуры", "Выводит информацию на экран", "Удаляет переменную", "Создаёт файл"], "correct": 1},
                    {"question": "Как правильно создать переменную с именем city?", "options": ["city -> \"Москва\"", "city = \"Москва\"", "var city = \"Москва\"", "city == \"Москва\""], "correct": 1},
                    {"question": "Что выведет код: x = 3; x = x * 2; print(x)?", "options": ["3", "5", "6", "Ошибка"], "correct": 2},
                ],
                "task": {
                    "description": "Создай две переменные: name (твоё имя) и hobby (твоё хобби). Выведи одной строкой через print(): \"Меня зовут <имя>, моё хобби — <хобби>\".",
                    "example_input": "name = \"Иван\", hobby = \"программирование\"",
                    "example_output": "Меня зовут Иван, моё хобби — программирование",
                    "solution_hint": "Используй f-строку или несколько аргументов в print().",
                },
            },
            2: {
                "title": "Типы данных (str, int, float, bool)",
                "theory": (
                    "📚 **Урок 1.2: Типы данных**\n\n"
                    "В Python есть базовые типы данных:\n\n"
                    "• **str** — строка: `\"Привет\"`\n"
                    "• **int** — целое число: `42`\n"
                    "• **float** — дробное число: `3.14`\n"
                    "• **bool** — логический: `True` или `False`\n\n"
                    "Пример:\n"
                    "```python\n"
                    "text = \"Python\"\n"
                    "count = 10\n"
                    "price = 99.5\n"
                    "is_active = True\n\n"
                    "print(type(text))   # <class 'str'>\n"
                    "print(type(count))  # <class 'int'>\n"
                    "```\n\n"
                    "Преобразование типов:\n"
                    "```python\n"
                    "age = int(\"25\")      # строка → число\n"
                    "score = str(100)     # число → строка\n"
                    "print(age + 5)       # 30\n"
                    "```"
                ),
                "test": [
                    {"question": "Какой тип у значения 3.14?", "options": ["int", "float", "str", "bool"], "correct": 1},
                    {"question": "Что вернёт type(True)?", "options": ["<class 'int'>", "<class 'str'>", "<class 'bool'>", "<class 'float'>"], "correct": 2},
                    {"question": "Как преобразовать строку \"42\" в число?", "options": ["str(\"42\")", "float(\"42\")", "int(\"42\")", "bool(\"42\")"], "correct": 2},
                ],
                "task": {
                    "description": "Создай переменные: title (строка), pages (целое число), rating (дробное число), is_read (True). Выведи f-строку: \"Книга '<title>': <pages> стр., рейтинг <rating>, прочитана: <is_read>\".",
                    "example_input": 'title="1984", pages=328, rating=4.8, is_read=True',
                    "example_output": "Книга '1984': 328 стр., рейтинг 4.8, прочитана: True",
                    "solution_hint": "Используй f-строку с переменными разных типов.",
                },
            },
            3: {
                "title": "Ввод данных через input()",
                "theory": (
                    "📚 **Урок 1.3: Ввод данных через input()**\n\n"
                    "Функция `input()` считывает текст с клавиатуры. "
                    "Всегда возвращает **строку** (str).\n\n"
                    "Пример:\n"
                    "```python\n"
                    "name = input(\"Как тебя зовут? \")\n"
                    "print(\"Привет,\", name)\n"
                    "```\n\n"
                    "Если нужно число — преобразуй тип:\n"
                    "```python\n"
                    "age = int(input(\"Сколько тебе лет? \"))\n"
                    "print(\"Через 5 лет тебе будет\", age + 5)\n"
                    "```"
                ),
                "test": [
                    {"question": "Какой тип возвращает input()?", "options": ["int", "float", "str", "bool"], "correct": 2},
                    {"question": "Как получить число от пользователя?", "options": ["num = input() + 0", "num = int(input())", "num = str(input())", "num = float(str(input()))"], "correct": 1},
                    {"question": "Что выведет: x = input(); print(type(x))?", "options": ["<class 'int'>", "<class 'float'>", "<class 'str'>", "Зависит от ввода"], "correct": 2},
                ],
                "task": {
                    "description": "Напиши программу: запроси у пользователя имя и возраст через input(), преобразуй возраст в int и выведи: \"<имя>, через 10 лет тебе будет <возраст+10> лет\".",
                    "example_input": "Пользователь вводит: Анна, затем 20",
                    "example_output": "Анна, через 10 лет тебе будет 30 лет",
                    "solution_hint": "name = input(...); age = int(input(...))",
                },
            },
        },
    },
    2: {
        "title": "Условия и циклы",
        "lessons": {
            1: {
                "title": "if / elif / else",
                "theory": (
                    "📚 **Урок 2.1: Условия if / elif / else**\n\n"
                    "Условия позволяют выполнять разный код в зависимости от данных.\n\n"
                    "```python\n"
                    "age = 18\n\n"
                    "if age >= 18:\n"
                    "    print(\"Совершеннолетний\")\n"
                    "elif age >= 14:\n"
                    "    print(\"Подросток\")\n"
                    "else:\n"
                    "    print(\"Ребёнок\")\n"
                    "```\n\n"
                    "Операторы сравнения: == != > < >= <=\n\n"
                    "Логические операторы:\n"
                    "```python\n"
                    "if age >= 18 and age < 65:\n"
                    "    print(\"Трудоспособный\")\n"
                    "```"
                ),
                "test": [
                    {"question": "Что выведет: if 5 > 3: print('да') else: print('нет')?", "options": ["нет", "да", "Ошибка", "Ничего"], "correct": 1},
                    {"question": "Какой оператор означает 'не равно'?", "options": ["<>", "!=", "=/=", "not="], "correct": 1},
                    {"question": "Что делает elif?", "options": ["Завершает программу", "Проверяет доп. условие если предыдущее ложно", "То же что else", "Создаёт цикл"], "correct": 1},
                ],
                "task": {
                    "description": "Напиши программу: запроси число. Если > 0 — 'Положительное', < 0 — 'Отрицательное', == 0 — 'Ноль'.",
                    "example_input": "Пользователь вводит: -5",
                    "example_output": "Отрицательное",
                    "solution_hint": "if num > 0: ... elif num < 0: ... else: ...",
                },
            },
            2: {
                "title": "Цикл for и range()",
                "theory": (
                    "📚 **Урок 2.2: Цикл for**\n\n"
                    "```python\n"
                    "for i in range(5):\n"
                    "    print(i)  # 0 1 2 3 4\n\n"
                    "for i in range(1, 6):\n"
                    "    print(i)  # 1 2 3 4 5\n\n"
                    "fruits = ['яблоко', 'банан']\n"
                    "for fruit in fruits:\n"
                    "    print(fruit)\n\n"
                    "for i, fruit in enumerate(fruits):\n"
                    "    print(f'{i}: {fruit}')\n"
                    "```"
                ),
                "test": [
                    {"question": "Что выведет range(3)?", "options": ["1 2 3", "0 1 2", "0 1 2 3", "1 2"], "correct": 1},
                    {"question": "Что делает range(2, 8, 2)?", "options": ["2 4 6 8", "2 4 6", "0 2 4 6 8", "2 3 4 5 6 7 8"], "correct": 1},
                    {"question": "Что возвращает enumerate(['a','b'])?", "options": ["Индексы", "Элементы", "Пары (индекс, элемент)", "Длину"], "correct": 2},
                ],
                "task": {
                    "description": "Выведи таблицу умножения числа 7 от 1 до 10. Каждая строка: '7 x N = результат'.",
                    "example_input": "Нет ввода",
                    "example_output": "7 x 1 = 7\n7 x 2 = 14\n...\n7 x 10 = 70",
                    "solution_hint": "for i in range(1, 11): print(f'7 x {i} = {7*i}')",
                },
            },
            3: {
                "title": "Цикл while",
                "theory": (
                    "📚 **Урок 2.3: Цикл while**\n\n"
                    "```python\n"
                    "count = 0\n"
                    "while count < 5:\n"
                    "    print(count)\n"
                    "    count += 1\n\n"
                    "# break — выход\n"
                    "while True:\n"
                    "    ans = input('stop для выхода: ')\n"
                    "    if ans == 'stop':\n"
                    "        break\n\n"
                    "# continue — пропустить итерацию\n"
                    "for i in range(10):\n"
                    "    if i % 2 == 0:\n"
                    "        continue\n"
                    "    print(i)  # нечётные\n"
                    "```"
                ),
                "test": [
                    {"question": "Что будет если не менять переменную в while?", "options": ["Не запустится", "Бесконечный цикл", "Ошибка", "Один раз"], "correct": 1},
                    {"question": "Что делает break?", "options": ["Пропускает", "Выходит из цикла", "Перезапускает", "Ошибка"], "correct": 1},
                    {"question": "Что делает continue?", "options": ["Выходит", "Завершает", "Пропускает текущую итерацию", "Повторяет"], "correct": 2},
                ],
                "task": {
                    "description": "Используя while, найди сумму всех чисел от 1 до 100. Выведи результат.",
                    "example_input": "Нет ввода",
                    "example_output": "5050",
                    "solution_hint": "total = 0; i = 1; while i <= 100: total += i; i += 1",
                },
            },
        },
    },
}

# ── Объединение курсов ─────────────────────────────────────────────────────

COURSES: dict[int, dict] = {
    1: CURRICULUM,
    2: ANALYTICS_CURRICULUM,
}

COURSE_NAMES: dict[int, str] = {
    1: "🐍 Python с нуля",
    2: "📊 Python для аналитики",
}


def _get_course(course_id: int) -> dict:
    return COURSES.get(course_id, CURRICULUM)


def get_module(module_id: int, course_id: int = 1) -> dict | None:
    return _get_course(course_id).get(module_id)


def get_lesson(module_id: int, lesson_id: int, course_id: int = 1) -> dict | None:
    module = _get_course(course_id).get(module_id)
    if not module:
        return None
    return module["lessons"].get(lesson_id)


def get_lesson_title(module_id: int, lesson_id: int, course_id: int = 1) -> str:
    module = _get_course(course_id).get(module_id, {})
    lesson = module.get("lessons", {}).get(lesson_id, {})
    return lesson.get("title", "Неизвестный урок")


def get_module_title(module_id: int, course_id: int = 1) -> str:
    module = _get_course(course_id).get(module_id, {})
    return module.get("title", "Неизвестный модуль")


def get_next_lesson(module_id: int, lesson_id: int, course_id: int = 1) -> tuple[int, int] | None:
    course = _get_course(course_id)
    module = course.get(module_id)
    if not module:
        return None

    lesson_ids = sorted(module["lessons"].keys())
    current_idx = lesson_ids.index(lesson_id) if lesson_id in lesson_ids else -1

    if current_idx >= 0 and current_idx + 1 < len(lesson_ids):
        return module_id, lesson_ids[current_idx + 1]

    next_module_id = module_id + 1
    if next_module_id in course:
        first_lesson = min(course[next_module_id]["lessons"].keys())
        return next_module_id, first_lesson

    return None


def count_total_lessons(course_id: int = 1) -> int:
    return sum(len(m["lessons"]) for m in _get_course(course_id).values())


def format_lesson_path(module_id: int, lesson_id: int, course_id: int = 1) -> str:
    return f"Модуль {module_id}.{lesson_id}: {get_lesson_title(module_id, lesson_id, course_id)}"


def get_course_name(course_id: int) -> str:
    return COURSE_NAMES.get(course_id, "Неизвестный курс")
