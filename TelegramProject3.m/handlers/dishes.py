from aiogram import Router, types, F
from aiogram.filters.command import Command

from handlers import start_router


@start_router.callback_query(F.data == "menu")
async def about_handler(callback:types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Плов \nОромо \nМанты \nШашлыки \nПицца")