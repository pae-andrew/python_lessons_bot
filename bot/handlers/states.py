from aiogram.fsm.state import State, StatesGroup


class TestStates(StatesGroup):
    in_progress = State()


class TaskStates(StatesGroup):
    waiting_code = State()
