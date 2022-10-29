from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, KeyboardButton, ReplyKeyboardMarkup
from data.config import kanallar
from keyboards.default.menu import menu_button
from keyboards.default.taomlar_uchun import taomlar_buttons
from loader import dp,base,bot
from keyboards.inline.tillar_uchun import tillar_buttons
from filters.shaxsiy_uchun import Shaxsiy

@dp.message_handler(Shaxsiy(),commands='start')
async def bot_start(message: types.Message):
    ism = message.from_user.first_name
    fam = message.from_user.last_name
    telegram_id = message.from_user.id
    try:
        base.user_qoshish(ism=ism,fam=fam,tg_id=telegram_id)
    except Exception as xatolik:
        print(xatolik)
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=tillar_buttons)


maxsulotlar= base.select_all_maxsulotlar()

@dp.message_handler(text=[i[1] for i in maxsulotlar])
async def bot_start(message: types.Message):
    nomi = message.text
    maxsulotlar = base.select_maxsulot(nomi=nomi)
    user_id = message.from_user.id
    for maxsulot in (maxsulotlar):
        max_nomi =maxsulot[1]
        max_narxi = maxsulot[2]
        max_rasm = maxsulot[3]
        await bot.send_photo(chat_id=user_id,photo=max_rasm,caption=f"Nomi : {max_nomi}\n"
                                                                    f"Narxi : {max_narxi}")


menu = base.select_all_menu()
@dp.message_handler(text=[i[1] for i in menu])
async def bot_start(message: types.Message):
    nomi = message.text
    maxsulotlar = base.select_maxsulot(tur=nomi)
    print(maxsulotlar)
    index = 0
    keys = []
    i = 0
    for taom in (maxsulotlar):
        taom_nomi = taom[1]
        if i % 2 == 0 and i != 0:
            index += 1
        if i % 2 == 0:
            keys.append([KeyboardButton(text=f'{taom_nomi}')])
        else:
            keys[index].append(KeyboardButton(text=f'{taom_nomi}'))
        i += 1
    keys.append([KeyboardButton(text=f'Ortga')])
    menu_button = ReplyKeyboardMarkup(keys, resize_keyboard=True)
    ism = message.from_user.first_name
    await message.answer(f"Assalomu alaykum botga hush kelibsiz taomlardan tanlang {ism}",reply_markup=menu_button)



@dp.callback_query_handler(text="til1")
async def bot_start(message: CallbackQuery):
    menu = base.select_all_menu()
    print(menu)
    await message.message.answer(text="O'zbek tili tanlandi",reply_markup=menu_button)





@dp.message_handler(Shaxsiy(),commands='reklama',chat_id='1892438581')
async def bot_start(message: types.Message):

    userlar = base.select_all_foydalanuvchilar()
    for user in kanallar:
        user_id = user
        await bot.send_message(chat_id=user_id,text="Bu reklama")


















