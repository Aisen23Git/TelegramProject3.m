import asyncio
import logging

from config import dp, bot
from aiogram.filters.command import Command
from aiogram import Router, types
#
from handlers.echo import echo_router
from handlers.picture import picture_router
from handlers.start import start_router
#
import os
import random
from aiogram.types import FSInputFile


@dp.message(Command("myinfo"))
async def info_handler(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f'id : {message.from_user.id}\n'
             f'name : {message.from_user.first_name}\n'
    )


async def main():

    dp.include_router(picture_router)
    dp.include_router(start_router)
    # в самом конце
    dp.include_router(echo_router)
    # запускаем бот
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())