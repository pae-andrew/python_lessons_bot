"""Учебная программа: модули, уроки, тесты и задачи."""

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
                    {
                        "question": "Что делает функция print()?",
                        "options": [
                            "Считывает данные с клавиатуры",
                            "Выводит информацию на экран",
                            "Удаляет переменную",
                            "Создаёт файл",
                        ],
                        "correct": 1,
                    },
                    {
                        "question": "Как правильно создать переменную с именем city?",
                        "options": [
                            "city -> \"Москва\"",
                            "city = \"Москва\"",
                            "var city = \"Москва\"",
                            "city == \"Москва\"",
                        ],
                        "correct": 1,
                    },
                    {
                        "question": "Что выведет код: x = 3; x = x * 2; print(x)?",
                        "options": ["3", "5", "6", "Ошибка"],
                        "correct": 2,
                    },
                ],
                "task": {
                    "description": (
                        "Создай две переменные: name (твоё имя) и hobby (твоё хобби). "
                        "Выведи одной строкой через print(): "
                        "\"Меня зовут <имя>, моё хобби — <хобби>\"."
                    ),
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
                    {
                        "question": "Какой тип у значения 3.14?",
                        "options": ["int", "float", "str", "bool"],
                        "correct": 1,
                    },
                    {
                        "question": "Что вернёт type(True)?",
                        "options": ["<class 'int'>", "<class 'str'>", "<class 'bool'>", "<class 'float'>"],
                        "correct": 2,
                    },
                    {
                        "question": "Как преобразовать строку \"42\" в число?",
                        "options": ["str(\"42\")", "float(\"42\")", "int(\"42\")", "bool(\"42\")"],
                        "correct": 2,
                    },
                ],
                "task": {
                    "description": (
                        "Создай переменные: title (строка), pages (целое число), "
                        "rating (дробное число), is_read (True). "
                        "Выведи f-строку: \"Книга '<title>': <pages> стр., "
                        "рейтинг <rating>, прочитана: <is_read>\"."
                    ),
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
                    "```\n\n"
                    "Можно комбинировать input() и f-строки:\n"
                    "```python\n"
                    "city = input(\"Твой город: \")\n"
                    "print(f\"Классно, что ты из {city}!\")\n"
                    "```"
                ),
                "test": [
                    {
                        "question": "Какой тип возвращает input()?",
                        "options": ["int", "float", "str", "bool"],
                        "correct": 2,
                    },
                    {
                        "question": "Как получить число от пользователя?",
                        "options": [
                            "num = input() + 0",
                            "num = int(input())",
                            "num = str(input())",
                            "num = float(str(input()))",
                        ],
                        "correct": 1,
                    },
                    {
                        "question": "Что выведет: x = input(); print(type(x))?",
                        "options": [
                            "<class 'int'>",
                            "<class 'float'>",
                            "<class 'str'>",
                            "Зависит от ввода",
                        ],
                        "correct": 2,
                    },
                ],
                "task": {
                    "description": (
                        "Напиши программу: запроси у пользователя имя и возраст через input(), "
                        "преобразуй возраст в int и выведи: "
                        "\"<имя>, через 10 лет тебе будет <возраст+10> лет\"."
                    ),
                    "example_input": "Пользователь вводит: Анна, затем 20",
                    "example_output": "Анна, через 10 лет тебе будет 30 лет",
                    "solution_hint": "name = input(), age = int(input()), затем print с f-строкой.",
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
                    "📚 **Урок 2.1: if / elif / else**\n\n"
                    "Условные операторы позволяют выполнять код "
                    "только при определённых условиях.\n\n"
                    "Пример:\n"
                    "```python\n"
                    "score = 85\n\n"
                    "if score >= 90:\n"
                    "    print(\"Отлично!\")\n"
                    "elif score >= 70:\n"
                    "    print(\"Хорошо!\")\n"
                    "else:\n"
                    "    print(\"Нужно подтянуть\")\n"
                    "```\n\n"
                    "Операторы сравнения: `==`, `!=`, `<`, `>`, `<=`, `>=`\n"
                    "Логические: `and`, `or`, `not`\n\n"
                    "```python\n"
                    "age = 20\n"
                    "if age >= 18 and age < 65:\n"
                    "    print(\"Рабочий возраст\")\n"
                    "```"
                ),
                "test": [
                    {
                        "question": "Когда выполняется блок elif?",
                        "options": [
                            "Всегда после if",
                            "Если условие if ложно и elif истинно",
                            "Только если if и else ложны",
                            "Никогда",
                        ],
                        "correct": 1,
                    },
                    {
                        "question": "Что выведет: x=5; print('A' if x>10 else 'B')?",
                        "options": ["A", "B", "5", "Ошибка"],
                        "correct": 1,
                    },
                    {
                        "question": "Какой оператор проверяет равенство?",
                        "options": ["=", "==", "!=", "is"],
                        "correct": 1,
                    },
                ],
                "task": {
                    "description": (
                        "Запроси число через input(), преобразуй в int. "
                        "Если число > 0 — выведи \"Положительное\", "
                        "если < 0 — \"Отрицательное\", иначе — \"Ноль\"."
                    ),
                    "example_input": "Пользователь вводит: -3",
                    "example_output": "Отрицательное",
                    "solution_hint": "Используй if / elif / else с int(input()).",
                },
            },
            2: {
                "title": "Цикл for и range()",
                "theory": (
                    "📚 **Урок 2.2: Цикл for и range()**\n\n"
                    "Цикл `for` повторяет код для каждого элемента "
                    "последовательности.\n\n"
                    "Пример:\n"
                    "```python\n"
                    "fruits = [\"яблоко\", \"банан\", \"вишня\"]\n"
                    "for fruit in fruits:\n"
                    "    print(fruit)\n"
                    "```\n\n"
                    "Функция `range()` создаёт последовательность чисел:\n"
                    "```python\n"
                    "for i in range(5):      # 0, 1, 2, 3, 4\n"
                    "    print(i)\n\n"
                    "for i in range(1, 6):   # 1, 2, 3, 4, 5\n"
                    "    print(i)\n\n"
                    "for i in range(0, 10, 2):  # 0, 2, 4, 6, 8\n"
                    "    print(i)\n"
                    "```"
                ),
                "test": [
                    {
                        "question": "Что выведет: for i in range(3): print(i)?",
                        "options": ["1 2 3", "0 1 2", "0 1 2 3", "3"],
                        "correct": 1,
                    },
                    {
                        "question": "range(2, 5) генерирует числа:",
                        "options": ["2, 3, 4, 5", "2, 3, 4", "0, 1, 2, 3, 4", "2, 5"],
                        "correct": 1,
                    },
                    {
                        "question": "Как перебрать список names?",
                        "options": [
                            "for names:",
                            "while names:",
                            "for name in names:",
                            "loop name in names:",
                        ],
                        "correct": 2,
                    },
                ],
                "task": {
                    "description": (
                        "Выведи квадраты чисел от 1 до 5 включительно, "
                        "каждый на новой строке в формате: \"<число>: <квадрат>\"."
                    ),
                    "example_input": "Нет ввода",
                    "example_output": "1: 1\n2: 4\n3: 9\n4: 16\n5: 25",
                    "solution_hint": "for i in range(1, 6): print(f\"{i}: {i*i}\")",
                },
            },
            3: {
                "title": "Цикл while",
                "theory": (
                    "📚 **Урок 2.3: Цикл while**\n\n"
                    "Цикл `while` повторяет код, пока условие истинно.\n\n"
                    "Пример:\n"
                    "```python\n"
                    "count = 0\n"
                    "while count < 3:\n"
                    "    print(\"Счёт:\", count)\n"
                    "    count += 1\n"
                    "```\n\n"
                    "Вывод:\n"
                    "```\n"
                    "Счёт: 0\n"
                    "Счёт: 1\n"
                    "Счёт: 2\n"
                    "```\n\n"
                    "Бесконечный цикл (осторожно!):\n"
                    "```python\n"
                    "while True:\n"
                    "    answer = input(\"Продолжить? (да/нет): \")\n"
                    "    if answer == \"нет\":\n"
                    "        break  # выход из цикла\n"
                    "```\n\n"
                    "`break` — выход из цикла, `continue` — переход к следующей итерации."
                ),
                "test": [
                    {
                        "question": "Когда выполняется тело цикла while?",
                        "options": [
                            "Один раз",
                            "Пока условие истинно",
                            "Пока условие ложно",
                            "Фиксированное число раз",
                        ],
                        "correct": 1,
                    },
                    {
                        "question": "Что делает break внутри цикла?",
                        "options": [
                            "Пропускает итерацию",
                            "Завершает цикл",
                            "Перезапускает программу",
                            "Ничего",
                        ],
                        "correct": 1,
                    },
                    {
                        "question": "Сколько раз выполнится: x=0; while x<3: x+=1?",
                        "options": ["2", "3", "4", "Бесконечно"],
                        "correct": 1,
                    },
                ],
                "task": {
                    "description": (
                        "С помощью while выведи числа от 1 до 5 включительно, "
                        "каждое на новой строке. Начни с num = 1."
                    ),
                    "example_input": "Нет ввода",
                    "example_output": "1\n2\n3\n4\n5",
                    "solution_hint": "num = 1; while num <= 5: print(num); num += 1",
                },
            },
        },
    },
    3: {
        "title": "Списки, словари, множества",
        "lessons": {
            1: {
                "title": "Списки: создание, индексы, срезы",
                "theory": (
                    "📚 **Урок 3.1: Списки**\n\n"
                    "Список — упорядоченная коллекция элементов любых типов.\n\n"
                    "Создание:\n"
                    "```python\n"
                    "fruits = ['яблоко', 'банан', 'вишня']\n"
                    "numbers = [1, 2, 3, 4, 5]\n"
                    "mixed = [1, 'привет', True, 3.14]\n"
                    "```\n\n"
                    "Доступ по индексу (с нуля):\n"
                    "```python\n"
                    "print(fruits[0])   # яблоко\n"
                    "print(fruits[-1])  # вишня (последний)\n"
                    "```\n\n"
                    "Срезы:\n"
                    "```python\n"
                    "nums = [0, 1, 2, 3, 4, 5]\n"
                    "print(nums[1:4])   # [1, 2, 3]\n"
                    "print(nums[:3])    # [0, 1, 2]\n"
                    "print(nums[::2])   # [0, 2, 4]\n"
                    "```"
                ),
                "test": [
                    {
                        "question": "Какой индекс у первого элемента списка?",
                        "options": ["1", "0", "-1", "None"],
                        "correct": 1,
                    },
                    {
                        "question": "Что вернёт nums[-1] если nums = [10, 20, 30]?",
                        "options": ["10", "20", "30", "Ошибка"],
                        "correct": 2,
                    },
                    {
                        "question": "Что вернёт [1,2,3,4,5][1:3]?",
                        "options": ["[1, 2, 3]", "[2, 3]", "[2, 3, 4]", "[1, 2]"],
                        "correct": 1,
                    },
                ],
                "task": {
                    "description": (
                        "Создай список из 5 любых чисел. "
                        "Выведи первый элемент, последний элемент "
                        "и срез из 2-го по 4-й элемент включительно."
                    ),
                    "example_input": "nums = [10, 20, 30, 40, 50]",
                    "example_output": "10\n50\n[20, 30, 40]",
                    "solution_hint": "nums[0], nums[-1], nums[1:4]",
                },
            },
            2: {
                "title": "Методы списков",
                "theory": (
                    "📚 **Урок 3.2: Методы списков**\n\n"
                    "Списки имеют встроенные методы для изменения:\n\n"
                    "```python\n"
                    "lst = [3, 1, 4, 1, 5]\n\n"
                    "lst.append(9)      # добавить в конец -> [3,1,4,1,5,9]\n"
                    "lst.insert(0, 0)   # вставить по индексу\n"
                    "lst.remove(1)      # удалить первое вхождение\n"
                    "lst.pop()          # удалить и вернуть последний\n"
                    "lst.sort()         # сортировка по возрастанию\n"
                    "lst.reverse()      # перевернуть список\n"
                    "```\n\n"
                    "Полезные функции:\n"
                    "```python\n"
                    "nums = [3, 1, 4, 1, 5]\n"
                    "print(len(nums))   # 5 — длина\n"
                    "print(sum(nums))   # 14 — сумма\n"
                    "print(min(nums))   # 1 — минимум\n"
                    "print(max(nums))   # 5 — максимум\n"
                    "print(1 in nums)   # True — проверка вхождения\n"
                    "```"
                ),
                "test": [
                    {
                        "question": "Какой метод добавляет элемент в конец списка?",
                        "options": ["insert()", "add()", "append()", "push()"],
                        "correct": 2,
                    },
                    {
                        "question": "Что делает lst.pop()?",
                        "options": [
                            "Удаляет первый элемент",
                            "Удаляет и возвращает последний элемент",
                            "Очищает список",
                            "Возвращает длину списка",
                        ],
                        "correct": 1,
                    },
                    {
                        "question": "Что вернёт len([1, 2, 3])?",
                        "options": ["2", "3", "4", "Ошибка"],
                        "correct": 1,
                    },
                ],
                "task": {
                    "description": (
                        "Создай список из чисел [5, 2, 8, 1, 9, 3]. "
                        "Добавь число 7 в конец, удали число 2, "
                        "отсортируй список и выведи результат."
                    ),
                    "example_input": "lst = [5, 2, 8, 1, 9, 3]",
                    "example_output": "[1, 3, 5, 7, 8, 9]",
                    "solution_hint": "append(7), remove(2), sort(), print(lst)",
                },
            },
            3: {
                "title": "Словари",
                "theory": (
                    "📚 **Урок 3.3: Словари**\n\n"
                    "Словарь — коллекция пар ключ: значение.\n\n"
                    "```python\n"
                    "person = {\n"
                    "    'name': 'Анна',\n"
                    "    'age': 25,\n"
                    "    'city': 'Москва'\n"
                    "}\n\n"
                    "print(person['name'])       # Анна\n"
                    "person['age'] = 26          # изменить значение\n"
                    "person['email'] = 'a@b.ru'  # добавить ключ\n"
                    "del person['city']          # удалить ключ\n"
                    "```\n\n"
                    "Методы словаря:\n"
                    "```python\n"
                    "d = {'a': 1, 'b': 2, 'c': 3}\n"
                    "print(d.keys())    # dict_keys(['a', 'b', 'c'])\n"
                    "print(d.values())  # dict_values([1, 2, 3])\n"
                    "print(d.items())   # dict_items([('a',1), ...])\n"
                    "print(d.get('z', 0))  # 0 (значение по умолчанию)\n"
                    "```"
                ),
                "test": [
                    {
                        "question": "Как получить значение по ключу 'name' в словаре d?",
                        "options": ["d(name)", "d.name", "d['name']", "d->name"],
                        "correct": 2,
                    },
                    {
                        "question": "Что вернёт d.get('x', 42) если ключа 'x' нет?",
                        "options": ["None", "Ошибка", "42", "0"],
                        "correct": 2,
                    },
                    {
                        "question": "Какой метод возвращает все ключи словаря?",
                        "options": ["d.keys()", "d.values()", "d.items()", "d.all()"],
                        "correct": 0,
                    },
                ],
                "task": {
                    "description": (
                        "Создай словарь с данными о книге: title, author, year, pages. "
                        "Добавь ключ 'rating' со значением 4.9. "
                        "Выведи все пары ключ-значение в формате 'ключ: значение'."
                    ),
                    "example_input": "book = {'title': '1984', 'author': 'Оруэлл', 'year': 1949, 'pages': 328}",
                    "example_output": "title: 1984\nauthor: Оруэлл\nyear: 1949\npages: 328\nrating: 4.9",
                    "solution_hint": "book['rating'] = 4.9; for k, v in book.items(): print(f'{k}: {v}')",
                },
            },
            4: {
                "title": "Множества и кортежи",
                "theory": (
                    "📚 **Урок 3.4: Множества и кортежи**\n\n"
                    "**Кортеж** — неизменяемый список:\n"
                    "```python\n"
                    "coords = (55.75, 37.61)  # нельзя изменить\n"
                    "rgb = (255, 128, 0)\n"
                    "print(coords[0])  # 55.75\n"
                    "```\n\n"
                    "**Множество** — неупорядоченная коллекция уникальных элементов:\n"
                    "```python\n"
                    "s = {1, 2, 3, 2, 1}   # {1, 2, 3} — дубликаты убраны\n"
                    "s.add(4)               # добавить элемент\n"
                    "s.remove(2)            # удалить элемент\n"
                    "print(3 in s)          # True — проверка вхождения\n"
                    "```\n\n"
                    "Операции с множествами:\n"
                    "```python\n"
                    "a = {1, 2, 3, 4}\n"
                    "b = {3, 4, 5, 6}\n"
                    "print(a & b)  # {3, 4} — пересечение\n"
                    "print(a | b)  # {1,2,3,4,5,6} — объединение\n"
                    "print(a - b)  # {1, 2} — разность\n"
                    "```"
                ),
                "test": [
                    {
                        "question": "Что будет в множестве {1, 2, 2, 3, 3, 3}?",
                        "options": ["{1,2,2,3,3,3}", "{1,2,3}", "{3}", "Ошибка"],
                        "correct": 1,
                    },
                    {
                        "question": "Можно ли изменить элемент кортежа?",
                        "options": ["Да, через индекс", "Да, через метод", "Нет, кортеж неизменяем", "Только первый элемент"],
                        "correct": 2,
                    },
                    {
                        "question": "Что вернёт {1,2,3} & {2,3,4}?",
                        "options": ["{1,2,3,4}", "{2,3}", "{1,4}", "{1,2,3,2,3,4}"],
                        "correct": 1,
                    },
                ],
                "task": {
                    "description": (
                        "Даны два списка с повторами: "
                        "a = [1, 2, 2, 3, 4, 4, 5] и b = [3, 4, 5, 5, 6, 7]. "
                        "Преобразуй их в множества и выведи: "
                        "пересечение, объединение и элементы только из a (разность)."
                    ),
                    "example_input": "a = [1,2,2,3,4,4,5], b = [3,4,5,5,6,7]",
                    "example_output": "Пересечение: {3, 4, 5}\nОбъединение: {1, 2, 3, 4, 5, 6, 7}\nТолько в a: {1, 2}",
                    "solution_hint": "sa = set(a); sb = set(b); sa & sb, sa | sb, sa - sb",
                },
            },
        },
    },
    4: {
        "title": "Функции и лямбды",
        "lessons": {
            1: {
                "title": "def, параметры, return",
                "theory": (
                    "📚 **Урок 4.1: Функции**\n\n"
                    "Функция — блок кода, который можно вызывать многократно.\n\n"
                    "```python\n"
                    "def greet(name):\n"
                    "    return f'Привет, {name}!'\n\n"
                    "print(greet('Анна'))  # Привет, Анна!\n"
                    "print(greet('Иван'))  # Привет, Иван!\n"
                    "```\n\n"
                    "Функция может возвращать несколько значений:\n"
                    "```python\n"
                    "def min_max(lst):\n"
                    "    return min(lst), max(lst)\n\n"
                    "lo, hi = min_max([3, 1, 4, 1, 5])\n"
                    "print(lo, hi)  # 1 5\n"
                    "```\n\n"
                    "Без return функция возвращает None:\n"
                    "```python\n"
                    "def say_hello():\n"
                    "    print('Привет!')\n\n"
                    "result = say_hello()  # печатает Привет!\n"
                    "print(result)         # None\n"
                    "```"
                ),
                "test": [
                    {
                        "question": "Что возвращает функция без оператора return?",
                        "options": ["0", "False", "None", "Ошибку"],
                        "correct": 2,
                    },
                    {
                        "question": "Как объявить функцию в Python?",
                        "options": ["function f():", "def f():", "func f():", "define f():"],
                        "correct": 1,
                    },
                    {
                        "question": "Что выведет: def f(x): return x*2; print(f(5))?",
                        "options": ["5", "2", "10", "x*2"],
                        "correct": 2,
                    },
                ],
                "task": {
                    "description": (
                        "Напиши функцию is_even(n), которая принимает число "
                        "и возвращает True если оно чётное, иначе False. "
                        "Проверь на числах 4 и 7."
                    ),
                    "example_input": "is_even(4), is_even(7)",
                    "example_output": "True\nFalse",
                    "solution_hint": "return n % 2 == 0",
                },
            },
            2: {
                "title": "Аргументы по умолчанию, *args, **kwargs",
                "theory": (
                    "📚 **Урок 4.2: Продвинутые аргументы**\n\n"
                    "Значения по умолчанию:\n"
                    "```python\n"
                    "def greet(name, greeting='Привет'):\n"
                    "    return f'{greeting}, {name}!'\n\n"
                    "print(greet('Анна'))            # Привет, Анна!\n"
                    "print(greet('Иван', 'Здравствуй'))  # Здравствуй, Иван!\n"
                    "```\n\n"
                    "*args — произвольное количество позиционных аргументов:\n"
                    "```python\n"
                    "def total(*args):\n"
                    "    return sum(args)\n\n"
                    "print(total(1, 2, 3))     # 6\n"
                    "print(total(10, 20))      # 30\n"
                    "```\n\n"
                    "**kwargs — произвольное количество именованных аргументов:\n"
                    "```python\n"
                    "def show_info(**kwargs):\n"
                    "    for key, val in kwargs.items():\n"
                    "        print(f'{key}: {val}')\n\n"
                    "show_info(name='Анна', age=25)  # name: Анна / age: 25\n"
                    "```"
                ),
                "test": [
                    {
                        "question": "Что означает *args в параметрах функции?",
                        "options": [
                            "Умножение аргументов",
                            "Произвольное количество позиционных аргументов",
                            "Обязательный аргумент",
                            "Именованные аргументы",
                        ],
                        "correct": 1,
                    },
                    {
                        "question": "Как передать аргумент по умолчанию?",
                        "options": [
                            "def f(x = 0):",
                            "def f(x default 0):",
                            "def f(x or 0):",
                            "def f(x | 0):",
                        ],
                        "correct": 0,
                    },
                    {
                        "question": "Что выведет: def f(*a): print(len(a)); f(1,2,3)?",
                        "options": ["1", "2", "3", "Ошибка"],
                        "correct": 2,
                    },
                ],
                "task": {
                    "description": (
                        "Напиши функцию describe_person(**kwargs), которая принимает "
                        "любые именованные аргументы и выводит каждый в формате "
                        "'ключ = значение'. Вызови её с аргументами name='Мария', age=30, city='Киев'."
                    ),
                    "example_input": "describe_person(name='Мария', age=30, city='Киев')",
                    "example_output": "name = Мария\nage = 30\ncity = Киев",
                    "solution_hint": "for k, v in kwargs.items(): print(f'{k} = {v}')",
                },
            },
            3: {
                "title": "Рекурсия",
                "theory": (
                    "📚 **Урок 4.3: Рекурсия**\n\n"
                    "Рекурсия — когда функция вызывает саму себя.\n\n"
                    "Пример — факториал:\n"
                    "```python\n"
                    "def factorial(n):\n"
                    "    if n <= 1:       # базовый случай (выход)\n"
                    "        return 1\n"
                    "    return n * factorial(n - 1)\n\n"
                    "print(factorial(5))  # 120 (5*4*3*2*1)\n"
                    "```\n\n"
                    "Пример — числа Фибоначчи:\n"
                    "```python\n"
                    "def fib(n):\n"
                    "    if n <= 1:\n"
                    "        return n\n"
                    "    return fib(n-1) + fib(n-2)\n\n"
                    "print(fib(6))  # 8 (0,1,1,2,3,5,8)\n"
                    "```\n\n"
                    "Важно: всегда нужен базовый случай, иначе бесконечная рекурсия!"
                ),
                "test": [
                    {
                        "question": "Что обязательно нужно в рекурсивной функции?",
                        "options": [
                            "Цикл while",
                            "Базовый случай для остановки",
                            "Аргумент по умолчанию",
                            "Оператор break",
                        ],
                        "correct": 1,
                    },
                    {
                        "question": "Что вернёт factorial(3) если factorial(n) = n * factorial(n-1)?",
                        "options": ["3", "6", "9", "1"],
                        "correct": 1,
                    },
                    {
                        "question": "Что произойдёт без базового случая в рекурсии?",
                        "options": [
                            "Функция вернёт None",
                            "Ошибка RecursionError",
                            "Вернётся 0",
                            "Ничего",
                        ],
                        "correct": 1,
                    },
                ],
                "task": {
                    "description": (
                        "Напиши рекурсивную функцию power(base, exp), "
                        "которая возводит base в степень exp без использования ** и pow(). "
                        "Проверь: power(2, 10) и power(3, 4)."
                    ),
                    "example_input": "power(2, 10), power(3, 4)",
                    "example_output": "1024\n81",
                    "solution_hint": "if exp == 0: return 1; return base * power(base, exp-1)",
                },
            },
            4: {
                "title": "Лямбды, map, filter",
                "theory": (
                    "📚 **Урок 4.4: Лямбды и функции высшего порядка**\n\n"
                    "Лямбда — короткая анонимная функция:\n"
                    "```python\n"
                    "square = lambda x: x ** 2\n"
                    "print(square(5))  # 25\n\n"
                    "add = lambda x, y: x + y\n"
                    "print(add(3, 4))  # 7\n"
                    "```\n\n"
                    "map() — применяет функцию к каждому элементу:\n"
                    "```python\n"
                    "nums = [1, 2, 3, 4, 5]\n"
                    "squares = list(map(lambda x: x**2, nums))\n"
                    "print(squares)  # [1, 4, 9, 16, 25]\n"
                    "```\n\n"
                    "filter() — оставляет элементы, где функция вернула True:\n"
                    "```python\n"
                    "nums = [1, 2, 3, 4, 5, 6]\n"
                    "evens = list(filter(lambda x: x % 2 == 0, nums))\n"
                    "print(evens)  # [2, 4, 6]\n"
                    "```"
                ),
                "test": [
                    {
                        "question": "Что делает lambda x: x * 3?",
                        "options": [
                            "Создаёт переменную x",
                            "Умножает x на 3 и возвращает результат",
                            "Печатает x * 3",
                            "Ничего",
                        ],
                        "correct": 1,
                    },
                    {
                        "question": "Что вернёт list(filter(lambda x: x > 3, [1,2,3,4,5]))?",
                        "options": ["[1,2,3]", "[4,5]", "[3,4,5]", "[1,2]"],
                        "correct": 1,
                    },
                    {
                        "question": "Что вернёт list(map(lambda x: x+1, [1,2,3]))?",
                        "options": ["[1,2,3]", "[2,3,4]", "[0,1,2]", "[2,4,6]"],
                        "correct": 1,
                    },
                ],
                "task": {
                    "description": (
                        "Дан список чисел [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. "
                        "С помощью filter и lambda оставь только нечётные числа, "
                        "затем с помощью map и lambda возведи каждое в квадрат. "
                        "Выведи результат."
                    ),
                    "example_input": "nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]",
                    "example_output": "[1, 9, 25, 49, 81]",
                    "solution_hint": "odds = filter(lambda x: x%2!=0, nums); list(map(lambda x: x**2, odds))",
                },
            },
        },
    },
    5: {
        "title": "ООП: классы и объекты",
        "lessons": {
            1: {
                "title": "Классы, объекты, __init__",
                "theory": (
                    "📚 **Урок 5.1: Классы и объекты**\n\n"
                    "Класс — шаблон для создания объектов. "
                    "Объект — экземпляр класса.\n\n"
                    "```python\n"
                    "class Dog:\n"
                    "    def __init__(self, name, age):\n"
                    "        self.name = name  # атрибут объекта\n"
                    "        self.age = age\n\n"
                    "    def bark(self):\n"
                    "        return f'{self.name} говорит: Гав!'\n\n"
                    "dog1 = Dog('Рекс', 3)\n"
                    "dog2 = Dog('Бобик', 5)\n\n"
                    "print(dog1.name)    # Рекс\n"
                    "print(dog1.bark())  # Рекс говорит: Гав!\n"
                    "print(dog2.age)     # 5\n"
                    "```\n\n"
                    "__init__ вызывается автоматически при создании объекта. "
                    "self — ссылка на сам объект."
                ),
                "test": [
                    {
                        "question": "Что такое __init__?",
                        "options": [
                            "Функция для удаления объекта",
                            "Конструктор — вызывается при создании объекта",
                            "Метод для вывода объекта",
                            "Служебная переменная",
                        ],
                        "correct": 1,
                    },
                    {
                        "question": "Что означает self в методах класса?",
                        "options": [
                            "Текущий модуль",
                            "Ссылка на сам объект",
                            "Родительский класс",
                            "Это просто название переменной",
                        ],
                        "correct": 1,
                    },
                    {
                        "question": "Как создать объект класса Cat с именем 'Мурка'?",
                        "options": [
                            "Cat.new('Мурка')",
                            "cat = Cat('Мурка')",
                            "cat = new Cat('Мурка')",
                            "Cat.create('Мурка')",
                        ],
                        "correct": 1,
                    },
                ],
                "task": {
                    "description": (
                        "Создай класс Rectangle с атрибутами width и height. "
                        "Добавь метод area(), возвращающий площадь, "
                        "и метод perimeter(), возвращающий периметр. "
                        "Создай объект с width=5, height=3 и выведи площадь и периметр."
                    ),
                    "example_input": "rect = Rectangle(5, 3)",
                    "example_output": "Площадь: 15\nПериметр: 16",
                    "solution_hint": "area = width * height; perimeter = 2 * (width + height)",
                },
            },
            2: {
                "title": "Методы и атрибуты класса",
                "theory": (
                    "📚 **Урок 5.2: Методы и атрибуты**\n\n"
                    "Атрибуты класса — общие для всех объектов:\n"
                    "```python\n"
                    "class Counter:\n"
                    "    count = 0  # атрибут класса\n\n"
                    "    def __init__(self, name):\n"
                    "        self.name = name      # атрибут объекта\n"
                    "        Counter.count += 1\n\n"
                    "a = Counter('A')\n"
                    "b = Counter('B')\n"
                    "print(Counter.count)  # 2\n"
                    "```\n\n"
                    "Статические методы не требуют self:\n"
                    "```python\n"
                    "class MathUtils:\n"
                    "    @staticmethod\n"
                    "    def square(x):\n"
                    "        return x ** 2\n\n"
                    "print(MathUtils.square(4))  # 16\n"
                    "```\n\n"
                    "Свойства через property:\n"
                    "```python\n"
                    "class Circle:\n"
                    "    def __init__(self, radius):\n"
                    "        self.radius = radius\n\n"
                    "    @property\n"
                    "    def area(self):\n"
                    "        return 3.14159 * self.radius ** 2\n\n"
                    "c = Circle(5)\n"
                    "print(c.area)  # 78.53...\n"
                    "```"
                ),
                "test": [
                    {
                        "question": "В чём разница между атрибутом класса и атрибутом объекта?",
                        "options": [
                            "Никакой разницы нет",
                            "Атрибут класса общий для всех объектов, атрибут объекта — индивидуальный",
                            "Атрибут класса изменяемый, атрибут объекта — нет",
                            "Атрибут объекта быстрее",
                        ],
                        "correct": 1,
                    },
                    {
                        "question": "Что делает декоратор @staticmethod?",
                        "options": [
                            "Запрещает изменять метод",
                            "Метод не привязан к объекту, не принимает self",
                            "Делает метод приватным",
                            "Вызывает метод автоматически",
                        ],
                        "correct": 1,
                    },
                    {
                        "question": "Как вызвать статический метод square класса Math?",
                        "options": [
                            "Math.square()",
                            "Math().square()",
                            "Оба варианта верны",
                            "static.Math.square()",
                        ],
                        "correct": 2,
                    },
                ],
                "task": {
                    "description": (
                        "Создай класс BankAccount с атрибутами owner и balance (по умолчанию 0). "
                        "Добавь методы deposit(amount) для пополнения и withdraw(amount) для снятия "
                        "(нельзя снять больше баланса — выведи 'Недостаточно средств'). "
                        "Добавь метод get_balance() и проверь работу."
                    ),
                    "example_input": "acc = BankAccount('Иван'); acc.deposit(1000); acc.withdraw(300); acc.withdraw(800)",
                    "example_output": "700\nНедостаточно средств",
                    "solution_hint": "if amount > self.balance: print('Недостаточно средств') else: self.balance -= amount",
                },
            },
            3: {
                "title": "Наследование",
                "theory": (
                    "📚 **Урок 5.3: Наследование**\n\n"
                    "Наследование позволяет создать новый класс на основе существующего:\n\n"
                    "```python\n"
                    "class Animal:\n"
                    "    def __init__(self, name):\n"
                    "        self.name = name\n\n"
                    "    def speak(self):\n"
                    "        return f'{self.name} издаёт звук'\n\n"
                    "class Dog(Animal):  # Dog наследует Animal\n"
                    "    def speak(self):  # переопределяем метод\n"
                    "        return f'{self.name} говорит: Гав!'\n\n"
                    "class Cat(Animal):\n"
                    "    def speak(self):\n"
                    "        return f'{self.name} говорит: Мяу!'\n\n"
                    "dog = Dog('Рекс')\n"
                    "cat = Cat('Мурка')\n"
                    "print(dog.speak())  # Рекс говорит: Гав!\n"
                    "print(cat.speak())  # Мурка говорит: Мяу!\n"
                    "```\n\n"
                    "super() вызывает метод родителя:\n"
                    "```python\n"
                    "class Puppy(Dog):\n"
                    "    def __init__(self, name, toy):\n"
                    "        super().__init__(name)  # вызов Dog.__init__\n"
                    "        self.toy = toy\n"
                    "```"
                ),
                "test": [
                    {
                        "question": "Как обозначить что класс B наследует класс A?",
                        "options": ["class B -> A:", "class B(A):", "class B extends A:", "B inherits A"],
                        "correct": 1,
                    },
                    {
                        "question": "Что делает super().__init__()?",
                        "options": [
                            "Создаёт новый объект",
                            "Вызывает конструктор родительского класса",
                            "Удаляет родительский класс",
                            "Копирует атрибуты",
                        ],
                        "correct": 1,
                    },
                    {
                        "question": "Если метод переопределён в дочернем классе, какой из них вызовется?",
                        "options": [
                            "Родительский",
                            "Дочерний",
                            "Оба",
                            "Зависит от аргументов",
                        ],
                        "correct": 1,
                    },
                ],
                "task": {
                    "description": (
                        "Создай класс Shape с методом area() возвращающим 0. "
                        "Создай дочерние классы Circle(radius) и Square(side), "
                        "переопределив в каждом метод area(). "
                        "Для круга: 3.14159 * r^2, для квадрата: side^2. "
                        "Выведи площади круга с r=7 и квадрата со стороной 4."
                    ),
                    "example_input": "Circle(7).area(), Square(4).area()",
                    "example_output": "153.93791\n16",
                    "solution_hint": "class Circle(Shape): def area(self): return 3.14159 * self.radius ** 2",
                },
            },
            4: {
                "title": "Магические методы",
                "theory": (
                    "📚 **Урок 5.4: Магические методы**\n\n"
                    "Магические методы (dunder) позволяют управлять поведением объектов:\n\n"
                    "```python\n"
                    "class Vector:\n"
                    "    def __init__(self, x, y):\n"
                    "        self.x = x\n"
                    "        self.y = y\n\n"
                    "    def __str__(self):      # str(obj) и print(obj)\n"
                    "        return f'Vector({self.x}, {self.y})'\n\n"
                    "    def __repr__(self):     # отображение в консоли\n"
                    "        return f'Vector({self.x!r}, {self.y!r})'\n\n"
                    "    def __add__(self, other):  # оператор +\n"
                    "        return Vector(self.x + other.x, self.y + other.y)\n\n"
                    "    def __len__(self):      # len(obj)\n"
                    "        return int((self.x**2 + self.y**2) ** 0.5)\n\n"
                    "v1 = Vector(1, 2)\n"
                    "v2 = Vector(3, 4)\n"
                    "print(v1)         # Vector(1, 2)\n"
                    "print(v1 + v2)    # Vector(4, 6)\n"
                    "print(len(v2))    # 5\n"
                    "```"
                ),
                "test": [
                    {
                        "question": "Какой метод вызывается при print(obj)?",
                        "options": ["__repr__", "__print__", "__str__", "__display__"],
                        "correct": 2,
                    },
                    {
                        "question": "Какой метод позволяет использовать оператор + с объектами?",
                        "options": ["__plus__", "__sum__", "__add__", "__concat__"],
                        "correct": 2,
                    },
                    {
                        "question": "Что такое dunder-методы?",
                        "options": [
                            "Методы с одним подчёркиванием",
                            "Методы с двойными подчёркиваниями: __метод__",
                            "Приватные методы",
                            "Статические методы",
                        ],
                        "correct": 1,
                    },
                ],
                "task": {
                    "description": (
                        "Создай класс Book с атрибутами title, author, pages. "
                        "Реализуй __str__ (выводит 'title by author'), "
                        "__len__ (возвращает количество страниц) "
                        "и __eq__ (книги равны если одинаковые title и author). "
                        "Проверь все три метода."
                    ),
                    "example_input": "b = Book('1984', 'Оруэлл', 328)",
                    "example_output": "1984 by Оруэлл\n328\nTrue",
                    "solution_hint": "__eq__: return self.title == other.title and self.author == other.author",
                },
            },
        },
    },
    6: {
        "title": "Файлы и исключения",
        "lessons": {
            1: {
                "title": "Чтение и запись файлов",
                "theory": (
                    "📚 **Урок 6.1: Работа с файлами**\n\n"
                    "Открытие файла через open():\n\n"
                    "```python\n"
                    "# Запись в файл\n"
                    "f = open('notes.txt', 'w', encoding='utf-8')\n"
                    "f.write('Привет, мир!\\n')\n"
                    "f.write('Вторая строка\\n')\n"
                    "f.close()  # обязательно закрыть!\n"
                    "```\n\n"
                    "Режимы открытия:\n"
                    "```\n"
                    "'r' — чтение (по умолчанию)\n"
                    "'w' — запись (создаёт/перезаписывает)\n"
                    "'a' — добавление в конец\n"
                    "'r+' — чтение и запись\n"
                    "```\n\n"
                    "Чтение файла:\n"
                    "```python\n"
                    "f = open('notes.txt', 'r', encoding='utf-8')\n"
                    "content = f.read()       # весь файл строкой\n"
                    "lines = f.readlines()    # список строк\n"
                    "f.close()\n"
                    "```"
                ),
                "test": [
                    {
                        "question": "Какой режим открывает файл для добавления в конец?",
                        "options": ["'w'", "'r'", "'a'", "'c'"],
                        "correct": 2,
                    },
                    {
                        "question": "Что вернёт f.read()?",
                        "options": [
                            "Список строк",
                            "Весь файл одной строкой",
                            "Первую строку",
                            "Количество символов",
                        ],
                        "correct": 1,
                    },
                    {
                        "question": "Почему важно вызывать f.close()?",
                        "options": [
                            "Чтобы удалить файл",
                            "Чтобы освободить ресурсы и сохранить данные",
                            "Это необязательно",
                            "Чтобы переименовать файл",
                        ],
                        "correct": 1,
                    },
                ],
                "task": {
                    "description": (
                        "Напиши программу: создай файл 'numbers.txt' и запиши в него "
                        "числа от 1 до 5, каждое на новой строке. "
                        "Затем открой файл, прочитай содержимое и выведи "
                        "сумму всех чисел."
                    ),
                    "example_input": "Нет ввода",
                    "example_output": "15",
                    "solution_hint": "write с '\\n', затем readlines() и sum(int(x) for x in lines)",
                },
            },
            2: {
                "title": "Контекстный менеджер with",
                "theory": (
                    "📚 **Урок 6.2: Оператор with**\n\n"
                    "with автоматически закрывает файл — даже при ошибке:\n\n"
                    "```python\n"
                    "# Вместо этого:\n"
                    "f = open('file.txt', 'r')\n"
                    "content = f.read()\n"
                    "f.close()\n\n"
                    "# Используй это (лучше):\n"
                    "with open('file.txt', 'r', encoding='utf-8') as f:\n"
                    "    content = f.read()\n"
                    "# f автоматически закрыт здесь\n"
                    "```\n\n"
                    "Чтение построчно:\n"
                    "```python\n"
                    "with open('data.txt', 'r', encoding='utf-8') as f:\n"
                    "    for line in f:\n"
                    "        print(line.strip())  # strip() убирает '\\n'\n"
                    "```\n\n"
                    "Запись списка строк:\n"
                    "```python\n"
                    "lines = ['первая\\n', 'вторая\\n', 'третья\\n']\n"
                    "with open('out.txt', 'w', encoding='utf-8') as f:\n"
                    "    f.writelines(lines)\n"
                    "```"
                ),
                "test": [
                    {
                        "question": "Когда закрывается файл при использовании with?",
                        "options": [
                            "Когда программа завершится",
                            "Автоматически при выходе из блока with",
                            "Только при вызове close()",
                            "Через 5 секунд",
                        ],
                        "correct": 1,
                    },
                    {
                        "question": "Что делает метод strip() при чтении строк?",
                        "options": [
                            "Удаляет файл",
                            "Убирает пробелы и символы переноса строки",
                            "Разбивает строку на слова",
                            "Преобразует в верхний регистр",
                        ],
                        "correct": 1,
                    },
                    {
                        "question": "Как правильно открыть файл через with?",
                        "options": [
                            "with open('f.txt') as f:",
                            "with file('f.txt') as f:",
                            "open('f.txt') with as f:",
                            "using open('f.txt') as f:",
                        ],
                        "correct": 0,
                    },
                ],
                "task": {
                    "description": (
                        "Создай файл 'words.txt' и запиши в него 5 любых слов, "
                        "каждое на новой строке. Используй with. "
                        "Затем прочитай файл через with и выведи каждое слово "
                        "в верхнем регистре."
                    ),
                    "example_input": "Нет ввода",
                    "example_output": "PYTHON\nКОД\nФАЙЛ\nДАННЫЕ\nПРОГРАММА",
                    "solution_hint": "with open... as f: for line in f: print(line.strip().upper())",
                },
            },
            3: {
                "title": "Исключения try/except",
                "theory": (
                    "📚 **Урок 6.3: Обработка исключений**\n\n"
                    "Исключения — ошибки во время выполнения программы:\n\n"
                    "```python\n"
                    "try:\n"
                    "    x = int(input('Введи число: '))\n"
                    "    result = 10 / x\n"
                    "    print(result)\n"
                    "except ValueError:\n"
                    "    print('Это не число!')\n"
                    "except ZeroDivisionError:\n"
                    "    print('Нельзя делить на ноль!')\n"
                    "except Exception as e:\n"
                    "    print(f'Неожиданная ошибка: {e}')\n"
                    "else:\n"
                    "    print('Всё прошло успешно!')  # если не было ошибок\n"
                    "finally:\n"
                    "    print('Выполняется всегда')  # всегда\n"
                    "```\n\n"
                    "Частые исключения:\n"
                    "```\n"
                    "ValueError       — неверное значение (int('abc'))\n"
                    "ZeroDivisionError — деление на ноль\n"
                    "FileNotFoundError — файл не найден\n"
                    "IndexError       — индекс за пределами списка\n"
                    "KeyError         — ключ не найден в словаре\n"
                    "TypeError        — неверный тип данных\n"
                    "```"
                ),
                "test": [
                    {
                        "question": "Какой блок выполняется всегда — даже при ошибке?",
                        "options": ["try", "except", "else", "finally"],
                        "correct": 3,
                    },
                    {
                        "question": "Какое исключение возникнет при int('abc')?",
                        "options": ["TypeError", "ValueError", "NameError", "SyntaxError"],
                        "correct": 1,
                    },
                    {
                        "question": "Когда выполняется блок else в try/except?",
                        "options": [
                            "Всегда",
                            "Только при ошибке",
                            "Только если ошибки не было",
                            "Никогда",
                        ],
                        "correct": 2,
                    },
                ],
                "task": {
                    "description": (
                        "Напиши функцию safe_divide(a, b), которая делит a на b. "
                        "Если b == 0 — перехвати ZeroDivisionError и верни 'Деление на ноль'. "
                        "Если a или b не числа — перехвати TypeError и верни 'Неверный тип'. "
                        "Проверь: safe_divide(10, 2), safe_divide(5, 0), safe_divide('a', 2)."
                    ),
                    "example_input": "safe_divide(10, 2), safe_divide(5, 0), safe_divide('a', 2)",
                    "example_output": "5.0\nДеление на ноль\nНеверный тип",
                    "solution_hint": "try: return a/b; except ZeroDivisionError: ...; except TypeError: ...",
                },
            },
            4: {
                "title": "Собственные исключения",
                "theory": (
                    "📚 **Урок 6.4: Создание собственных исключений**\n\n"
                    "Можно создавать свои классы исключений:\n\n"
                    "```python\n"
                    "class AgeError(ValueError):\n"
                    "    \"\"\"Ошибка: недопустимый возраст\"\"\"\n"
                    "    pass\n\n"
                    "class NegativeBalanceError(Exception):\n"
                    "    def __init__(self, amount):\n"
                    "        self.amount = amount\n"
                    "        super().__init__(f'Баланс не может быть {amount}')\n\n"
                    "def set_age(age):\n"
                    "    if age < 0 or age > 150:\n"
                    "        raise AgeError(f'Возраст {age} недопустим')\n"
                    "    return age\n\n"
                    "try:\n"
                    "    set_age(-5)\n"
                    "except AgeError as e:\n"
                    "    print(f'Ошибка: {e}')  # Ошибка: Возраст -5 недопустим\n"
                    "```\n\n"
                    "raise вручную вызывает исключение. "
                    "Собственные исключения наследуют Exception или его подклассы."
                ),
                "test": [
                    {
                        "question": "Как создать собственное исключение?",
                        "options": [
                            "class MyError: pass",
                            "class MyError(Exception): pass",
                            "exception MyError: pass",
                            "def MyError(Exception): pass",
                        ],
                        "correct": 1,
                    },
                    {
                        "question": "Какой оператор вызывает исключение вручную?",
                        "options": ["throw", "raise", "error", "except"],
                        "correct": 1,
                    },
                    {
                        "question": "От какого класса обычно наследуют собственные исключения?",
                        "options": ["object", "BaseClass", "Exception", "Error"],
                        "correct": 2,
                    },
                ],
                "task": {
                    "description": (
                        "Создай исключение PasswordError(ValueError). "
                        "Напиши функцию validate_password(password): "
                        "если длина меньше 8 символов — raise PasswordError('Пароль слишком короткий'), "
                        "если нет цифр — raise PasswordError('Пароль должен содержать цифры'). "
                        "Проверь на паролях: 'abc', 'abcdefgh', 'abc12345'."
                    ),
                    "example_input": "validate_password('abc'), validate_password('abcdefgh'), validate_password('abc12345')",
                    "example_output": "Пароль слишком короткий\nПароль должен содержать цифры\nПароль принят",
                    "solution_hint": "any(c.isdigit() for c in password) — проверка наличия цифры",
                },
            },
        },
    },
}


