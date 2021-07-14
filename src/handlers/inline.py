from aiogram import types

from src.settings import BASE_URL
from src.similar_movie import Client


async def choose_movie(query: types.InlineQuery):
    if not query.query:
        return

    client = Client()
    movies = client.get_movies_by_name(query.query)
    results = [
        types.InlineQueryResultArticle(
            id=movie['id'],
            title=movie['title'],
            url=f'{BASE_URL}{movie["url"]}',
            thumb_url=f'{BASE_URL}{movie["thumb"]}',
            input_message_content=types.InputTextMessageContent(
                message_text=f'{BASE_URL}{movie["url"]}',
                disable_web_page_preview=True,
            ),
            hide_url=True,
        ) for movie in movies
    ]
    await query.answer(results=results)


async def get_similar_movies(query: types.ChosenInlineResult):
    client = Client()
    similar_movies = client.get_similar_movies(query.result_id)
    