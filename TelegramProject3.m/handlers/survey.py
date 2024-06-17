from aiogram import Router, F, types
from aiogram.filters.command import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from config import database

survey_router = Router()


#FSM - Finite State Mashine - Конечный автомат
class FoodSurvey(StatesGroup):


    name = State()  # Имя пользователя
    age = State()  # Сколько лет пользователю
    gender = State()  # Пол
    favorite_food = State()  # Любимая еда


@survey_router.message(Command("opros"))
async def start_survey(message: types.Message, state: FSMContext):
    #Устанавливаем состояние
    await message.set_state(FoodSurvey.name)
    await message.answer("Как вас зовут ?")


@survey_router.message(Command("stop"))
@survey_router.message(F.text =="стоп")
async def stop_survey(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Опрос остановлен.")


@survey_router.message(FoodSurvey.name)
async def process_name(message: types.Message, state: FSMContext):
    print("Message:",message.text)
    #Сохраняем данные пользователя
    await state.update_data(name = message.text)

    #Устанавливаем состояние
    await state.set_state(FoodSurvey.age)
    await message.answer("Сколько вам лет?")


@survey_router.message(FoodSurvey.age)
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
    await state.set_state(FoodSurvey.gender)
    await message.answer("Какого вы пола?")


@survey_router.message(FoodSurvey.gender)
async def process_gender(message: types.Message, state: FSMContext):
    # Сохраняем данные пользователя
    await state.update_data(gender = message.text)

    # Устанавливаем состояние
    await state.set_state(FoodSurvey.favorite_food)
    await message.answer("Какое ваше любимое блюдо?")


@survey_router.message(FoodSurvey.favorite_food)
async def process_favorite_food(message: types.Message, state: FSMContext):
    # Сохраняем данные пользователя
    await state.update_data(favorite_food = message.text)

    # Берем сохраненные данные
    data = await state.get_data()
    print("Data", data)
    # Save to DB
    await database.execute("""
        INSERT INTO survey_results (name, age, gender, favorite_food)
        VALUES (?, ?, ?, ?)""",
        data['name'], data['age'], data['gender'], data['favorite_food']
    )
    # Чистим данные
    await state.clear()
    await message.answer("Спасибо за прохождение опроса?")