import asyncio
import logging
from datetime import datetime, timezone

from supabase import Client, create_client

logger = logging.getLogger(__name__)

_client: Client | None = None


def get_client() -> Client:
    if _client is None:
        raise RuntimeError("База данных не инициализирована. Вызови init_db().")
    return _client


async def init_db(url: str, key: str) -> None:
    global _client
    try:
        _client = create_client(url, key)
        logger.info("Supabase клиент инициализирован")
    except Exception as e:
        logger.error("Ошибка инициализации Supabase: %s", e)
        raise


# ---------------------------------------------------------------------------
# Users
# ---------------------------------------------------------------------------

async def get_or_create_user(user_id: int, username: str | None) -> dict:
    try:
        client = get_client()

        def _run():
            res = client.table("users").select("*").eq("user_id", user_id).execute()
            if res.data:
                return res.data[0]
            now = datetime.now(timezone.utc).isoformat()
            insert_res = client.table("users").insert({
                "user_id": user_id,
                "username": username,
                "current_module": 1,
                "current_lesson": 1,
                "total_score": 0,
                "created_at": now,
            }).execute()
            return insert_res.data[0]

        return await asyncio.to_thread(_run)
    except Exception as e:
        logger.error("Ошибка get_or_create_user для %s: %s", user_id, e)
        raise


async def get_user(user_id: int) -> dict | None:
    try:
        client = get_client()

        def _run():
            res = client.table("users").select("*").eq("user_id", user_id).execute()
            return res.data[0] if res.data else None

        return await asyncio.to_thread(_run)
    except Exception as e:
        logger.error("Ошибка get_user для %s: %s", user_id, e)
        raise


async def add_score(user_id: int, points: int) -> None:
    try:
        client = get_client()
        user = await get_user(user_id)
        if not user:
            return
        new_score = user["total_score"] + points

        def _run():
            client.table("users").update({"total_score": new_score}).eq("user_id", user_id).execute()

        await asyncio.to_thread(_run)
    except Exception as e:
        logger.error("Ошибка add_score для %s: %s", user_id, e)
        raise


# ---------------------------------------------------------------------------
# Progress
# ---------------------------------------------------------------------------

async def get_lesson_progress(user_id: int, module_id: int, lesson_id: int) -> dict | None:
    try:
        client = get_client()

        def _run():
            res = (
                client.table("progress")
                .select("*")
                .eq("user_id", user_id)
                .eq("module_id", module_id)
                .eq("lesson_id", lesson_id)
                .execute()
            )
            return res.data[0] if res.data else None

        return await asyncio.to_thread(_run)
    except Exception as e:
        logger.error("Ошибка get_lesson_progress: %s", e)
        raise


async def upsert_lesson_progress(
    user_id: int,
    module_id: int,
    lesson_id: int,
    *,
    test_passed: bool | None = None,
    task_passed: bool | None = None,
    score_delta: int = 0,
) -> None:
    try:
        client = get_client()
        existing = await get_lesson_progress(user_id, module_id, lesson_id)

        def _run():
            if existing:
                updates: dict = {}
                if test_passed is not None:
                    updates["test_passed"] = test_passed
                if task_passed is not None:
                    updates["task_passed"] = task_passed
                if score_delta:
                    updates["score"] = existing["score"] + score_delta
                if updates:
                    client.table("progress").update(updates).eq(
                        "user_id", user_id
                    ).eq("module_id", module_id).eq("lesson_id", lesson_id).execute()
            else:
                client.table("progress").insert({
                    "user_id": user_id,
                    "module_id": module_id,
                    "lesson_id": lesson_id,
                    "test_passed": test_passed if test_passed is not None else False,
                    "task_passed": task_passed if task_passed is not None else False,
                    "score": score_delta,
                }).execute()

        await asyncio.to_thread(_run)
    except Exception as e:
        logger.error("Ошибка upsert_lesson_progress: %s", e)
        raise


async def mark_lesson_completed(user_id: int, module_id: int, lesson_id: int) -> None:
    try:
        client = get_client()
        now = datetime.now(timezone.utc).isoformat()

        def _run():
            client.table("progress").update({"completed_at": now}).eq(
                "user_id", user_id
            ).eq("module_id", module_id).eq("lesson_id", lesson_id).execute()

        await asyncio.to_thread(_run)
    except Exception as e:
        logger.error("Ошибка mark_lesson_completed: %s", e)
        raise


async def advance_lesson(user_id: int) -> dict | None:
    from content.curriculum import get_next_lesson
    try:
        user = await get_user(user_id)
        if not user:
            return None

        next_pos = get_next_lesson(user["current_module"], user["current_lesson"])
        if not next_pos:
            return user

        next_module, next_lesson = next_pos
        client = get_client()

        def _run():
            client.table("users").update({
                "current_module": next_module,
                "current_lesson": next_lesson,
            }).eq("user_id", user_id).execute()

        await asyncio.to_thread(_run)
        return await get_user(user_id)
    except Exception as e:
        logger.error("Ошибка advance_lesson для %s: %s", user_id, e)
        raise


async def get_user_stats(user_id: int) -> dict:
    try:
        user = await get_user(user_id)
        if not user:
            return {}

        client = get_client()

        def _run():
            res = (
                client.table("progress")
                .select("*")
                .eq("user_id", user_id)
                .order("module_id")
                .order("lesson_id")
                .execute()
            )
            return res.data

        rows = await asyncio.to_thread(_run)
        completed = [r for r in rows if r["test_passed"] and r["task_passed"]]

        return {
            "user": user,
            "progress_rows": rows,
            "completed_count": len(completed),
            "total_lesson_score": sum(r["score"] for r in rows),
        }
    except Exception as e:
        logger.error("Ошибка get_user_stats для %s: %s", user_id, e)
        raise