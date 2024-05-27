from aiogram.utils.keyboard import InlineKeyboardBuilder

from data.callbacks import ColorData


def get_color_code():
    builder = InlineKeyboardBuilder()

    builder.button(text='Красный', callback_data=ColorData(color='#ff0000'))
    builder.button(text='Жёлтый', callback_data=ColorData(color='#ffff00'))
    builder.button(text='Зелёный', callback_data=ColorData(color='#008000'))
    builder.button(text='Синий', callback_data=ColorData(color='#0000ff'))
    builder.button(text='Малиновый', callback_data=ColorData(color='#dc143c'))
    builder.button(text='Розовый', callback_data=ColorData(color='#ff1493'))

    return builder.adjust(3).as_markup()
