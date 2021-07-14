from aiogram import types

from src.utils import rate_limit


@rate_limit(limit=3)
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}')
