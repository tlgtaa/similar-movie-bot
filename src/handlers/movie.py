from aiogram import types
from aiogram.types import InlineKeyboardButton

from src.keyboards import choice
from src.similar_movie import Client


async def get_movies_by_name(message: types.Message):
    movie = message.text
    client = Client()
    movies = client.get_movies_by_name(movie)
    size = len(movies)
    if size > 1:
        choice.insert(
            InlineKeyboardButton("Выбрать фильм", switch_inline_query_current_chat=movie)
        )
        await message.answer(
            f'По запросу <strong>{movie.capitalize()}</strong> найдено {size} результатов.',
            reply_markup=choice
        )
    elif size == 1:
        pass
        # await message.answer(movies)
    else:
        await message.answer(
            f'Похожий фильм не был найден или введите название фильма правильно {movie}'
        )
