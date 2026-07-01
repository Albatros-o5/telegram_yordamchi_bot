from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


support_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Support Account",
                url="tg://user?id=6954414989"
            )
        ]
    ]
)
