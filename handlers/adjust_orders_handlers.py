from aiogram import types, Dispatcher
from keyboards import main_kb, change_status_kb, inline_change_kb
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from ozon import get_data, write_delivered, write_delivering, write_last_mile, write_sended_by_seller
from config import client_id, api_key

class Form_send(StatesGroup):
    send_data = State()
    confirm = State()
class Form_status(StatesGroup):
    status = State()

# @dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer('Приветствую, здесь ты можешь управлять своими заказами', reply_markup=main_kb)

# @dp.message_handler(commands=['watch_orders'])
async def watch_orders(message: types.Message):
    lst_data = get_data(client_id, api_key)
    if not lst_data:
        await message.answer('В вашем личном кабинете нет заказов')
        return
    for key in lst_data.keys():
        print(key)
        # data = lst_data[key]['data']
        product_id = lst_data[key]['product_id']
        date_begin = lst_data[key]['delivery_date_begin']
        date_end = lst_data[key]['delivery_date_end']
        quantity = lst_data[key]['quantity']
        price = lst_data[key]['price']
        f_addres = lst_data[key]['first_addres']
        s_addres = lst_data[key]['second_addres']
        phone = lst_data[key]['client_phone']
        comment = lst_data[key]['comment']
        dr_comment = '...'
        del_status = lst_data[key]['delivery_status']
        posting_number = lst_data[key]['posting_number']
        card_id = lst_data[key]['card_id']
        await message.answer(
f"""Артикул: {product_id}
Дата отправления-доставки: {date_begin}-{date_end}
Количество: {quantity}
Цена: {price}
Адресс: {f_addres}
Адресс клиента: {s_addres}
Телефон клиента: {phone}
Комментарий клиента {comment}
Комментарий для водителя: {dr_comment}
статус статус: {del_status}
Номер поставки: {posting_number}
Айди карточки в боте: {card_id}""", reply_markup=inline_change_kb)

# @dp.callback_query_handler(lambda c: c.data == 'send')
async def process_callback_button2(callback_query: types.CallbackQuery):
    global post_number
    post_number = callback_query.message.text.split('\n')[-1].split(': ')[-1]
    await callback_query.message.answer('Выберите статус доставки', reply_markup=change_status_kb)
    await Form_status.status.set()
post_number = None
# @dp.callback_query_handler(lambda c: c.data == 'change')
async def process_callback_button1(callback_query: types.CallbackQuery):
    global post_number
    post_number = callback_query.message.text.split('\n')[-1].split(': ')[-1]
    await callback_query.message.answer('Выберите статус доставки', reply_markup=change_status_kb)
    await Form_status.status.set()

async def process_status(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['status'] = message.text
        status = data['status']

    await message.answer(f"Статус отправки поменян на: {status}")
    if status == 'Доставляется':
        write_delivering(client_id, api_key, post_number)
    elif status == 'Последняя миля':
        write_last_mile(client_id, api_key, post_number)
    elif status == 'Доставлено':
        write_delivered(client_id, api_key, post_number)
    elif status == 'Отправлено продавцом':
        write_sended_by_seller(client_id, api_key, post_number)
    await state.finish()


def register_handlers_adjust(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=["start", "help"])
    dp.register_message_handler(watch_orders, commands=["watch_orders"])
    dp.register_callback_query_handler(process_callback_button1, lambda c: c.data == 'change')
    dp.register_callback_query_handler(process_callback_button2, lambda c: c.data == 'send')
    dp.register_message_handler(process_status, state=Form_status.status)
