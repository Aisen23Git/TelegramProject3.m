import sqlite3

from aiogram import Router, F, types
from aiogram.filters.command import Command
from config import database

order_router = Router()


# @order_router.message(Command("menu"))
# async def show_menu(message: types.Message):
#     kb = types.ReplyKeyboardMarkup(
#         keyboard=[
#             [
#                 types.KeyboardButton(text="Шашлыки")
#             ],
#             [
#                 types.KeyboardButton(text="Плов"),
#                 types.KeyboardButton(text="Манты")
#             ],
#             [
#                 types.KeyboardButton(text="Чай"),
#                 types.KeyboardButton(text="Компот"),
#                 types.KeyboardButton(text="Кымыз"),
#                 types.KeyboardButton(text="Бозо")
#
#             ]
#         ],
#         resize_keyboard=True
#     )
#     await message.answer("Выберите блюдо которое вы хотите ниже: ", reply_markup=kb)


@order_router.message(Command("drinks"))
async def show_menu(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Чай"),
                types.KeyboardButton(text="Компот"),
                types.KeyboardButton(text="Кымыз"),
                types.KeyboardButton(text="Бозо"),
                types.KeyboardButton(text="Сок"),
                types.KeyboardButton(text="Пиво"),
                types.KeyboardButton(text="Кымыз"),
                types.KeyboardButton(text="Бозо")
            ]
        ],
        resize_keyboard=True
    )
    await message.answer("Выберите блюдо которое вы хотите ниже: ", reply_markup=kb)

@order_router.message(Command("food"))
async def show_menu(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Шашлыки"),
                types.KeyboardButton(text="Плов"),
                types.KeyboardButton(text="Манты")
            ],
            [
                types.KeyboardButton(text="Омлет"),
                types.KeyboardButton(text="Пицца"),
                types.KeyboardButton(text="Плов"),
                types.KeyboardButton(text="Манты")
            ]
        ],
        resize_keyboard=True
    )
    await message.answer("Выберите блюдо которое вы хотите ниже: ", reply_markup=kb)


@order_router.message(Command("dessert"))
async def show_menu(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Мороженое"),
                types.KeyboardButton(text="Торт"),
                types.KeyboardButton(text="Шоколад")
            ]
            # [
            #     types.KeyboardButton(text="Омлет"),
            #     types.KeyboardButton(text="Пицца"),
            #     types.KeyboardButton(text="Плов"),
            #     types.KeyboardButton(text="Манты")
            # ]
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

#===================================

dishes = ("шашлык","манты","плов ","чай","компот","кымыз","бозо","пицца пепперони с перцами чили и с сотрым кетчупом", "пиво живое")


@order_router.message(F.text.to_lower().in_(dishes))
async def show_dishes(message:types.Message):
    kb = types.ReplyKeyboardRemove()
    dishes = message.text.capitalize() # Одно из блюд
    foods = await database.fetch("""
        SELECT * FROM dishes JOIN dishes on food.dishes_id = dishes.id
        WHERE dishes.name = ? 
    """, (dishes,))
    await message.answer("Блюда на сегодня", reply_markup = kb)
    # await database.fetch("SELECT * FROM feedback_results")
    for food in dishes:
        await message.answer_photo(
            photo = food["image"],
            caption = f'{food['name']} - {food['price']} сом'
        )