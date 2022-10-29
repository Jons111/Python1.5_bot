from aiogram import types
from aiogram.types import ContentType

from loader import dp


# Echo bot
@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()
    await message.answer(text="Dakument qabul qilindi")

@dp.message_handler(content_types=ContentType.VIDEO)
async def bot_echo(message: types.Message):
    await message.video.download()
    await message.answer(text="Video qabul qilindi")

@dp.message_handler(content_types=ContentType.PHOTO)
async def bot_echo(message: types.Message):
    await message.photo[1].download()
    await message.answer(text="rasm qabul qilindi")