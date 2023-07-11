from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_show_orders = KeyboardButton('/Просмотреть заказы')
main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.add(button_show_orders)