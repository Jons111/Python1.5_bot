from aiogram import types
from aiogram.types import InputFile
import requests
from loader import dp,bot


# Echo bot
@dp.message_handler(text='Osh')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/malikovdev/183'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu rasm")

    rasm_manzili = 'https://t.me/malikovdev/183'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption="Bu rasm")

    rasm_manzili = 'https://t.me/malikovdev/183'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption="Bu rasm")


