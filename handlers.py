from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart, StateFilter
from aiogram.filters.state import State, StatesGroup
from keyboards import city_keyboard, age_keyboard

# Определяем состояния для формы
class Form(StatesGroup):
    age = State()
    city = State()

# Словарь с городами и их каналами
CITY_DATA = {
    'city_moscow': {
        'name': 'Москва',
        'channel': 'https://t.me/+nNMIULfPucc2MGUy'
    },
    'city_spb': {
        'name': 'Санкт-Петербург',
        'channel': 'https://t.me/+-bHakOhjRd1lOTAy'
    },
    'city_nsk': {
        'name': 'Новосибирск',
        'channel': 'https://t.me/+_Kj4ii1JVt44MDNi'
    },
    'city_cheb': {
        'name': 'Чебоксары',
        'channel': 'https://t.me/+LmlCT-iO8k9lMjUy'
    },
    'city_krasnodar': {
        'name': 'Краснодар',
        'channel': 'https://t.me/+UD1m1d1TehgyNzRi'
    }
}

# Создаем роутер
router = Router()

# Обработчик команды старта
@router.message(CommandStart())
async def start_handler(message: types.Message, state: FSMContext):
    await state.clear()  # Очищаем состояние
    await message.answer('Вам есть 18 лет?', reply_markup=age_keyboard())
    await state.set_state(Form.age)  # Устанавливаем состояние для возраста

# Обработчик для возраста
@router.callback_query(StateFilter(Form.age))
async def process_age(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.edit_reply_markup(reply_markup=None)
    
    if callback.data == 'age_yes':
        await callback.message.answer("С какого вы города?", reply_markup=city_keyboard())
        await state.set_state(Form.city)  # Переход к состоянию выбора города
    elif callback.data == 'age_no':
        await callback.message.answer('Доступ запрещен.')
        await state.clear()  # Очищаем состояние
        return

# Обработчик для выбора города
@router.callback_query(StateFilter(Form.city))
async def process_city(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.edit_reply_markup(reply_markup=None)
    
    city_data = CITY_DATA.get(callback.data)  # Получаем данные о городе
    if city_data:
        await callback.message.answer(
            f'Ссылка на канал города {city_data["name"]}: {city_data["channel"]}'
        )
    else:
        await callback.message.answer('Выберите город из списка.')
    
    await state.clear()  # Очищаем состояние
