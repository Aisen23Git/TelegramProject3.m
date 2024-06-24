import asyncio
import logging
from aiogram import types

from config import dp, bot, database
# from aiogram.filters.command import Command
# from aiogram import Router, types
#
from handlers import (
    start_router,
    order_router,
    feedback_router,
    picture_router,
    echo_router,
    survey_router
)


async def on_startup(bot):
    await database.create_table()




# @dp.message(Command("myinfo"))
# async def info_handler(message: types.Message):
#     await bot.send_message(
#         chat_id=message.from_user.id,
#         text=f'id : {message.from_user.id}\n'
#              f'name : {message.from_user.first_name}\n'
#     )


async def main():
    await bot.set_my_commands([
        types.BotCommand(command = "start", description = "Начало"),
        types.BotCommand(command = "menu", description = "Наши блюда"),
        types.BotCommand(command = "feedback", description = "Отзывы клиентов"),
        types.BotCommand(command = "picture", description = "Отправка картинок"),
    ])
    # Регистрируем роутер
    dp.include_router(picture_router)
    dp.include_router(start_router)
    dp.include_router(feedback_router)
    dp.include_router(order_router)
    dp.include_router(survey_router)

    # в самом конце
    dp.include_router(echo_router)
    # запускаем бот
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())