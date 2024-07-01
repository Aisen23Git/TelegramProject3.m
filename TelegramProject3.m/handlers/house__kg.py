from aiogram import Router, F, types
from aiogram.filters.command import Command
from crawler.house_kg import get_page, get_links
from config import bot
house_router = Router()


@house_router.callback_query(lambda call:call.data =='crawler')
async def show_obyavlenie(message: types.Message):
    page=get_page()
    links=get_links(page)
    for i in links:
        await bot.send_message(
            chat_id=message.from_user.id,
            text=i,
        )
