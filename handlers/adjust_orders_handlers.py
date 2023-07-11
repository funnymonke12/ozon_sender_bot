from aiogram import types, Dispatcher
from keyboards import main_kb, change_status_kb
from ozon import get_data
from config import client_id, api_key




# @dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer('Приветствую, сдесь ты можешь управлять своими заказами', reply_markup=main_kb)

# @dp.message_handler(commands=['watch_orders'])
async def watch_orders(message: types.Message):
    lst_data = get_data(client_id, api_key)
    articul = lst_data[0]
    date = lst_data[1]
    quantity = lst_data[2]
    price = lst_data[3]
    address = lst_data[4]
    address_client = lst_data[5]
    phone_client = lst_data[6]
    comment_client = lst_data[7]
    comment_taxi = lst_data[8]
    await message.answer(
f"""Артикул: {articul}
Дата отправления-доставки: {date}
Количество: {quantity}
Цена: {price}
Адресс: {address}
Адресс клиента: {address_client}
Телефон клиента: {phone_client}
Комментарий клиента {comment_client}
Комментарий для водителя: {comment_taxi}
статус статус: """)
    
# @dp.callback_query_handler(func=lambda c: c.data == 'change')
# async def process_callback_button1(callback_query: types.CallbackQuery):
#     await callback_query.message.answer('Выберите статус доставки', reply_markup=change_status_kb)    


def register_handlers_adjust(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=["start", "help"])
    dp.register_message_handler(watch_orders, commands=["watch_orders"])
    # dp.register_callback_query_handler(process_callback_button1, function=lambda c: c.data == 'change')
