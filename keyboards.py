from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

button_show_orders = KeyboardButton('/watch_orders')
main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.add(button_show_orders)

inline_button_change = InlineKeyboardButton('Поменять статус отправки', callback_data='change')
inline_button_send = InlineKeyboardButton('Отправить заказ', callback_data='send')
inline_change_kb = InlineKeyboardMarkup().add(inline_button_change).add(inline_button_send)

button_yes = KeyboardButton('y')
button_no = KeyboardButton('n')
confirm_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
confirm_keyboard.add(button_yes)
confirm_keyboard.add(button_no)

button_sending = KeyboardButton('Доставляется')
button_last_mile = KeyboardButton('Последняя миля')
button_sended = KeyboardButton('Доставлено')
button_sended_by_seller = KeyboardButton('Отправлено продавцом')
change_status_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
change_status_kb.add(button_sending)
change_status_kb.add(button_last_mile)
change_status_kb.add(button_sended)
change_status_kb.add(button_sended_by_seller)

taxi_class_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button_express = KeyboardButton('Экспресс')
button_courier = KeyboardButton('Курьер')
button_long_express = KeyboardButton('Доставка за 4 часа')
taxi_class_kb.add(button_express, button_courier, button_long_express)