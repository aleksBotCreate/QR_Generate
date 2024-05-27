import os

from aiogram import Router, types, filters, F
from aiogram.enums import ContentType
from aiogram.fsm.context import FSMContext

from data.callbacks import ColorData
from keyboards import inline
from utils.qr import create_code

user_router = Router()


@user_router.message(filters.CommandStart())
async def command_start(event: types.Message, state: FSMContext):
    data = await state.get_data()
    await delete_reply(event, data)
    await state.clear()

    text = '👋 Привет посетитель. Ты попал в бот по генерации <b>QR кодов</b>.\n\n' \
           '📑 Просто <b>пришли мне текст</b>, который хочешь спрятать в QR код и я пришлю его тебе.\n\n' \
           'Разработка telegram ботов: @aleksBotCreate_channel'
    await event.answer(text=text)


@user_router.message(F.content_type == ContentType.TEXT)
async def create_qr_code(event: types.Message, state: FSMContext):
    data = await state.get_data()
    await delete_reply(event, data)
    await state.clear()

    path = create_code(event.html_text, '#000000')
    photo = types.FSInputFile(path)
    caption = '✅ Твой QR код создан.\n' \
              '🎨 Ты можешь изменить свой код, выбери цвет на ниже!\n\n' \
              'Нужен еще один? Скорее присылай текст для qr кода.'
    kb = inline.get_color_code()
    msg = await event.answer_photo(photo=photo, caption=caption, reply_markup=kb)

    await state.set_data({'data': event.html_text, 'msg_id': msg.message_id})

    os.remove(path)


@user_router.message()
async def qr_error(event: types.Message, state: FSMContext):
    data = await state.get_data()
    await delete_reply(event, data)
    await state.clear()

    text = '❌ Упс... Я не могу создать QR код. Помните, вы должны прислать текст, повторите ввод.'
    await event.answer(text=text)


@user_router.callback_query(ColorData.filter())
async def get_color_code(event: types.CallbackQuery, callback_data: ColorData, state: FSMContext):
    data = await state.get_data()
    await delete_reply(event, data)
    await state.clear()

    path = create_code(data['data'], callback_data.color)
    photo = types.FSInputFile(path)
    caption = '✅ Твой QR код создан.\n' \
              '🎨 Ты можешь изменить свой код, выбери цвет на ниже!\n\n' \
              'Нужен еще один? Скорее присылай текст для qr кода.'
    kb = inline.get_color_code()
    msg = await event.message.answer_photo(photo=photo, caption=caption, reply_markup=kb)

    await state.set_data({'data': data['data'], 'msg_id': msg.message_id})

    os.remove(path)


async def delete_reply(event, data):
    try:
        await event.bot.edit_message_reply_markup(chat_id=event.from_user.id, message_id=data['msg_id'])
    except:
        pass

    return
