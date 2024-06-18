from aiogram import Router, F, types
from aiogram.filters.command import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from config import database

feedback_router = Router()

class FeedBack(StatesGroup):
    name = State() # Имя пользователя
    age = State() # Возраст пользователя
    phone_number = State()  # Номер телефона
    instagram = State()  # Соц сеть Интсаграмм пользователя
    rating = State()  # Оценка
    commentary = State()  # Комментарий


@feedback_router.message(Command("feedback"))
async def start_feedback(message: types.Message, state: FSMContext):
    #Устанавливаем состояние
    await state.set_state(FeedBack.name)
    await message.answer("Как вас зовут ?")


@feedback_router.message(Command("stop"))
@feedback_router.message(F.text =="стоп")
async def stop_feedback(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Опрос остановлен.")


@feedback_router.message(FeedBack.name)
async def process_name(message: types.Message, state: FSMContext):
    print("Message:",message.text)
    #Сохраняем данные пользователя
    await state.update_data(name = message.text)

    #Устанавливаем состояние
    await state.set_state(FeedBack.age)
    await message.answer("Сколько вам лет?")


@feedback_router.message(FeedBack.age)
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("Пожалуйста введите только цифры !")
        return
    age = int(age)
    if age <10 or age > 90:
        await message.answer("Введите возраст от 10 до 90 !")
        return

    # Сохраняем данные пользователя
    await state.update_data(age = message.text)

    # Устанавливаем состояние
    await state.set_state(FeedBack.phone_number)
    await message.answer("Поделитесь вашим номером телефона ?")

@feedback_router.message(FeedBack.phone_number)
async def process_phone_number(message: types.Message, state: FSMContext):
    # Сохраняем данные пользователя
    await state.update_data(phone_number = message.text)

    # Устанавливаем состояние
    await state.set_state(FeedBack.instagram)
    await message.answer("Поделитесь вашим адресом в Инстаграме: ")


@feedback_router.message(FeedBack.instagram)
async def process_instagram(message: types.Message, state: FSMContext):
    await state.update_data(instagram = message.text)
    # Устанавливаем зависимость
    await message.set_state(FeedBack.commentary)
    await message.answer("Обязательно оставьте свой комментарий! Они будут учтены. ")


@feedback_router.message(FeedBack.commentary)
async def process_commentary(message: types.Message, state: FSMContext):
    await state.update_data(commentary = message.text)
    #Устанавливаем состояние
    await message.set_state(FeedBack.rating)
    await message.answer("Пожалуйста оцените наше заведение от 1 до 5. Спасибо !")


@feedback_router.message(FeedBack.rating)
async def process_rating(message: types.Message, state: FSMContext):
    rating = message.text


    if not rating.isdigit():
        await message.answer("Пожалуйста введите только цифры !")
        return

    rating = int(rating)

    if rating <= 2:
        print(f'Мы поняли что ваша оценка {rating}. Спасибо за вашу оценку ! Будем больше стараться (-_-)')
    elif rating <= 4:
        print(f'Мы поняли что ваша оценка {rating}. Спасибо за вашу оценку ! Мы стараемся ради вас !')
    elif rating >= 5:
        print(f'Мы поняли что ваша оценка {rating}. Спасибо за вашу оценку ! Мы очень рады что вы довольны нами !')
    else:
        print('Oops! You entered an invalid command! ')


    await state.update_data(rating = rating)

    data = await state.get_data()
    print("Data", data)

    await database.execute("""
        INSERT INTO survey_results (name, age, phone_number, instagram, commentary, rating)
        VALUES (?, ?, ?, ?, ?, ?)""",
        data['name'], data['age'], data['phone_number'], data['instagram'], data['rating'], data['commentary']
    )
    await state.clear()
    await message.answer("Спасибо за прохождение опроса?")
    #Устанавливаем состояние
    # await message.answer("Вы можете оставить вашу оценку от 1 до 5 ")