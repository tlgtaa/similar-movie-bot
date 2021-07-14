from typing import List

from aiogram import Dispatcher


async def on_startup_notify(dp: Dispatcher, users: List[str]):
    for user in users:
        await dp.bot.send_message(user, 'Бот запущен!')


def rate_limit(limit: int, key=None):
    """
    Decorator for configuring rate limit and key in different functions.
    :param limit:
    :param key:
    :return:
    """

    def decorator(func):
        setattr(func, 'throttling_rate_limit', limit)
        if key:
            setattr(func, 'throttling_key', key)
        return func

    return decorator
