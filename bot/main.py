import asyncio
import logging
import sys
import config as cfg

from aiogram import BaseMiddleware, Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from typing import Any, Awaitable, Callable

from config import Config, load_config
from database import init_db
from handlers import lesson, progress, start, task, test

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    stream=sys.stdout,
)
logger = logging.getLogger(__name__)


class ConfigMiddleware(BaseMiddleware):
    def __init__(self, config: Config) -> None:
        self.config = config

    async def __call__(
        self,
        handler: Callable[[Any, dict[str, Any]], Awaitable[Any]],
        event: Any,
        data: dict[str, Any],
    ) -> Any:
        data["config"] = self.config
        return await handler(event, data)


async def main() -> None:
    try:
        config = load_config()
    except ValueError as e:
        logger.error("%s", e)
        sys.exit(1)

    await init_db(url=cfg.supabase_url, key=cfg.supabase_key)

    bot = Bot(token=config.bot_token)
    dp = Dispatcher(storage=MemoryStorage())
    dp.update.middleware(ConfigMiddleware(config))

    dp.include_router(start.router)
    dp.include_router(lesson.router)
    dp.include_router(test.router)
    dp.include_router(task.router)
    dp.include_router(progress.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())