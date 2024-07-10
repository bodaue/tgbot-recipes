from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def start_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Рецепты")]], resize_keyboard=True
    )
    return keyboard
