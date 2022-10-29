from aiogram.types import ReplyKeyboardMarkup , KeyboardButton
from loader import base

index = 0
keys = []
i = 0
menu = base.select_all_menu()
for taom in (menu):
    taom_nomi = taom[1]
    if i % 2 == 0 and i != 0:
            index += 1
    if i % 2 == 0:
            keys.append([KeyboardButton(text=f'{taom_nomi}')])
    else:
            keys[index].append(KeyboardButton(text=f'{taom_nomi}'))
    i += 1

menu_button = ReplyKeyboardMarkup(keys, resize_keyboard=True)


tasdiqlash_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tasdiqlash"),
            KeyboardButton(text="Bekor qilish")
        ],

    ],
    resize_keyboard=True
)