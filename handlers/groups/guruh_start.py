from aiogram import types
from aiogram.types import ContentTypes

from loader import dp,bot
from filters.guruh_uchun import Guruh

# Echo bot
@dp.message_handler(Guruh(),text='salom')
async def bot_echo(message: types.Message):
    ism = message.from_user.full_name
    chat_id = message.chat.id
    user_id=message.from_user.id
    await bot.restrict_chat_member(chat_id=chat_id,user_id=user_id,until_date='1:2:00',can_send_messages=False)

@dp.message_handler(Guruh(),commands ='start')
async def bot_echo(message: types.Message):
    await message.reply(text="Guruh orqali start yubordiz")

royxat=['salom','hello','qalesan','bye']
@dp.message_handler(Guruh(),text=[i for i in royxat])
async def bot_echo(message: types.Message):
    await message.reply(text="Va alaykum assalom")

@dp.message_handler(Guruh(),content_types=ContentTypes.ANY)
async def bot_echo(message: types.Message):

    kim_qoshyapti = message
    print(kim_qoshyapti,'-----------------')
    chat_id = message.chat.id

    mes_id = message.message_id
    await message.answer(text=f"Guruhga hush kelibsiz ")

@dp.message_handler(Guruh(),content_types=ContentTypes.LEFT_CHAT_MEMBER)
async def bot_echo(message: types.Message):
    ism = message.left_chat_member.full_name
    kim_qoshyapti = message
    print(kim_qoshyapti,'-----------------')
    chat_id = message.chat.id

    mes_id = message.message_id
    await bot.delete_message(chat_id=chat_id,message_id=mes_id)
    await message.answer(text=f"Guruhga hush kelibsiz {ism}")
