from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def input_currency_buttons():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🇺🇿 Сум", callback_data="in_uzs")],
        [InlineKeyboardButton(text="🇺🇸 Доллар", callback_data="in_usd")],
        [InlineKeyboardButton(text="🇷🇺 Рубль", callback_data="in_rub")],
    ])

def output_currency_buttons():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🇺🇿 Сум", callback_data="out_uzs")],
        [InlineKeyboardButton(text="🇺🇸 Доллар", callback_data="out_usd")],
        [InlineKeyboardButton(text="🇷🇺 Рубль", callback_data="out_rub")],
    ])