def get_module(module_id: int) -> dict | None:
    return CURRICULUM.get(module_id)


def get_lesson(module_id: int, lesson_id: int) -> dict | None:
    module = CURRICULUM.get(module_id)
    if not module:
        return None
    return module["lessons"].get(lesson_id)


def get_lesson_title(module_id: int, lesson_id: int) -> str:
    module = CURRICULUM.get(module_id, {})
    lesson = module.get("lessons", {}).get(lesson_id, {})
    return lesson.get("title", "Неизвестный урок")


def get_module_title(module_id: int) -> str:
    module = CURRICULUM.get(module_id, {})
    return module.get("title", "Неизвестный модуль")


def get_next_lesson(module_id: int, lesson_id: int) -> tuple[int, int] | None:
    module = CURRICULUM.get(module_id)
    if not module:
        return None

    lesson_ids = sorted(module["lessons"].keys())
    current_idx = lesson_ids.index(lesson_id) if lesson_id in lesson_ids else -1

    if current_idx >= 0 and current_idx + 1 < len(lesson_ids):
        return module_id, lesson_ids[current_idx + 1]

    next_module_id = module_id + 1
    if next_module_id in CURRICULUM:
        first_lesson = min(CURRICULUM[next_module_id]["lessons"].keys())
        return next_module_id, first_lesson

    return None


def count_total_lessons() -> int:
    return sum(len(m["lessons"]) for m in CURRICULUM.values())


def format_lesson_path(module_id: int, lesson_id: int) -> str:
    return f"Модуль {module_id}.{lesson_id}: {get_lesson_title(module_id, lesson_id)}"
