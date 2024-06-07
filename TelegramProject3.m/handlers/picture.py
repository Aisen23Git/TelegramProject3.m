from aiogram import Router, types
from aiogram.filters.command import Command


picture_router = Router()


@picture_router.message(Command("picture"))
async def picture_handler(message: types.Message):
    files = os.listdir('C:/Users/Admin/PycharmProjects/TelegramProject3.m/images')
    random1 = random.choice(files)
    photo=FSInputFile(random1)
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=photo,
    )