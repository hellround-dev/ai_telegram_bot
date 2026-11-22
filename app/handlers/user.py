from aiogram import Router, types
from aiogram.filters import CommandStart

router = Router()


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я готов к работе.")


@router.message()
async def echo_message(message: types.Message):
    await message.answer(f"Ты написал: {message.text}")