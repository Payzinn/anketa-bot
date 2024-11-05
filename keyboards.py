from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Функция для создания клавиатуры с вопросом о возрасте
def age_keyboard():
    buttons = [
        [InlineKeyboardButton(text='Да', callback_data='age_yes')],  # Кнопка "Да"
        [InlineKeyboardButton(text='Нет', callback_data='age_no')]   # Кнопка "Нет"
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)  # Формируем клавиатуру
    return keyboard

# Функция для создания клавиатуры с выбором города
def city_keyboard():
    buttons = [
        [InlineKeyboardButton(text='Москва', callback_data='city_moscow')],          # Кнопка для Москвы
        [InlineKeyboardButton(text='Санкт-Петербург', callback_data='city_spb')],   # Кнопка для Санкт-Петербурга
        [InlineKeyboardButton(text='Новосибирск', callback_data='city_nsk')],       # Кнопка для Новосибирска
        [InlineKeyboardButton(text='Чебоксары', callback_data='city_cheb')],        # Кнопка для Чебоксар
        [InlineKeyboardButton(text='Краснодар', callback_data='city_krasnodar')]    # Кнопка для Краснодара
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)  # Формируем клавиатуру
    return keyboard
