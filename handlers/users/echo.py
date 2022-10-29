from aiogram import types

from loader import dp,bot,base

from filters.shaxsiy_uchun import Shaxsiy





@dp.message_handler(Shaxsiy(),state=None)
async def bot_echo(message: types.Message):
   ism = message.from_user.first_name
   matn = message.text
   tg_id = message.from_user.id
   base.add_murojaat(ism=ism,matn=matn,tg_id=tg_id)
   await message.answer(text=message.text)