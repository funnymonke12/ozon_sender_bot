from aiogram import types, Dispatcher
from geopy import Nominatim

from keyboards import main_kb, change_status_kb, inline_change_kb
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from ozon import get_data, write_delivered, write_delivering, write_last_mile, write_sended_by_seller, get_clients_data
from ozon import get_clients_coords
from config import client_id, api_key

class FormSend(StatesGroup):
    data = State()
    confirm = State()
class FormStatus(StatesGroup):
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
        product_name = lst_data[key]['product_name']
        product_id = lst_data[key]['product_id']
        date_begin = lst_data[key]['delivery_date_begin']
        date_end = lst_data[key]['delivery_date_end']
        quantity = lst_data[key]['quantity']
        price = lst_data[key]['price']
        s_addres = lst_data[key]['second_address']
        phone = lst_data[key]['client_phone']
        comment = lst_data[key]['comment']
        del_status = lst_data[key]['delivery_status']
        posting_number = lst_data[key]['posting_number']
        card_id = lst_data[key]['card_id']
        await message.answer(
f"""Название товара: {product_name}
Артикул: {product_id}
Дата отправления-доставки: {date_begin}-{date_end}
Количество: {quantity}
Цена: {price}
Адресс клиента: {s_addres}
Комментарий клиента: {comment}
статус: {del_status}
Номер поставки: {posting_number}
Айди карточки: {card_id}""", reply_markup=inline_change_kb)

card_id = None
# @dp.callback_query_handler(lambda c: c.data == 'send')
async def process_callback_button2(callback_query: types.CallbackQuery):
    global card_id
    card_id = callback_query.message.text.split('\n')[-1].split(': ')[-1]
    print(card_id)
    await FormSend.data.set()
    print('Запускаем отправку')
    await callback_query.message.reply('Введите данные как в примере: адрес_1 или (ширина, высота) / Название_компании / номер_заказа / номер_клиента')

async def process_data(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['address'] = message.text.split(' / ')[0]
        data['company_name'] = message.text.split(' / ')[1]
        data['order_id'] = message.text.split(' / ')[2]
        data['client_phone'] = message.text.split(' / ')[3]
        data['data'] = get_clients_data(card_id)

        if data['address'].split()[0].isdigit():
            data['long'] = float(data['address'].split()[0])
            data['lat'] = float(data['address'].split()[1])
        else:
            geolocator = Nominatim(user_agent="Tester")
            location = geolocator.geocode(data['address'])
            print(location)
            print(location.latitude, location.longitude)
            data['long'] = location.latitude
            data['lat'] = location.longitude

        data['description'] = f"Магазин {data['company_name']}. Забрать заказ {data['order_id']}. Если у вас возникают вопрос по доставке, напишите Вотсапе +79055935860\nОтдавать БЕЗ чека! Это подарок! Звони получателю {data['client_phone']}"

    print(data['long'], data['lat'])
    await message.answer_location(data['lat'], data['long'])
    await message.answer(
f"""ТОВАР: {data['data']['product_name']}\n
{data['data']['delivery_date_begin']} - {data['data']['delivery_date_end']}'\n
АДРЕС 1: {data['address']}\n
{data['description']}\n
АДРЕС 2: {data['data']['second_address']}
""")

    await FormSend.next()
    await message.reply("Вы подтверждаете отправку? Y/N")

# state=FormSend.confirm
async def process_confirm(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['confirm_send'] = message.text.lower()
    print('Подтвердили отправку')
    if data['confirm_send'] == 'n':
        await message.answer('Отменяю отправку')
        return
    await message.answer('Вызываю экспресс доставку')
    await state.finish()




post_number = None
# @dp.callback_query_handler(lambda c: c.data == 'change')
async def process_callback_button1(callback_query: types.CallbackQuery):
    global post_number
    post_number = callback_query.message.text.split('\n')[-1].split(': ')[-1]
    await callback_query.message.answer('Выберите статус доставки', reply_markup=change_status_kb)
    await FormStatus.status.set()

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
    dp.register_message_handler(process_data, state=FormSend.data)
    dp.register_message_handler(process_confirm, state=FormSend.confirm)
    dp.register_message_handler(process_status, state=FormStatus.status)
