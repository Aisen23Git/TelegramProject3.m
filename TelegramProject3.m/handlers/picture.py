from aiogram import Router, types
from aiogram.filters.command import Command
from config import bot, media
import os
import random
from aiogram.types import FSInputFile



picture_router = Router()


@picture_router.message(Command("picture"))
async def picture_handler(message: types.Message):
    files = os.listdir(media)
    random1 = random.choice(files)
    print(media + random1)
    photo=FSInputFile(random1)
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=photo,
        caption ="images"
    )