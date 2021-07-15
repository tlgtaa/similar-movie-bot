from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode

from src.settings import ADMINS, API_TOKEN


async def on_startup(dp: Dispatcher):
    from src import handlers, middlewares, db
    from src.utils import on_startup_notify

    dp.bot.db = db.get_manager()
    middlewares.setup(dp)
    handlers.setup(dp)
    await on_startup_notify(dp, ADMINS)


if __name__ == '__main__':
    bot = Bot(API_TOKEN, parse_mode=ParseMode.HTML)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    executor.start_polling(dp, on_startup=on_startup)
