from aiogram.dispatcher.filters.builtin import Command


class CommandMovie(Command):
    def __init__(self):
        super().__init__(['movie'])
