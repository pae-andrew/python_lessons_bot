import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR.parent / ".env")
load_dotenv(BASE_DIR / ".env")
supabase_url: str = os.getenv("SUPABASE_URL", "")
supabase_key: str = os.getenv("SUPABASE_KEY", "")


@dataclass(frozen=True)
class Config:
    bot_token: str
    anthropic_api_key: str
    claude_model: str = "claude-sonnet-4-6"
    db_path: str = "bot_data.db"


def load_config() -> Config:
    bot_token = os.getenv("BOT_TOKEN", "")
    anthropic_api_key = os.getenv("ANTHROPIC_API_KEY", "")

    if not bot_token:
        raise ValueError("BOT_TOKEN не задан в .env")
    if not anthropic_api_key:
        raise ValueError("ANTHROPIC_API_KEY не задан в .env")

    return Config(
        bot_token=bot_token,
        anthropic_api_key=anthropic_api_key,
    )
