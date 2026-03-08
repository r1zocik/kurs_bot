from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
import aiohttp

from keyboards.currency_buttons import input_currency_buttons, output_currency_buttons
from handlers.register import RegisterState

router = Router()


async def get_rate(code: str):
    url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()

    for item in data:
        if item["Ccy"] == code:
            return float(item["Rate"])
    return None


@router.message(RegisterState.amount)
async def amount_msg(message: types.Message, state: FSMContext):
    if not message.text.replace(".", "", 1).isdigit():
        return await message.answer("Faqat son kiriting!")

    await state.update_data(amount=float(message.text))
    await message.answer("Siz yuborga valyutani tanlang:", reply_markup=input_currency_buttons())



@router.callback_query(F.data.startswith("in_"))
async def input_currency(call: types.CallbackQuery, state: FSMContext):
    currency = call.data.replace("in_", "")
    await state.update_data(input_currency=currency)

    await call.message.answer("Endi, qaysi valyutaga o'tkazmoqchisiz:", reply_markup=output_currency_buttons())
    await call.answer()


@router.callback_query(F.data.startswith("out_"))
async def convert(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    amount = data["amount"]
    input_currency = data["input_currency"]
    output_currency = call.data.replace("out_", "")

  
    usd = await get_rate("USD")
    rub = await get_rate("RUB")

    
    if input_currency == "uzs":
        uzs = amount
    elif input_currency == "usd":
        uzs = amount * usd
    elif input_currency == "rub":
        uzs = amount * rub
    else:
        return await call.message.answer("Ошибка валюты.")

    
    if output_currency == "uzs":
        result = uzs
    elif output_currency == "usd":
        result = uzs / usd
    elif output_currency == "rub":
        result = uzs / rub
    else:
        return await call.message.answer("Ошибка валюты.")

    await call.message.answer(
        f"💱 Конвертация:\n"
        f"{amount} {input_currency.upper()} → {round(result, 2)} {output_currency.upper()}"
    )

    await call.answer()
