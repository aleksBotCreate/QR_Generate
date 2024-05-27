from aiogram.filters.callback_data import CallbackData


class ColorData(CallbackData, prefix='ColorData'):
    color: str
