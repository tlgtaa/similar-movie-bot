from aiogram import types

from src.utils import rate_limit
from src.db import get_or_create_user


@rate_limit(limit=3)
async def bot_start(message: types.Message):
    if db := message.bot.db:
        kwargs = {
            'subscribed': True,
            'full_name': message.from_user.full_name,
            **message.from_user.values,
        }
        kwargs['chat_id'] = kwargs.pop('id')
        await get_or_create_user(db, **kwargs)

    await message.answer(f'Привет, {message.from_user.full_name}')
