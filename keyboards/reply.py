from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🖥️ List"),
            KeyboardButton(text="🛒 Total")
        ],
        [
            KeyboardButton(text="🚑 Help"), KeyboardButton(text="🗑️ Reset")
        ]
    ],
    resize_keyboard=True
)
