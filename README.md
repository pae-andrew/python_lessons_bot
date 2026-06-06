# Python Learning Telegram Bot

Telegram-бот для обучения программированию на Python с уроками, тестами и проверкой кода через Claude API.

## Возможности

- 📚 Теория с примерами кода
- 🧪 Тесты с вариантами ответов (InlineKeyboard)
- 💻 Практические задачи с AI-проверкой
- ⭐ Система баллов и отслеживание прогресса
- 🗄️ Локальная SQLite БД (готово к миграции на Supabase)

## Требования

- Python 3.11+
- Токен Telegram-бота ([@BotFather](https://t.me/BotFather))
- API-ключ [Anthropic](https://console.anthropic.com/)

## Установка

```bash
# Перейти в папку проекта
cd Projects

# Создать виртуальное окружение
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Установить зависимости
pip install -r requirements.txt

# Настроить переменные окружения
cp .env.example .env
# Отредактировать .env — указать BOT_TOKEN и ANTHROPIC_API_KEY
```

## Запуск

```bash
cd bot
python main.py
```

## Команды бота

| Команда | Описание |
|---------|----------|
| `/start` | Регистрация и главное меню |
| `/lesson` | Теория текущего урока |
| `/test` | Тест по текущему уроку |
| `/task` | Практическая задача |
| `/progress` | Статистика и прогресс |
| `/next` | Следующий урок (после сдачи теста и задачи) |

## Логика прогресса

- **Тест:** +10 баллов за каждый правильный ответ (минимум 2/3 для зачёта)
- **Задача:** +30 баллов («Отлично»), +20 баллов («Хорошо»)
- **Следующий урок:** доступен после сдачи теста и задачи с оценкой не ниже «Хорошо»

## Структура проекта

```
bot/
├── main.py              # Точка входа
├── config.py            # Загрузка .env
├── database.py          # SQLite через aiosqlite
├── handlers/
│   ├── start.py         # /start
│   ├── lesson.py        # /lesson
│   ├── test.py          # /test
│   ├── task.py          # /task, /next
│   └── progress.py      # /progress
├── content/
│   └── curriculum.py    # Учебная программа
└── services/
    └── ai_checker.py    # Проверка кода через Claude
```

## Учебная программа

**Модуль 1 — Основы Python**
- 1.1 print() и переменные
- 1.2 Типы данных (str, int, float, bool)
- 1.3 Ввод данных через input()

**Модуль 2 — Условия и циклы**
- 2.1 if / elif / else
- 2.2 Цикл for и range()
- 2.3 Цикл while

## Переменные окружения

| Переменная | Описание |
|------------|----------|
| `BOT_TOKEN` | Токен Telegram-бота |
| `ANTHROPIC_API_KEY` | Ключ Anthropic API |

## Разработка

База данных создаётся автоматически при первом запуске (`bot_data.db` в рабочей директории).

Для добавления новых модулей отредактируйте `bot/content/curriculum.py`.
