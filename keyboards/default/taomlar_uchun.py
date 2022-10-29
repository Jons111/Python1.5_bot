from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

taomlar_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Osh"),
            KeyboardButton(text="Somsa"),
            KeyboardButton(text="Sho'rva")
        ],
        [
            KeyboardButton(text="Kabob"),
            KeyboardButton(text="Gril")
        ]
    ],
    resize_keyboard=True
)