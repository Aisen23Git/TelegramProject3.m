from aiogram import Router, F, types
from aiogram.filters.command import Command


order_router = Router()


@order_router.message(Command("menu"))
async def show_menu(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Шашлыки")
            ],
            [
                types.KeyboardButton(text="Плов"),
                types.KeyboardButton(text="Манты")
            ],
            [
                types.KeyboardButton(text="Чай"),
                types.KeyboardButton(text="Компот"),
                types.KeyboardButton(text="Кымыз"),
                types.KeyboardButton(text="Бозо")

            ]
        ],
        resize_keyboard=True
    )
    await message.answer("Выберите блюдо которое вы хотите ниже: ", reply_markup=kb)


@order_router.message(F.text == "Шашлыки")
async def show_shashliki(message: types.Message):
    print(message.text)
    kb = types.ReplyKeyboardRemove()
    await message.answer("У нас есть шашлыки ! Сейчас принесут, прошу подождите.", reply_markup = kb)


@order_router.message(F.text == "Манты")
async def show_manty(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("У нас есть Манты ! Сейчас принесут, прошу подождите.", reply_markup = kb)


@order_router.message(F.text == "Плов")
async def show_plov(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("У нас есть Пловы ! Сейчас принесут, прошу подождите.", reply_markup = kb)


@order_router.message(F.text == "Чай")
async def show_chai(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("У нас есть чай ! Сейчас принесут, прошу подождите.", reply_markup = kb)


@order_router.message(F.text == "Компот")
async def show_kompot(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("У нас есть компоты ! Сейчас принесут, прошу подождите.", reply_markup=kb)


@order_router.message(F.text == "Кымыз")
async def show_kymyz(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("У нас есть кымыз(саамал) ! Сейчас принесут, прошу подождите.", reply_markup = kb)


@order_router.message(F.text == "Бозо")
async def show_bozo(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("У нас есть бозошки ! Сейчас принесут, прошу подождите.", reply_markup=kb)