from aiogram import types

from src.db import user_exists
from src.settings import BASE_URL
from src.similar_movie import Client


async def choose_movie(query: types.InlineQuery):
    if not query.query:
        return

    if db := query.bot.db:
        if await user_exists(db, query.from_user['id']):
            client = Client()
            movies = client.get_movies_by_name(query.query)
            results = [
                types.InlineQueryResultArticle(
                    id=movie['id'],
                    title=movie['title'],
                    url=f'{BASE_URL}{movie["url"]}',
                    thumb_url=f'{BASE_URL}{movie["thumb"]}',
                    input_message_content=types.InputTextMessageContent(
                        message_text=f'Ищу похожие фильмы на <strong>{movie["title"]}</strong>',
                        disable_web_page_preview=True,
                    ),
                    hide_url=True,
                ) for movie in movies
            ]
            await query.answer(results=results)
        else:
            await query.answer(
                results=[],
                switch_pm_text='Бот недоступен. Подключить бота.',
                switch_pm_parameter='connect_user',
            )
    else:
        await query.answer(
            results=[],
        )


async def get_similar_movies(query: types.ChosenInlineResult):
    client = Client()
    similar_movies = client.get_similar_movies(query.result_id)
    # @TODO подумать как отображать список фильмов?
    await query.bot.send_message(query.from_user.id, 'I have found')
