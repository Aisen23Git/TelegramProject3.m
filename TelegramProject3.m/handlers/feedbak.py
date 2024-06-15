from aiogram import Router, F, types
from aiogram.filters.command import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


survey_router = Router()

class FeedBack(StatesGroup):


    name = State() # Имя пользователя
    phone_number = State()  # Номер телефона
    instagram = State()  # Соц сеть Интсаграмм пользователя
    estimation = State()  # Оценка
    commentary= State()  # Комментарий


@survey_router.message(Command("feedback"))
async def start_survey(message: types.Message, state: FSMContext):
    await state.update_data(name = message.text)
    #Устанавливаем состояние
    await message.set_state(FeedBack.name)
    await message.answer("Как вас зовут ?")

@survey_router.message(FeedBack.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name = message.text)
    # Устанавливаем состояние
    await message.set_state(FeedBack.phone_number)
    await message.answer("Введите пожалуйста ваш номер телефона: ")



@survey_router.message(FeedBack.phone_number)
async def process_phone_number(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("Введите пожалуйста только цифры !")
        return

    await state.update_data(phone_number=message.text)
    # Устанавливаем состояние
    await message.set_state(FeedBack.instagram)
    await message.answer("Какой ваш номер телефона")


@survey_router.message(FeedBack.instagram)
async def process_instagram(message: types.Message, state: FSMContext):
    await state.update_data(instagram = message.text)
    # Устанавливаем зависимость
    await message.set_state(FeedBack.commentary)
    await message.answer("Поделитесь вашим адресом в Инстаграме: ")


@survey_router.message(FeedBack.commentary)
async def process_commentary(message: types.Message, state: FSMContext):
    await state.update_data(commentary = message.text)
    #Устанавливаем состояние
    await message.set_state(FeedBack.estimation)
    await message.answer("Обязательно оставьте свой комментарий! Они будут учтены.")


@survey_router.message(FeedBack.estimation)
async def process_instagram(message: types.Message, state: FSMContext):
    estimation = message.text
    estimation = int(estimation)
    if estimation <= 2:
        print(f'Мы поняли что ваша оценка {estimation}. Спасибо за вашу оценку ! Будем больше стараться (-_-)')
    elif estimation <= 4:
        print(f'Мы поняли что ваша оценка {estimation}. Спасибо за вашу оценку ! Мы стараемся ради вас !)
    elif estimation = 5:
        print(f'Мы поняли что ваша оценка {estimation}. Спасибо за вашу оценку ! Мы очень рады что вы довольны нами !)
    else:
        print('Oops! You entered an invalid command! ')

    await state.update_data(estimate = message.text)
    #Устанавливаем состояние
    await message.set_state(FeedBack.commentary)
    await message.answer("Вы можете оставить вашу оценку от 1 до 5 ")
