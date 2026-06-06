ANALYTICS_CURRICULUM: dict[int, dict] = {
    1: {
        "title": "NumPy: числа и массивы",
        "lessons": {
            1: {
                "title": "Введение в NumPy: массивы",
                "theory": (
                    "📚 **Урок 1.1: NumPy и массивы**\n\n"
                    "NumPy — основа аналитики данных в Python. "
                    "Работает в десятки раз быстрее обычных списков.\n\n"
                    "```python\n"
                    "import numpy as np\n\n"
                    "# Создание массивов\n"
                    "a = np.array([1, 2, 3, 4, 5])\n"
                    "b = np.zeros(5)          # [0. 0. 0. 0. 0.]\n"
                    "c = np.ones((2, 3))      # матрица 2x3 из единиц\n"
                    "d = np.arange(0, 10, 2)  # [0 2 4 6 8]\n"
                    "e = np.linspace(0, 1, 5) # [0. 0.25 0.5 0.75 1.]\n"
                    "```\n\n"
                    "Основные атрибуты:\n"
                    "```python\n"
                    "a = np.array([[1, 2, 3], [4, 5, 6]])\n"
                    "print(a.shape)   # (2, 3)\n"
                    "print(a.ndim)    # 2\n"
                    "print(a.dtype)   # int64\n"
                    "print(a.size)    # 6\n"
                    "```"
                ),
                "test": [
                    {"question": "Что вернёт np.arange(2, 10, 3)?", "options": ["[2, 5, 8]", "[2, 3, 4]", "[2, 10, 3]", "[3, 6, 9]"], "correct": 0},
                    {"question": "Что хранит атрибут .shape у массива?", "options": ["Тип данных", "Количество элементов", "Размерность (кортеж размеров)", "Сумму элементов"], "correct": 2},
                    {"question": "Чем NumPy массив лучше обычного списка?", "options": ["Хранит только строки", "Работает быстрее для математических операций", "Занимает больше памяти", "Поддерживает разные типы данных"], "correct": 1},
                ],
                "task": {
                    "description": "Создай три массива NumPy:\n1. Массив чисел от 1 до 10 включительно\n2. Матрицу 3x3 из нулей\n3. 6 равномерно распределённых чисел от 0 до 1\nВыведи каждый массив и его форму (shape).",
                    "example_input": "import numpy as np",
                    "example_output": "[ 1  2  3  4  5  6  7  8  9 10] shape: (10,)\n[[0. 0. 0.]\n [0. 0. 0.]\n [0. 0. 0.]] shape: (3, 3)\n[0.  0.2 0.4 0.6 0.8 1. ] shape: (6,)",
                    "solution_hint": "np.arange(1,11), np.zeros((3,3)), np.linspace(0,1,6)",
                },
            },
            2: {
                "title": "NumPy: операции и индексация",
                "theory": (
                    "📚 **Урок 1.2: Операции с массивами**\n\n"
                    "NumPy применяет операции ко всем элементам сразу:\n\n"
                    "```python\n"
                    "import numpy as np\n\n"
                    "a = np.array([1, 2, 3, 4, 5])\n"
                    "print(a * 2)      # [2 4 6 8 10]\n"
                    "print(a ** 2)     # [1 4 9 16 25]\n"
                    "print(a + 10)     # [11 12 13 14 15]\n"
                    "print(a > 3)      # [False False False True True]\n"
                    "```\n\n"
                    "Индексация и срезы:\n"
                    "```python\n"
                    "a = np.array([[1, 2, 3],\n"
                    "              [4, 5, 6],\n"
                    "              [7, 8, 9]])\n\n"
                    "print(a[0, 1])    # 2\n"
                    "print(a[:, 1])    # [2 5 8] — столбец\n"
                    "print(a[1, :])    # [4 5 6] — строка\n"
                    "print(a[a > 5])   # [6 7 8 9]\n"
                    "```"
                ),
                "test": [
                    {"question": "Что вернёт np.array([1,2,3,4]) * 3?", "options": ["[3, 3, 3, 3]", "[3, 6, 9, 12]", "[1, 2, 3, 4, 3]", "Ошибка"], "correct": 1},
                    {"question": "Как получить весь второй столбец матрицы a?", "options": ["a[2]", "a[:, 1]", "a[1, :]", "a[2, :]"], "correct": 1},
                    {"question": "Что делает булева маска a[a > 0]?", "options": ["Удаляет все элементы", "Возвращает элементы больше нуля", "Проверяет размер массива", "Меняет знак элементов"], "correct": 1},
                ],
                "task": {
                    "description": "Создай массив чисел от 1 до 20.\n1. Выведи все чётные числа (используй булеву маску)\n2. Возведи все элементы в квадрат\n3. Выведи элементы с индексами от 5 до 10 включительно",
                    "example_input": "a = np.arange(1, 21)",
                    "example_output": "Чётные: [ 2  4  6  8 10 12 14 16 18 20]\nКвадраты: [  1   4   9  16  25 ...]\nСрез: [ 6  7  8  9 10 11]",
                    "solution_hint": "a[a%2==0], a**2, a[5:11]",
                },
            },
            3: {
                "title": "NumPy: статистика",
                "theory": (
                    "📚 **Урок 1.3: Статистические функции**\n\n"
                    "```python\n"
                    "import numpy as np\n\n"
                    "data = np.array([4, 7, 2, 9, 1, 5, 8, 3, 6, 10])\n\n"
                    "print(np.mean(data))    # 5.5\n"
                    "print(np.median(data))  # 5.5\n"
                    "print(np.std(data))     # стандартное отклонение\n"
                    "print(np.var(data))     # дисперсия\n"
                    "print(np.min(data))     # 1\n"
                    "print(np.max(data))     # 10\n"
                    "print(np.sum(data))     # 55\n"
                    "print(np.percentile(data, 75))  # 75-й перцентиль\n"
                    "```\n\n"
                    "Случайные числа:\n"
                    "```python\n"
                    "np.random.seed(42)\n"
                    "r = np.random.randint(1, 100, size=10)\n"
                    "n = np.random.normal(0, 1, 1000)\n"
                    "```"
                ),
                "test": [
                    {"question": "Что вычисляет np.mean(a)?", "options": ["Медиану", "Среднее арифметическое", "Моду", "Дисперсию"], "correct": 1},
                    {"question": "Зачем использовать np.random.seed()?", "options": ["Для ускорения генерации", "Для воспроизводимости — одинаковые случайные числа", "Для шифрования данных", "Для сортировки"], "correct": 1},
                    {"question": "Что вернёт np.percentile([1,2,3,4,5], 50)?", "options": ["2.5", "3.0", "2.0", "5.0"], "correct": 1},
                ],
                "task": {
                    "description": "Сгенерируй массив из 100 случайных целых чисел от 1 до 1000 (np.random.seed(42)).\nВычисли и выведи: среднее, медиану, стандартное отклонение, минимум, максимум и 25-й и 75-й перцентили.",
                    "example_input": "np.random.seed(42); data = np.random.randint(1, 1001, 100)",
                    "example_output": "Среднее: 523.17\nМедиана: 532.5\nСтд. откл.: 291.45\nМин: 10, Макс: 997\n25%: 278.75, 75%: 771.5",
                    "solution_hint": "np.mean, np.median, np.std, np.min, np.max, np.percentile",
                },
            },
            4: {
                "title": "NumPy: матричные операции",
                "theory": (
                    "📚 **Урок 1.4: Матрицы и reshape**\n\n"
                    "```python\n"
                    "import numpy as np\n\n"
                    "a = np.arange(12)\n"
                    "m = a.reshape(3, 4)\n"
                    "print(m.T)  # транспонирование\n\n"
                    "a = np.array([[1, 2], [3, 4]])\n"
                    "b = np.array([[5, 6], [7, 8]])\n\n"
                    "print(a + b)          # поэлементное\n"
                    "print(a @ b)          # матричное умножение\n"
                    "print(np.linalg.det(a))  # определитель\n"
                    "```\n\n"
                    "Конкатенация:\n"
                    "```python\n"
                    "x = np.array([1, 2, 3])\n"
                    "y = np.array([4, 5, 6])\n"
                    "np.concatenate([x, y])   # [1 2 3 4 5 6]\n"
                    "np.vstack([x, y])        # [[1 2 3] [4 5 6]]\n"
                    "```"
                ),
                "test": [
                    {"question": "Что делает метод .reshape(2, 6)?", "options": ["Удаляет элементы", "Изменяет форму массива на 2 строки и 6 столбцов", "Сортирует элементы", "Транспонирует массив"], "correct": 1},
                    {"question": "Какой оператор выполняет матричное умножение?", "options": ["*", "**", "@", "//"], "correct": 2},
                    {"question": "Что делает атрибут .T?", "options": ["Возвращает тип данных", "Транспонирует матрицу", "Возвращает количество элементов", "Сортирует по убыванию"], "correct": 1},
                ],
                "task": {
                    "description": "Создай массив от 1 до 9 и преобразуй его в матрицу 3x3.\nЗатем создай вторую матрицу 3x3 из единиц.\nВыведи: исходную матрицу, её транспонирование и результат матричного умножения на матрицу из единиц.",
                    "example_input": "a = np.arange(1, 10).reshape(3, 3)",
                    "example_output": "[[1 2 3]\n [4 5 6]\n [7 8 9]]\n\nТранспонированная...\n\nМатричное умножение...",
                    "solution_hint": "a.T, a @ np.ones((3,3))",
                },
            },
        },
    },
    2: {
        "title": "Pandas: работа с данными",
        "lessons": {
            1: {
                "title": "Series и DataFrame",
                "theory": (
                    "📚 **Урок 2.1: Pandas — основы**\n\n"
                    "```python\n"
                    "import pandas as pd\n\n"
                    "# Series\n"
                    "s = pd.Series([10, 20, 30], index=['a','b','c'])\n\n"
                    "# DataFrame\n"
                    "df = pd.DataFrame({\n"
                    "    'name': ['Анна', 'Иван', 'Мария'],\n"
                    "    'age':  [25, 30, 22],\n"
                    "    'city': ['Москва', 'СПб', 'Казань']\n"
                    "})\n\n"
                    "print(df.head())      # первые строки\n"
                    "print(df.shape)       # (3, 3)\n"
                    "print(df.dtypes)      # типы столбцов\n"
                    "print(df.describe())  # статистика\n"
                    "print(df['age'])      # столбец\n"
                    "```"
                ),
                "test": [
                    {"question": "Что такое DataFrame в Pandas?", "options": ["Одномерный массив", "Двумерная таблица данных", "Словарь Python", "Матрица NumPy"], "correct": 1},
                    {"question": "Что возвращает df.describe()?", "options": ["Описание ошибок", "Статистику: среднее, мин, макс и перцентили", "Названия столбцов", "Первые 5 строк"], "correct": 1},
                    {"question": "Как получить столбец 'price' из DataFrame df?", "options": ["df.price()", "df->price", "df['price']", "df.get_column('price')"], "correct": 2},
                ],
                "task": {
                    "description": "Создай DataFrame с информацией о 4 товарах: name, price, quantity, in_stock.\nВыведи: весь датафрейм, его форму, типы данных и статистику по числовым столбцам.",
                    "example_input": "Данные о товарах: ноутбук/75000/5/True, телефон/45000/12/True, планшет/30000/0/False, наушники/8000/20/True",
                    "example_output": "     name  price  quantity  in_stock\n0  ноутбук  75000         5      True\n...\nshape: (4, 4)",
                    "solution_hint": "pd.DataFrame({'name': [...], 'price': [...], ...})",
                },
            },
            2: {
                "title": "Чтение CSV, Excel, JSON",
                "theory": (
                    "📚 **Урок 2.2: Чтение и запись файлов**\n\n"
                    "```python\n"
                    "import pandas as pd\n\n"
                    "# CSV\n"
                    "df = pd.read_csv('data.csv', encoding='utf-8')\n"
                    "df.to_csv('output.csv', index=False)\n\n"
                    "# Excel\n"
                    "df = pd.read_excel('data.xlsx')\n"
                    "df.to_excel('output.xlsx', index=False)\n\n"
                    "# JSON\n"
                    "df = pd.read_json('data.json')\n"
                    "df.to_json('output.json', orient='records')\n\n"
                    "# Создать тестовый CSV\n"
                    "data = 'name,age,salary\\nАнна,25,80000\\nИван,32,120000'\n"
                    "with open('test.csv', 'w') as f:\n"
                    "    f.write(data)\n"
                    "df = pd.read_csv('test.csv')\n"
                    "print(df.info())\n"
                    "```"
                ),
                "test": [
                    {"question": "Какая функция читает CSV файл?", "options": ["pd.open_csv()", "pd.read_csv()", "pd.load_csv()", "pd.import_csv()"], "correct": 1},
                    {"question": "Зачем передавать index=False при сохранении?", "options": ["Чтобы ускорить сохранение", "Чтобы не сохранять индекс как отдельный столбец", "Чтобы сохранить только первый столбец", "Это обязательный параметр"], "correct": 1},
                    {"question": "Что показывает df.info()?", "options": ["Только названия столбцов", "Типы данных, количество непустых значений и память", "Первые 5 строк", "Статистику по числовым столбцам"], "correct": 1},
                ],
                "task": {
                    "description": "Создай CSV файл 'sales.csv' с данными: month, product, units, revenue.\nДобавь минимум 5 строк.\nПрочитай через pandas и выведи: первые 3 строки, форму, общую выручку и среднее количество единиц.",
                    "example_input": "Файл sales.csv с полями month, product, units, revenue",
                    "example_output": "Shape: (5, 4)\nОбщая выручка: ...\nСреднее units: ...",
                    "solution_hint": "df['revenue'].sum(), df['units'].mean()",
                },
            },
            3: {
                "title": "Фильтрация, сортировка, группировка",
                "theory": (
                    "📚 **Урок 2.3: Работа с данными**\n\n"
                    "```python\n"
                    "import pandas as pd\n\n"
                    "df = pd.DataFrame({\n"
                    "    'name': ['Анна', 'Иван', 'Мария', 'Пётр'],\n"
                    "    'dept': ['IT', 'HR', 'IT', 'HR'],\n"
                    "    'salary': [80000, 60000, 95000, 55000],\n"
                    "})\n\n"
                    "# Фильтрация\n"
                    "it = df[df['dept'] == 'IT']\n"
                    "rich = df[df['salary'] > 70000]\n\n"
                    "# Сортировка\n"
                    "df.sort_values('salary', ascending=False)\n\n"
                    "# Группировка\n"
                    "df.groupby('dept')['salary'].mean()\n"
                    "df.groupby('dept').agg({'salary': 'mean'})\n"
                    "```"
                ),
                "test": [
                    {"question": "Как отфильтровать строки где salary > 50000?", "options": ["df.filter(salary > 50000)", "df[df['salary'] > 50000]", "df.where('salary', 50000)", "df.select(salary > 50000)"], "correct": 1},
                    {"question": "Что делает df.groupby('city')['sales'].sum()?", "options": ["Фильтрует по городу", "Сортирует по городу", "Считает сумму продаж для каждого города", "Удаляет дубликаты"], "correct": 2},
                    {"question": "Как отсортировать по убыванию столбца 'age'?", "options": ["df.sort_values('age')", "df.sort_values('age', ascending=False)", "df.order_by('age', 'desc')", "df.sort('age', reverse=True)"], "correct": 1},
                ],
                "task": {
                    "description": "Создай DataFrame с 6 сотрудниками: name, department (IT/HR/Finance), salary, years_exp.\n1. Отфильтруй с опытом > 3 лет\n2. Отсортируй по зарплате по убыванию\n3. Средняя зарплата по отделам",
                    "example_input": "DataFrame с 6 сотрудниками",
                    "example_output": "Опыт > 3 лет: ...\nПо зарплате: ...\nСредняя по отделам:\n...",
                    "solution_hint": "groupby('department')['salary'].mean()",
                },
            },
            4: {
                "title": "Очистка данных",
                "theory": (
                    "📚 **Урок 2.4: Очистка данных**\n\n"
                    "```python\n"
                    "import pandas as pd\n\n"
                    "df = pd.DataFrame({\n"
                    "    'name': ['Анна', None, 'Мария'],\n"
                    "    'age': [25, 30, None],\n"
                    "    'salary': [80000, 90000, 80000]\n"
                    "})\n\n"
                    "# Пропуски\n"
                    "print(df.isnull().sum())\n"
                    "df.dropna()                         # удалить строки\n"
                    "df['age'].fillna(df['age'].mean())  # заполнить средним\n\n"
                    "# Дубликаты\n"
                    "df.drop_duplicates()\n\n"
                    "# Изменение типов\n"
                    "df['age'] = df['age'].astype(int)\n\n"
                    "# Переименование\n"
                    "df.rename(columns={'name': 'full_name'}, inplace=True)\n"
                    "```"
                ),
                "test": [
                    {"question": "Что возвращает df.isnull().sum()?", "options": ["Общее количество строк", "Количество пропусков в каждом столбце", "Сумму всех числовых значений", "Список строк с ошибками"], "correct": 1},
                    {"question": "Чем dropna() отличается от fillna(0)?", "options": ["Никакой разницы", "dropna удаляет строки с NaN, fillna заменяет NaN на значение", "dropna быстрее", "fillna удаляет строки"], "correct": 1},
                    {"question": "Как удалить дублирующиеся строки?", "options": ["df.remove_duplicates()", "df.drop_duplicates()", "df.delete_duplicates()", "df.unique()"], "correct": 1},
                ],
                "task": {
                    "description": "Создай DataFrame с намеренно грязными данными: 2 строки с None и 1 полный дубликат.\n1. Выведи количество пропусков\n2. Заполни числовые пропуски средним\n3. Удали дубликаты\n4. Выведи чистый DataFrame",
                    "example_input": "DataFrame с пропусками и дубликатами",
                    "example_output": "Пропуски:\n...\nПосле очистки:\n...",
                    "solution_hint": "fillna(df[col].mean()), drop_duplicates()",
                },
            },
        },
    },
    3: {
        "title": "Matplotlib: визуализация",
        "lessons": {
            1: {
                "title": "Линейные графики",
                "theory": (
                    "📚 **Урок 3.1: Matplotlib — основы**\n\n"
                    "```python\n"
                    "import matplotlib.pyplot as plt\n"
                    "import numpy as np\n\n"
                    "x = np.linspace(0, 10, 100)\n"
                    "y = np.sin(x)\n\n"
                    "plt.figure(figsize=(10, 5))\n"
                    "plt.plot(x, y, color='blue', linewidth=2, label='sin(x)')\n"
                    "plt.plot(x, np.cos(x), 'r--', label='cos(x)')\n\n"
                    "plt.title('Тригонометрические функции')\n"
                    "plt.xlabel('x')\n"
                    "plt.ylabel('y')\n"
                    "plt.legend()\n"
                    "plt.grid(True)\n"
                    "plt.savefig('plot.png')\n"
                    "plt.show()\n"
                    "```\n\n"
                    "Subplots:\n"
                    "```python\n"
                    "fig, axes = plt.subplots(1, 2, figsize=(12, 4))\n"
                    "axes[0].plot(x, np.sin(x))\n"
                    "axes[1].plot(x, np.cos(x), 'r')\n"
                    "plt.tight_layout()\n"
                    "```"
                ),
                "test": [
                    {"question": "Какая функция сохраняет график?", "options": ["plt.save()", "plt.savefig()", "plt.export()", "plt.write()"], "correct": 1},
                    {"question": "Что делает plt.legend()?", "options": ["Добавляет заголовок", "Показывает легенду", "Рисует сетку", "Сохраняет файл"], "correct": 1},
                    {"question": "Как создать два графика рядом?", "options": ["plt.double()", "plt.subplots(1, 2)", "plt.plot() дважды", "plt.split(2)"], "correct": 1},
                ],
                "task": {
                    "description": "Создай график с двумя линиями:\n1. y = x^2 от -5 до 5 (синяя)\n2. y = x^3/10 от -5 до 5 (красная пунктирная)\nДобавь заголовок, оси, легенду, сетку. Сохрани как 'functions.png'.",
                    "example_input": "x = np.linspace(-5, 5, 100)",
                    "example_output": "График сохранён в functions.png",
                    "solution_hint": "plt.plot(x, x**2, label='x^2'); plt.plot(x, x**3/10, 'r--', label='x^3/10')",
                },
            },
            2: {
                "title": "Гистограммы и столбчатые диаграммы",
                "theory": (
                    "📚 **Урок 3.2: Bar и Histogram**\n\n"
                    "```python\n"
                    "import matplotlib.pyplot as plt\n"
                    "import numpy as np\n\n"
                    "# Гистограмма\n"
                    "data = np.random.normal(170, 10, 500)\n"
                    "plt.hist(data, bins=30, color='steelblue', edgecolor='white')\n"
                    "plt.title('Распределение роста')\n"
                    "plt.show()\n\n"
                    "# Столбчатая\n"
                    "categories = ['Q1', 'Q2', 'Q3', 'Q4']\n"
                    "values = [125, 180, 150, 200]\n"
                    "plt.bar(categories, values, color='steelblue')\n"
                    "for i, v in enumerate(values):\n"
                    "    plt.text(i, v + 2, str(v), ha='center')\n"
                    "plt.show()\n"
                    "```"
                ),
                "test": [
                    {"question": "Чем гистограмма отличается от bar chart?", "options": ["Гистограмма цветная", "Гистограмма — распределение чисел, bar — сравнение категорий", "Bar точнее", "Никакой разницы"], "correct": 1},
                    {"question": "Что означает bins=30 в plt.hist()?", "options": ["Цвет", "Количество интервалов", "Ширину", "Максимум"], "correct": 1},
                    {"question": "Что делает alpha=0.7?", "options": ["Меняет цвет", "Задаёт прозрачность", "Меняет ширину", "Добавляет тень"], "correct": 1},
                ],
                "task": {
                    "description": "Создай два графика (subplots 1x2):\n1. Гистограмму из 1000 случайных чисел (mean=50, std=15), bins=25\n2. Bar chart продаж за 6 месяцев (120,145,160,135,180,200)\nСохрани как 'charts.png'.",
                    "example_input": "np.random.seed(42)",
                    "example_output": "График сохранён в charts.png",
                    "solution_hint": "fig, (ax1, ax2) = plt.subplots(1, 2); ax1.hist(...); ax2.bar(...)",
                },
            },
            3: {
                "title": "Scatter и Pie chart",
                "theory": (
                    "📚 **Урок 3.3: Scatter и Pie**\n\n"
                    "```python\n"
                    "import matplotlib.pyplot as plt\n"
                    "import numpy as np\n\n"
                    "# Scatter\n"
                    "x = np.random.randn(100)\n"
                    "y = 2 * x + np.random.randn(100) * 0.5\n"
                    "plt.scatter(x, y, c='steelblue', alpha=0.6, s=50)\n"
                    "plt.show()\n\n"
                    "# Pie\n"
                    "labels = ['Python', 'JS', 'Java', 'C++']\n"
                    "sizes = [35, 25, 25, 15]\n"
                    "plt.pie(sizes, labels=labels, autopct='%1.1f%%')\n"
                    "plt.show()\n"
                    "```"
                ),
                "test": [
                    {"question": "Когда лучше scatter plot?", "options": ["Для долей", "Для одной переменной", "Для связи двух числовых переменных", "Для категорий"], "correct": 2},
                    {"question": "Что делает autopct='%1.1f%%'?", "options": ["Задаёт цвета", "Добавляет проценты к сегментам", "Вращает диаграмму", "Убирает легенду"], "correct": 1},
                    {"question": "Параметр s в scatter отвечает за:", "options": ["Цвет", "Форму", "Размер точек", "Прозрачность"], "correct": 2},
                ],
                "task": {
                    "description": "Создай два графика:\n1. Scatter из 200 точек (seed=42), цвет зависит от значения x\n2. Pie chart бюджета: Зарплаты 45%, Маркетинг 20%, Разработка 25%, Прочее 10%\nСохрани как 'scatter_pie.png'.",
                    "example_input": "np.random.seed(42)",
                    "example_output": "График сохранён в scatter_pie.png",
                    "solution_hint": "plt.scatter(x, y, c=x, cmap='viridis'); plt.colorbar()",
                },
            },
            4: {
                "title": "Стили и настройка",
                "theory": (
                    "📚 **Урок 3.4: Профессиональные графики**\n\n"
                    "```python\n"
                    "import matplotlib.pyplot as plt\n"
                    "import numpy as np\n\n"
                    "plt.style.use('seaborn-v0_8')\n\n"
                    "x = np.linspace(0, 10, 100)\n"
                    "y = np.sin(x)\n\n"
                    "fig, ax = plt.subplots(figsize=(10, 5))\n"
                    "ax.plot(x, y, 'b-', linewidth=2)\n\n"
                    "# Аннотация\n"
                    "ax.annotate('Максимум', xy=(np.pi/2, 1),\n"
                    "            xytext=(3, 0.8),\n"
                    "            arrowprops=dict(arrowstyle='->'))\n\n"
                    "# Линия и заливка\n"
                    "ax.axhline(y=0, color='k', linestyle='--', linewidth=0.8)\n"
                    "ax.fill_between(x, y, 0, where=(y>0), alpha=0.3, color='green')\n\n"
                    "plt.savefig('styled.png', dpi=150, bbox_inches='tight')\n"
                    "```"
                ),
                "test": [
                    {"question": "Что делает plt.style.use('ggplot')?", "options": ["Устанавливает библиотеку", "Применяет стиль оформления", "Импортирует R", "Меняет фон"], "correct": 1},
                    {"question": "Что делает fill_between()?", "options": ["Рисует точки", "Закрашивает область", "Добавляет сетку", "Рисует стрелку"], "correct": 1},
                    {"question": "dpi в savefig отвечает за:", "options": ["Размер файла", "Разрешение изображения", "Формат", "Цвет"], "correct": 1},
                ],
                "task": {
                    "description": "Создай профессиональный график продаж за 12 месяцев.\nСтиль: seaborn-v0_8. Закрась область под кривой, добавь горизонтальную линию среднего, аннотацию к максимуму.\nСохрани как 'professional.png' с dpi=150.",
                    "example_input": "sales = [120,135,148,162,145,178,195,187,201,215,198,230]",
                    "example_output": "График сохранён в professional.png",
                    "solution_hint": "ax.fill_between(x, y, alpha=0.3); ax.axhline(y=np.mean(y), linestyle='--')",
                },
            },
        },
    },
    4: {
        "title": "Seaborn: красивые графики",
        "lessons": {
            1: {
                "title": "Введение, heatmap",
                "theory": (
                    "📚 **Урок 4.1: Seaborn**\n\n"
                    "```python\n"
                    "import seaborn as sns\n"
                    "import matplotlib.pyplot as plt\n\n"
                    "sns.set_theme(style='whitegrid')\n\n"
                    "# Heatmap корреляций\n"
                    "tips = sns.load_dataset('tips')\n"
                    "corr = tips.select_dtypes('number').corr()\n\n"
                    "sns.heatmap(corr, annot=True, fmt='.2f',\n"
                    "            cmap='coolwarm', vmin=-1, vmax=1)\n"
                    "plt.title('Матрица корреляций')\n"
                    "plt.show()\n\n"
                    "# Встроенные датасеты\n"
                    "tips = sns.load_dataset('tips')\n"
                    "iris = sns.load_dataset('iris')\n"
                    "titanic = sns.load_dataset('titanic')\n"
                    "```"
                ),
                "test": [
                    {"question": "Для чего heatmap?", "options": ["Для географии", "Для матриц и корреляций через цвет", "Для рядов", "Для pie"], "correct": 1},
                    {"question": "Что делает annot=True в heatmap?", "options": ["Аннотации к осям", "Числа в ячейках", "Границы ячеек", "Легенда"], "correct": 1},
                    {"question": "Что вычисляет df.corr()?", "options": ["Среднее", "Матрицу корреляций", "Уникальные значения", "Отклонение"], "correct": 1},
                ],
                "task": {
                    "description": "Загрузи tips (sns.load_dataset('tips')).\nСоздай heatmap корреляций числовых столбцов.\ncmap='RdYlGn', annot=True, fmt='.2f'.\nСохрани как 'correlation.png'.",
                    "example_input": "tips = sns.load_dataset('tips')",
                    "example_output": "Heatmap сохранён в correlation.png",
                    "solution_hint": "tips.select_dtypes('number').corr()",
                },
            },
            2: {
                "title": "Boxplot, violinplot, histplot",
                "theory": (
                    "📚 **Урок 4.2: Распределения**\n\n"
                    "```python\n"
                    "import seaborn as sns\n"
                    "import matplotlib.pyplot as plt\n\n"
                    "tips = sns.load_dataset('tips')\n"
                    "fig, axes = plt.subplots(1, 3, figsize=(15, 5))\n\n"
                    "sns.histplot(data=tips, x='total_bill', kde=True, ax=axes[0])\n"
                    "sns.boxplot(data=tips, x='day', y='total_bill', ax=axes[1])\n"
                    "sns.violinplot(data=tips, x='day', y='tip', ax=axes[2])\n\n"
                    "plt.tight_layout()\n"
                    "plt.show()\n"
                    "```"
                ),
                "test": [
                    {"question": "Что показывает линия внутри boxplot?", "options": ["Среднее", "Медиану", "Моду", "Максимум"], "correct": 1},
                    {"question": "Чем violinplot лучше boxplot?", "options": ["Больше данных", "Показывает форму распределения", "Быстрее", "Выбросы"], "correct": 1},
                    {"question": "Что такое KDE в histplot?", "options": ["Тип данных", "Сглаженная кривая распределения", "Цвет", "Интервалы"], "correct": 1},
                ],
                "task": {
                    "description": "Загрузи iris.\nСоздай три графика:\n1. Histplot с KDE для sepal_length\n2. Boxplot sepal_width по species\n3. Violinplot petal_length по species\nСохрани как 'distributions.png'.",
                    "example_input": "iris = sns.load_dataset('iris')",
                    "example_output": "distributions.png сохранён",
                    "solution_hint": "fig, axes = plt.subplots(1,3); sns.histplot(kde=True, ax=axes[0])",
                },
            },
            3: {
                "title": "Scatterplot и regplot",
                "theory": (
                    "📚 **Урок 4.3: Scatter и регрессия**\n\n"
                    "```python\n"
                    "import seaborn as sns\n"
                    "import matplotlib.pyplot as plt\n\n"
                    "tips = sns.load_dataset('tips')\n"
                    "fig, axes = plt.subplots(1, 2, figsize=(14, 5))\n\n"
                    "sns.scatterplot(data=tips, x='total_bill', y='tip',\n"
                    "                hue='sex', size='size', ax=axes[0])\n\n"
                    "sns.regplot(data=tips, x='total_bill', y='tip',\n"
                    "            line_kws={'color': 'red'}, ax=axes[1])\n\n"
                    "plt.tight_layout()\n"
                    "```"
                ),
                "test": [
                    {"question": "Что делает hue в seaborn?", "options": ["Меняет яркость", "Раскрашивает по значению столбца", "Сетка", "Форма точек"], "correct": 1},
                    {"question": "Чем regplot отличается от scatterplot?", "options": ["Быстрее", "Добавляет линию регрессии", "Не поддерживает цвет", "Нет разницы"], "correct": 1},
                    {"question": "Что показывает затенение у линии регрессии?", "options": ["Отклонение", "Доверительный интервал", "Диапазон", "Ошибку"], "correct": 1},
                ],
                "task": {
                    "description": "Загрузи tips.\nДва графика рядом:\n1. Scatterplot total_bill vs tip, hue='smoker', style='sex'\n2. Regplot тех же осей, красная линия\nСохрани как 'regression.png'.",
                    "example_input": "tips = sns.load_dataset('tips')",
                    "example_output": "regression.png сохранён",
                    "solution_hint": "sns.scatterplot(hue='smoker', style='sex'); sns.regplot(line_kws={'color':'red'})",
                },
            },
            4: {
                "title": "Pairplot и catplot",
                "theory": (
                    "📚 **Урок 4.4: Pairplot и catplot**\n\n"
                    "```python\n"
                    "import seaborn as sns\n"
                    "import matplotlib.pyplot as plt\n\n"
                    "iris = sns.load_dataset('iris')\n"
                    "sns.pairplot(iris, hue='species', diag_kind='kde')\n"
                    "plt.savefig('pairplot.png', bbox_inches='tight')\n\n"
                    "tips = sns.load_dataset('tips')\n"
                    "sns.catplot(data=tips, x='day', y='total_bill',\n"
                    "            hue='sex', kind='bar', palette='Set1')\n"
                    "plt.show()\n"
                    "```"
                ),
                "test": [
                    {"question": "Что строит pairplot?", "options": ["Один scatter", "Матрицу попарных зависимостей", "Heatmap", "Гистограммы"], "correct": 1},
                    {"question": "kind='bar' в catplot строит:", "options": ["Scatter", "Линию", "Столбчатую", "Heatmap"], "correct": 2},
                    {"question": "Что на диагонали pairplot?", "options": ["Scatter", "Распределение каждой переменной", "Корреляции", "Пустые ячейки"], "correct": 1},
                ],
                "task": {
                    "description": "Загрузи tips.\n1. Pairplot с hue='sex', diag_kind='hist'. Сохрани как 'pairplot.png'.\n2. Catplot x='day', y='tip', hue='smoker', kind='violin'. Сохрани как 'catplot.png'.",
                    "example_input": "tips = sns.load_dataset('tips')",
                    "example_output": "pairplot.png и catplot.png сохранены",
                    "solution_hint": "sns.pairplot(tips, hue='sex', diag_kind='hist')",
                },
            },
        },
    },
    5: {
        "title": "Продвинутый Pandas",
        "lessons": {
            1: {
                "title": "GroupBy и агрегации",
                "theory": (
                    "📚 **Урок 5.1: Продвинутый GroupBy**\n\n"
                    "```python\n"
                    "import pandas as pd\n\n"
                    "df = pd.DataFrame({\n"
                    "    'region': ['Север','Север','Юг','Юг'],\n"
                    "    'product': ['A','B','A','B'],\n"
                    "    'sales': [100, 150, 200, 120],\n"
                    "})\n\n"
                    "# Несколько агрегаций\n"
                    "df.groupby('region').agg(\n"
                    "    total=('sales', 'sum'),\n"
                    "    avg=('sales', 'mean')\n"
                    ").reset_index()\n\n"
                    "# Transform — сохраняет длину\n"
                    "df['region_avg'] = df.groupby('region')['sales'].transform('mean')\n\n"
                    "# Pivot table\n"
                    "df.pivot_table(values='sales', index='region',\n"
                    "               columns='product', aggfunc='sum')\n"
                    "```"
                ),
                "test": [
                    {"question": "Что делает transform('mean')?", "options": ["Удаляет столбец", "Добавляет среднее по группе сохраняя длину", "Сжимает датафрейм", "Сортирует"], "correct": 1},
                    {"question": "Для чего pivot_table?", "options": ["Удалить строки", "Создать сводную таблицу", "Транспонировать", "Сортировать"], "correct": 1},
                    {"question": "Что делает reset_index() после groupby?", "options": ["Удаляет индекс", "Индекс группы становится столбцом", "Сбрасывает данные", "Нумерует с нуля"], "correct": 1},
                ],
                "task": {
                    "description": "Создай DataFrame: region, category, sales, cost (12+ строк).\n1. Сумма продаж и средняя прибыль по регионам\n2. Pivot: регионы x категории, сумма продаж\n3. Столбец 'pct_of_region' — доля продаж в своём регионе",
                    "example_input": "DataFrame 12+ строк",
                    "example_output": "GroupBy и pivot table",
                    "solution_hint": "df['sales'] / df.groupby('region')['sales'].transform('sum')",
                },
            },
            2: {
                "title": "Merge, join, concat",
                "theory": (
                    "📚 **Урок 5.2: Объединение**\n\n"
                    "```python\n"
                    "import pandas as pd\n\n"
                    "employees = pd.DataFrame({'id':[1,2,3], 'name':['А','И','М'], 'dept_id':[1,2,1]})\n"
                    "departments = pd.DataFrame({'dept_id':[1,2], 'name':['IT','HR']})\n\n"
                    "# INNER JOIN\n"
                    "pd.merge(employees, departments, on='dept_id')\n\n"
                    "# LEFT JOIN\n"
                    "pd.merge(employees, departments, on='dept_id', how='left')\n\n"
                    "# Concat вертикально\n"
                    "pd.concat([df1, df2], ignore_index=True)\n\n"
                    "# Concat горизонтально\n"
                    "pd.concat([df1, df2], axis=1)\n"
                    "```"
                ),
                "test": [
                    {"question": "Чем left join отличается от inner?", "options": ["Быстрее", "Все строки левого, даже без совпадений", "По индексу", "Нет разницы"], "correct": 1},
                    {"question": "concat([df1,df2], axis=0):", "options": ["По горизонтали", "По вертикали", "Inner join", "Транспонирует"], "correct": 1},
                    {"question": "Зачем ignore_index=True в concat?", "options": ["Дубликаты", "Сброс индекса 0,1,2...", "Игнорирует NaN", "Ускоряет"], "correct": 1},
                ],
                "task": {
                    "description": "Создай: orders (order_id, customer_id, product_id, amount), customers (customer_id, name, city), products (product_id, name, category).\nОбъедини все три через merge.\nДобавь 2 заказа через concat.",
                    "example_input": "Три датафрейма",
                    "example_output": "Объединённая таблица заказов",
                    "solution_hint": "pd.merge(orders, customers, on='customer_id').merge(products, on='product_id')",
                },
            },
            3: {
                "title": "Apply, map, lambda",
                "theory": (
                    "📚 **Урок 5.3: Функции к данным**\n\n"
                    "```python\n"
                    "import pandas as pd\n\n"
                    "df = pd.DataFrame({'name':['анна','ИВАН'], 'salary':[80000,120000], 'age':[25,32]})\n\n"
                    "# map — к каждому элементу\n"
                    "df['salary_k'] = df['salary'].map(lambda x: f'{x//1000}k')\n\n"
                    "# apply к столбцу\n"
                    "df['name'] = df['name'].apply(str.title)\n\n"
                    "# apply к строке\n"
                    "def grade(row):\n"
                    "    if row['salary'] > 100000: return 'Senior'\n"
                    "    elif row['salary'] > 80000: return 'Middle'\n"
                    "    return 'Junior'\n\n"
                    "df['level'] = df.apply(grade, axis=1)\n"
                    "```"
                ),
                "test": [
                    {"question": "apply(axis=1) vs apply(axis=0)?", "options": ["axis=1 быстрее", "axis=1 — к строкам, axis=0 — к столбцам", "axis=0 — к строкам", "Нет разницы"], "correct": 1},
                    {"question": "Что такое .map() в Series?", "options": ["Merge", "Функция к каждому элементу", "Новый DataFrame", "Фильтр"], "correct": 1},
                    {"question": "Зачем apply вместо for?", "options": ["Не работает с большими", "Нет разницы", "Оптимизирован, быстрее", "Для читаемости"], "correct": 2},
                ],
                "task": {
                    "description": "DataFrame с 5 сотрудниками: name, salary, department, years_exp.\nДобавь:\n1. 'tax' — 13% от salary\n2. 'net_salary' — salary - tax\n3. 'grade' — Junior(<3), Middle(3-6), Senior(>6)\n4. 'name_upper' — имя заглавными",
                    "example_input": "DataFrame с 5 сотрудниками",
                    "example_output": "DataFrame с новыми столбцами",
                    "solution_hint": "apply(lambda row: 'Senior' if row['years_exp']>6 else ..., axis=1)",
                },
            },
            4: {
                "title": "Временные ряды",
                "theory": (
                    "📚 **Урок 5.4: Time Series**\n\n"
                    "```python\n"
                    "import pandas as pd\n"
                    "import numpy as np\n\n"
                    "dates = pd.date_range('2024-01-01', periods=365, freq='D')\n"
                    "ts = pd.Series(np.random.randn(365).cumsum() + 100, index=dates)\n\n"
                    "# Ресемплинг\n"
                    "ts.resample('ME').mean()  # по месяцам\n"
                    "ts.resample('W').sum()    # по неделям\n\n"
                    "# Скользящее среднее\n"
                    "ts.rolling(7).mean()   # 7-дневное\n"
                    "ts.rolling(30).std()   # 30-дневное\n\n"
                    "# Атрибуты дат\n"
                    "df['month'] = df['date'].dt.month\n"
                    "df['dayofweek'] = df['date'].dt.dayofweek\n"
                    "df['quarter'] = df['date'].dt.quarter\n"
                    "```"
                ),
                "test": [
                    {"question": "Что делает resample('ME').mean()?", "options": ["Удаляет пропуски", "Среднее по месяцам", "Фильтрует", "Прогноз"], "correct": 1},
                    {"question": "Что такое rolling mean?", "options": ["Среднее всего", "Среднее за N периодов", "Прогноз", "Медиана"], "correct": 1},
                    {"question": "Как получить месяц из дат?", "options": ["df['date'].month", "df['date'].dt.month", "pd.month()", "df['date'].get_month()"], "correct": 1},
                ],
                "task": {
                    "description": "Создай ряд ежедневных продаж за 2024 год (seed=42).\n1. Среднемесячные продажи\n2. 7-дневное скользящее среднее\n3. Столбцы: month, dayofweek, quarter\n4. День недели с наибольшими продажами",
                    "example_input": "np.random.seed(42); dates = pd.date_range('2024-01-01', periods=366, freq='D')",
                    "example_output": "Месячные:\n...\nЛучший день: ...",
                    "solution_hint": "df.groupby('dayofweek')['sales'].mean().idxmax()",
                },
            },
        },
    },
    6: {
        "title": "Финальный проект",
        "lessons": {
            1: {
                "title": "EDA: исследовательский анализ",
                "theory": (
                    "📚 **Урок 6.1: EDA**\n\n"
                    "```python\n"
                    "import pandas as pd\n"
                    "import seaborn as sns\n\n"
                    "df = sns.load_dataset('titanic')\n\n"
                    "# Обзор\n"
                    "print(df.shape)\n"
                    "print(df.dtypes)\n"
                    "print(df.describe())\n"
                    "print(df.isnull().sum())\n\n"
                    "# Анализ\n"
                    "df.groupby('pclass')['survived'].mean()\n\n"
                    "# Корреляции\n"
                    "sns.heatmap(df.select_dtypes('number').corr(), annot=True)\n\n"
                    "# Вывод\n"
                    "print(f'Выживаемость: {df[\"survived\"].mean():.1%}')\n"
                    "```"
                ),
                "test": [
                    {"question": "Что такое EDA?", "options": ["ML модель", "Исследовательский анализ данных", "Визуализация", "Очистка"], "correct": 1},
                    {"question": "Первый шаг EDA?", "options": ["Модель", "Обзор: форма, типы, пропуски", "Корреляции", "Выбросы"], "correct": 1},
                    {"question": "Зачем df.describe()?", "options": ["Типы", "Статистика числовых столбцов", "Дубликаты", "Графики"], "correct": 1},
                ],
                "task": {
                    "description": "Загрузи tips и проведи полный EDA:\n1. Размер, типы, пропуски\n2. Статистика\n3. Средние чаевые по дням и времени\n4. Heatmap корреляций\n5. Три вывода: 'Вывод: ...'",
                    "example_input": "tips = sns.load_dataset('tips')",
                    "example_output": "Размер: (244, 7)\n...\nВывод: ...",
                    "solution_hint": "groupby(['day','time'])['tip'].mean()",
                },
            },
            2: {
                "title": "Plotly: интерактивные графики",
                "theory": (
                    "📚 **Урок 6.2: Plotly**\n\n"
                    "```python\n"
                    "import plotly.express as px\n\n"
                    "df = px.data.gapminder().query('year == 2007')\n"
                    "fig = px.scatter(df, x='gdpPercap', y='lifeExp',\n"
                    "                 size='pop', color='continent',\n"
                    "                 hover_name='country', log_x=True)\n"
                    "fig.show()\n"
                    "fig.write_html('chart.html')\n\n"
                    "# Line\n"
                    "fig2 = px.line(df2, x='year', y='gdpPercap')\n\n"
                    "# Bar\n"
                    "fig3 = px.bar(tips, x='day', y='tip',\n"
                    "              color='sex', barmode='group')\n"
                    "```"
                ),
                "test": [
                    {"question": "Plotly vs Matplotlib?", "options": ["Plotly только 3D", "Plotly интерактивный, Matplotlib статичный", "Matplotlib быстрее", "Plotly не работает с DF"], "correct": 1},
                    {"question": "Как сохранить как HTML?", "options": ["fig.save()", "fig.write_html()", "px.export()", "fig.to_html()"], "correct": 1},
                    {"question": "hover_name делает:", "options": ["Заголовок", "Имя при наведении", "Цвет", "Легенда"], "correct": 1},
                ],
                "task": {
                    "description": "Загрузи gapminder (px.data.gapminder()).\n1. Scatter 2007: x=gdpPercap, y=lifeExp, size=pop, color=continent, log_x=True. Сохрани 'scatter.html'\n2. Line Россия и Германия: y='lifeExp'. Сохрани 'lines.html'",
                    "example_input": "import plotly.express as px",
                    "example_output": "scatter.html и lines.html сохранены",
                    "solution_hint": "df.query('country in [\"Russia\", \"Germany\"]')",
                },
            },
            3: {
                "title": "Статистический анализ",
                "theory": (
                    "📚 **Урок 6.3: Статистика и гипотезы**\n\n"
                    "```python\n"
                    "import seaborn as sns\n"
                    "from scipy import stats\n\n"
                    "tips = sns.load_dataset('tips')\n\n"
                    "# Корреляция\n"
                    "corr, pval = stats.pearsonr(tips['total_bill'], tips['tip'])\n"
                    "print(f'r={corr:.3f}, p={pval:.4f}')\n\n"
                    "# T-тест\n"
                    "lunch = tips[tips['time']=='Lunch']['tip']\n"
                    "dinner = tips[tips['time']=='Dinner']['tip']\n"
                    "t, p = stats.ttest_ind(lunch, dinner)\n"
                    "if p < 0.05:\n"
                    "    print('Различие значимо')\n"
                    "```"
                ),
                "test": [
                    {"question": "p-value < 0.05 означает?", "options": ["Гипотеза подтверждена", "Значимо с 95% вероятностью", "Мало данных", "Высокая корреляция"], "correct": 1},
                    {"question": "Корреляция Пирсона измеряет?", "options": ["Разницу средних", "Силу линейной связи (-1 до 1)", "Вероятность", "Отклонение"], "correct": 1},
                    {"question": "T-тест используют для:", "options": ["Графиков", "Сравнения средних двух групп", "Очистки", "Прогноза"], "correct": 1},
                ],
                "task": {
                    "description": "Загрузи tips.\n1. Корреляция total_bill и tip\n2. T-тест: чаевые курящих vs некурящих\n3. Средние по дням с выводом\n4. Вывод по каждому пункту",
                    "example_input": "tips = sns.load_dataset('tips')",
                    "example_output": "Корреляция: 0.676, p<0.001\nT-тест: p=...\n...",
                    "solution_hint": "stats.ttest_ind(smokers['tip'], non_smokers['tip'])",
                },
            },
            4: {
                "title": "Финальный проект: Titanic",
                "theory": (
                    "📚 **Урок 6.4: Полный аналитический проект**\n\n"
                    "Структура профессионального анализа:\n\n"
                    "```python\n"
                    "import pandas as pd\n"
                    "import numpy as np\n"
                    "import matplotlib.pyplot as plt\n"
                    "import seaborn as sns\n"
                    "from scipy import stats\n\n"
                    "df = sns.load_dataset('titanic')\n\n"
                    "# 1. Обзор\n"
                    "print(f'Строк: {df.shape[0]}')\n"
                    "print(df.isnull().sum())\n\n"
                    "# 2. Очистка\n"
                    "df['age'].fillna(df['age'].median(), inplace=True)\n\n"
                    "# 3. Анализ\n"
                    "by_class = df.groupby('pclass')['survived'].mean()\n"
                    "by_sex = df.groupby('sex')['survived'].mean()\n\n"
                    "# 4. Дашборд\n"
                    "fig, axes = plt.subplots(2, 2, figsize=(12, 10))\n"
                    "# ...\n\n"
                    "# 5. Выводы\n"
                    "print(f'Выжили: {df[\"survived\"].mean():.1%}')\n"
                    "```"
                ),
                "test": [
                    {"question": "Результат аналитического проекта?", "options": ["Только графики", "Данные, визуализации и выводы", "Только статистика", "ML модель"], "correct": 1},
                    {"question": "Зачем документировать выводы?", "options": ["Необязательно", "Для решений без технических деталей", "Для размера", "Для себя"], "correct": 1},
                    {"question": "Порядок шагов:", "options": ["Выводы→Очистка→Загрузка", "Загрузка→Очистка→Анализ→Визуализация→Выводы", "Визуализация→Загрузка", "Анализ→Загрузка"], "correct": 1},
                ],
                "task": {
                    "description": "Финальный проект! Titanic, полный анализ:\n1. Обзор (shape, dtypes, пропуски)\n2. Очистка (age — медиана, embarked — мода)\n3. Выживаемость по классу, полу, возрасту\n4. Дашборд 2x2: выживаемость по классам, по полу, распределение возраста, heatmap корреляций\n5. T-тест: возраст выживших vs погибших\n6. Минимум 5 выводов\nСохрани как 'titanic_analysis.png'.",
                    "example_input": "df = sns.load_dataset('titanic')",
                    "example_output": "Полный анализ с графиками и выводами",
                    "solution_hint": "fig, axes = plt.subplots(2,2,figsize=(14,10))",
                },
            },
        },
    },
}
