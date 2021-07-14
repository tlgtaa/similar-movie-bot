from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart, CommandHelp

from .commands import CommandMovie
from .help import bot_help
from .inline import choose_movie, get_similar_movies
from .movie import get_movies_by_name
from .start import bot_start


def setup(dp: Dispatcher):
    dp.register_message_handler(bot_start, CommandStart())
    dp.register_message_handler(bot_help, CommandHelp())
    dp.register_message_handler(get_movies_by_name, CommandMovie())
    dp.register_inline_handler(choose_movie)
    dp.register_chosen_inline_handler(get_similar_movies)
