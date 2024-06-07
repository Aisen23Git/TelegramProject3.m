from aiogram import Router, types
from aiogram.filters.command import Command


start_router = Router()


@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    print("Message", message)
    print("User info", message.from_user)

    name = message.from_user.first_name
    surname = message.from_user.first_name
    await message.answer(
        f"Привет, {name}" + " {surname}"
    )