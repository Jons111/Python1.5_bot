from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

son = 5
print(son)
print(5)

tillar_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="O'zbek tili",callback_data='til1'),
            InlineKeyboardButton(text="Rus tili",callback_data='til2')
        ],
        [
            InlineKeyboardButton(text="Ingliz tili",callback_data='til3')
        ],
        [
            InlineKeyboardButton(text="Hamkorlarimiz",url="https://t.me/UstozShogird"),
            InlineKeyboardButton(text="Ulashish",switch_inline_query="Zo'r bot ekan foydalaninglar")
        ]
    ]
)