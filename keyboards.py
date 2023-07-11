from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

button_show_orders = KeyboardButton('/watch_orders')
main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.add(button_show_orders)

inline_button_change = InlineKeyboardButton('Поменять статус отправки', callback_data='change')
inline_keyboard_change = InlineKeyboardMarkup().add(inline_button_change)

button_sending = KeyboardButton('Доставляется')
button_last_mile = KeyboardButton('Последняя миля')
button_sended = KeyboardButton('Доставлено')
button_sended_by_seller = KeyboardButton('Отправлено продавцом')
change_status_kb = ReplyKeyboardMarkup(resize_keyboard=True)
change_status_kb.add(button_sending)
change_status_kb.add(button_last_mile)
change_status_kb.add(button_sended)
change_status_kb.add(button_sended_by_seller)