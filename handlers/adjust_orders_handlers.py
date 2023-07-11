from aiogram import types, Dispatcher
from keyboards import main_kb, change_status_kb, inline_change_kb
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from ozon import get_data, write_delivered, write_delivering, write_last_mile, write_sended_by_seller
from config import client_id, api_key

class Form(StatesGroup):
    status = State()




# @dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer('Приветствую, сдесь ты можешь управлять своими заказами', reply_markup=main_kb)

# @dp.message_handler(commands=['watch_orders'])
async def watch_orders(message: types.Message):
    lst_data = get_data(client_id, api_key)
    articul = lst_data[0]
    date_begin = lst_data[1]
    date_end = lst_data[2]
    quantity = lst_data[3]
    price = lst_data[4]
    address = lst_data[5]
    address_client = lst_data[6]
    phone_client = lst_data[7]
    comment_client = lst_data[8]
    comment_taxi = lst_data[9]
    delivery_status = lst_data[10]
    posting_number = lst_data[11]
    await message.answer(
f"""Артикул: {articul}
Дата отправления-доставки: {date_begin}-{date_end}
Количество: {quantity}
Цена: {price}
Адресс: {address}
Адресс клиента: {address_client}
Телефон клиента: {phone_client}
Комментарий клиента {comment_client}
Комментарий для водителя: {comment_taxi}
статус статус: {delivery_status}
Номер поставки: {posting_number}""", reply_markup=inline_change_kb)
    
# @dp.callback_query_handler(func=lambda c: c.data == 'change')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await callback_query.message.answer('Выберите статус доставки', reply_markup=change_status_kb)
    await Form.status.set()

async def process_status(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['status'] = message.text
        status = data['status']

    await message.answer(f" {status}")
    if status == 'Доставляется':
        write_delivering(client_id, api_key)
    elif status == 'Последняя миля':
        write_last_mile(client_id, api_key)
    elif status == 'Доставлено':
        write_delivered(client_id, api_key)
    elif status == 'Отправлено продавцом':
        write_sended_by_seller(client_id, api_key)
    await state.finish()


def register_handlers_adjust(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=["start", "help"])
    dp.register_message_handler(watch_orders, commands=["watch_orders"])
    dp.register_callback_query_handler(process_callback_button1, lambda c: c.data == 'change')
    dp.register_message_handler(process_status, state=Form.status)
