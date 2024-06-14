from config import dp, bot
from aiogram.filters.command import Command
from aiogram import Router, types

@dp.message(Command("myinfo"))
async def info_handler(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f'id : {message.from_user.id}\n'
             f'name : {message.from_user.first_name}\n'
    )