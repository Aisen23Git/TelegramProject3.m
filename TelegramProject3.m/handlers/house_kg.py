from aiogram import Router, F, types
from aiogram.filters.command import Command
# from crawler.house_kg import get_page, get_links


house_router = Router()


@house_router.message(Command("obyavlenie"))
async def show_obyavlenie(message: types.Message):
    await message.answer("Тут будут объявления")
