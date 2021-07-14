from aiogram import types


async def bot_help(msg: types.Message):
    text = [
        'Список команд: ',
        '/start - Начать диалог',
        '/help - Получить справку',
        '/movie <strong>Название фильма</strong> - Получить похожие фильмы по названию фильма'
    ]
    await msg.answer('\n'.join(text))
