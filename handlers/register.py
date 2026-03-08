from aiogram import Router, types, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from keyboards.phone_button import phone_button, region
from database import user_exists, add_user

router = Router()


class RegisterState(StatesGroup):
    name = State()
    phone = State()
    country = State()
    amount = State()


@router.message(F.text == "/start")
async def start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    if user_exists(user_id):  
        await state.set_state(RegisterState.amount)
        await message.answer("Summa kiriting:")
    else:
        await state.set_state(RegisterState.name)
        await message.answer("Ismingizni kiriting:")


@router.message(RegisterState.name)
async def reg_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(RegisterState.phone)
    await message.answer("Telefon raqamingizni yuboring:", reply_markup=phone_button())


@router.message(RegisterState.phone, F.contact)
async def reg_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.contact.phone_number)
    await state.set_state(RegisterState.country)
    await message.answer("Mamlakatingizni kiriting:", reply_markup=region())


@router.message(RegisterState.country)
async def reg_country(message: types.Message, state: FSMContext):
    data = await state.get_data()

    add_user(
        message.from_user.id,
        data["name"],
        data["phone"],
        message.text
    )

    await state.set_state(RegisterState.amount)
    await message.answer("Summa kiriting:")
