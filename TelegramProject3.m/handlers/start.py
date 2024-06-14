from aiogram import Router, types, F
from aiogram.filters.command import Command


start_router = Router()


@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    # print("Message", message)
    # print("User info", message.from_user)
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text = "Наш сайт",url = "https://geeks.kg"),
                types.InlineKeyboardButton(text="О нас", callback_data="about")
            ],
            [
                types.InlineKeyboardButton(text = "Мы в инстаграмме !", url = "https://instagram.com/geeks.kg")
            ],
            [
                types.InlineKeyboardButton(text = "Пожертвования для нас !", callback_data = "donate")
            ],
            [
                 types.InlineKeyboardButton(text="Menu", callback_data="dishes")
            ],
            [
                types.InlineKeyboardButton(text="Отзывы!", callback_data="feedback")
            ]
        ]
    )


    name = message.from_user.first_name
    surname = message.from_user.first_name
    await message.answer(
        f"Привет, {name}" + " {surname}",
        reply_markup=kb
    )


@start_router.callback_query(F.data == "about")
async def about_handler(callback:types.CallbackQuery):
    await callback.answer()# для того чтобы бот не завивасал.
    await callback.message.answer("О нас")


@start_router.callback_query(F.data == "donate")
async def about_handler(callback:types.CallbackQuery):
    await callback.answer()# для того чтобы бот не завивасал.
    await callback.message.answer("Мы будем очень благодарны за вашу поддержку.")


@start_router.callback_query(F.data == "dishes")
async def about_handler(callback:types.CallbackQuery):
    await callback.answer()# для того чтобы бот не завивасал.
    await callback.message.answer("Плов \nОромо \nМанты \nШашлыки \nПицца.")


@start_router.callback_query(F.data == "feedback")
async def about_handler(callback:types.CallbackQuery):
    await callback.answer()# для того чтобы бот не завивасал.
    await callback.message.answer("Нами все довольны )))!!!.")