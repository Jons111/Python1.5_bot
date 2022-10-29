from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp,bot
from states.holatlar import Murojaat
from keyboards.default.menu import tasdiqlash_button,menu_button
# Echo bot
@dp.message_handler(text="Adminga murojaat")
async def bot_echo(message: types.Message):
    await message.answer(text="Adminga habar jo'natish uchun ismingizni kiriting")
    await Murojaat.ism_holati.set()

@dp.message_handler(state=Murojaat.ism_holati)
async def bot_echo(message: types.Message,state:FSMContext):

    ism = message.text
    await state.update_data({"name":ism})
    await message.answer(text="Familyani kiriting")
    await Murojaat.fam_holati.set()


@dp.message_handler(state=Murojaat.fam_holati)
async def bot_echo(message: types.Message, state: FSMContext):
    familya= message.text
    await state.update_data({"fam": familya})
    await message.answer(text="Yoshni kiriting")
    await Murojaat.yosh_holati.set()


@dp.message_handler(state=Murojaat.yosh_holati)
async def bot_echo(message: types.Message, state: FSMContext):
    yosh = message.text
    await state.update_data({"age": yosh})
    await message.answer(text="Telni kiriting")
    await Murojaat.tel_holati.set()

@dp.message_handler(state=Murojaat.tel_holati)
async def bot_echo(message: types.Message, state: FSMContext):
    tel = message.text
    await state.update_data({"nomer": tel})
    await message.answer(text="Murojaatni kiriting")
    await Murojaat.maqsad_holati.set()

@dp.message_handler(state=Murojaat.maqsad_holati)
async def bot_echo(message: types.Message, state: FSMContext):
    matn = message.text
    user_id = message.from_user.id
    await state.update_data({"text": matn})

    malumot = await state.get_data()
    ismi = malumot.get('name')
    fami = malumot.get('fam')
    yoshi = malumot.get('age')
    teli = malumot.get('nomer')
    matni = malumot.get('text')

    ekranga_chiqarish = f"Ism :{ismi}\n" \
                        f"Familya :{fami}\n" \
                        f"Yosh :{yoshi}\n" \
                        f"Tel :{teli}\n" \
                        f"Murojaat :{matni}\n"

    await bot.send_message(chat_id=user_id,text=ekranga_chiqarish,reply_markup=tasdiqlash_button)
    await Murojaat.tasdiqlash_holati.set()

@dp.message_handler(state=Murojaat.tasdiqlash_holati,text="Tasdiqlash")
async def bot_echo(message: types.Message, state: FSMContext):
    matn = message.text
    user_id = message.from_user.id
    malumot = await state.get_data()
    ismi = malumot.get('name')
    fami = malumot.get('fam')
    yoshi = malumot.get('age')
    teli = malumot.get('nomer')
    matni = malumot.get('text')

    ekranga_chiqarish = f"Ushbu faoyalanuvchi xabar yubordi{ismi}\n" \
                        f"Ism :{ismi}\n" \
                        f"Familya :{fami}\n" \
                        f"Yosh :{yoshi}\n" \
                        f"Tel :{teli}\n" \
                        f"Murojaat :{matni}\n"

    await bot.send_message(chat_id="1892438581",text=ekranga_chiqarish)
    await bot.send_message(chat_id=user_id,text="Adminga yuborildi",reply_markup=menu_button)
    await state.finish()
@dp.message_handler(state=Murojaat.tasdiqlash_holati,text="Bekor qilish")
async def bot_echo(message: types.Message, state: FSMContext):
    matn = message.text
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id,text="Bekor qilindi",reply_markup=menu_button)
    await state.finish()