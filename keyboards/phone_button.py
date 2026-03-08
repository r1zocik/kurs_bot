from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def phone_button():
    kb = [[KeyboardButton(text="📱 Отправить номер", request_contact=True)]]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)


def region():
    kb=[
        [
            KeyboardButton(text="🇺🇿 O'zbekiston"),
            KeyboardButton(text="🇷🇺 Rossiya"),
            KeyboardButton(text="🇺🇸 Amerika Qo'shma Shtatlari"),
        ]
    ]