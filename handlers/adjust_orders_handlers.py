from datetime import datetime
from aiogram import types, Dispatcher
from keyboards import main_kb, change_status_kb, inline_change_kb, confirm_keyboard, taxi_class_kb
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from ozon import get_data, write_delivered, write_delivering, write_last_mile, write_sended_by_seller, get_clients_data
from ozon import get_clients_coords
from call_express import call_express, get_express_price
from call_during_day import get_during_day_price, call_during_day
from create_bot import bot, loop
from geocoder import get_address, get_coords, define_coords


class FormSend(StatesGroup):
    data = State()
    taxi_class = State()
    confirm = State()

class FormStatus(StatesGroup):
    status = State()

# @dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer('Приветствую, здесь ты можешь управлять своими заказами', reply_markup=main_kb)
async def helloworld():
    pass

s_addres = ''
async def watch_orders(message: types.Message):
    global s_addres
    lst_data = get_data()

    if not lst_data:
        await message.answer('В вашем личном кабинете нет заказов')
        return
    for key in lst_data.keys():
        # data = lst_data[key]['data']
        product_name = lst_data[key]['product_name']
        product_id = lst_data[key]['product_id']
        date_begin = lst_data[key]['delivery_date_begin']
        date_end = lst_data[key]['delivery_date_end']
        quantity = lst_data[key]['quantity']
        price = lst_data[key]['price']
        s_addres = lst_data[key]['second_address']
        comment = lst_data[key]['comment']
        del_status = lst_data[key]['delivery_status']
        posting_number = lst_data[key]['posting_number']
        card_id = lst_data[key]['card_id']
        shop = lst_data[key]['shop']
        await message.answer(
f"""Название товара: {product_name}
Дата отправления-доставки: {date_begin}   -   {date_end}
Количество: {quantity}
Цена: {price}
Адресс клиента: {s_addres}
Комментарий клиента: {comment}
<b>СТАТУС: {del_status}</b>
Магазин: {shop}
Айди карточки: {card_id}""", reply_markup=inline_change_kb, parse_mode="html")

card_id = None
# @dp.callback_query_handler(lambda c: c.data == 'send')
async def process_callback_button2(callback_query: types.CallbackQuery):
    global card_id
    card_id = callback_query.message.text.split('\n')[-1].split(': ')[-1]
    await FormSend.data.set()
    await callback_query.message.reply('Введите данные как в примере:\nадрес_1 / Название_компании / номер_заказа / номер_клиента\nили\nадрес_1 / адрес_2 / название_компании / номер_заказа / номер_клиента')

def set_data(data, state):
    coords = define_coords(data['address'])
    data['lat'] = coords[0]
    data['long'] = coords[1]
    print(f"Вывожу координаты отправителя: {data['lat']}, {data['long']}")
    print(f"Вывожу координаты клиента: {data['client_lat']}, {data['client_long']}")
    data['data'] = get_clients_data(card_id)
    data['quantity'] = get_clients_data(card_id)["quantity"]
    data['product_name'] = get_clients_data(card_id)["product_name"]
    data['fulladdress'] = get_address(data['lat'], data['long'])
    data['client_comment'] = get_clients_data(card_id)['comment']
    data['fulladdress'] = get_address(data['lat'], data['long'])
    data['first_comment'] = f"Магазин {data['company_name']}. Забрать заказ {data['order_id']}. Убрать ценник с товара! Чек не забирать!  Если возникла проблема при отгрузке - напиши WhatsApp +79055935860"
    data['second_comment'] = f"""Отдавать БЕЗ чека! Это подарок! Звони получателю {data['client_phone']}. \n
Комментарий клиента: {data['client_comment']}"""
async def process_data(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            if len(message.text.split(' / ')) == 4:
                data['address'] = message.text.split(' / ')[0]
                data['company_name'] = message.text.split(' / ')[1]
                data['order_id'] = message.text.split(' / ')[2]
                data['client_phone'] = message.text.split(' / ')[3].strip()
                data['client_lat'] = get_clients_coords(card_id)[0]
                data['client_long'] = get_clients_coords(card_id)[1]
                data['client_fulladdress'] = get_clients_data(card_id)['second_address']
                set_data(data, state)
            elif len(message.text.split(' / ')) == 5:
                data['address'] = message.text.split(' / ')[0]
                data['client_address'] = message.text.split(' / ')[1]
                data['company_name'] = message.text.split(' / ')[2]
                data['order_id'] = message.text.split(' / ')[3]
                data['client_phone'] = message.text.split(' / ')[4].strip()
                client_coords = define_coords(data['client_address'])
                data['client_lat'] = client_coords[0]
                data['client_long'] = client_coords[1]
                data['client_fulladdress'] = get_address(data['client_lat'], data['client_long'])
                set_data(data, state)
            print(f'Адрес отправителя: {data["fulladdress"]}')
            print(f"Адрес клиента: {data['client_fulladdress']}")
            await bot.send_location(message.chat.id, data['lat'], data['long'])
            await bot.send_location(message.chat.id, data['client_lat'], data['client_long'])
            await message.answer(
        f"""ТОВАР: {data['data']['product_name']}\n
        Дата доставки: {data['data']['delivery_date_begin']} - {data['data']['delivery_date_end']}'\n
        АДРЕС 1: {data['fulladdress']}
        Комментарий: {data['first_comment']}\n
        АДРЕС 2: {data['client_fulladdress']}
        Комментарий: {data['second_comment']}
        """)
            express_price = get_express_price(data['long'], data['lat'], data['client_long'], data['client_lat'], data['fulladdress'], data['client_fulladdress'], 'express')
            courier_price = get_express_price(data['long'], data['lat'], data['client_long'], data['client_lat'],data['fulladdress'], data['client_fulladdress'], 'courier')
            during_day_price = get_during_day_price(data['long'], data['lat'], data['client_long'], data['client_lat'],data['fulladdress'], data['client_fulladdress'], 'express')
            await message.reply(
            f"Выберите тип доставки.\nКурьер - {courier_price}\nЭкспресс обычный - {express_price}\nДоставка за 4 часа - {during_day_price}\n\nЧтобы запланировать доставку введите:\nЗапланировать доставку дата время\nПример: Запланировать доставку 2023-07-23 15:00",
            reply_markup=taxi_class_kb)
            await FormSend.next()
        except:
            await message.answer('Не удаётся оценить расстояние. Отправка отменена.')
            await state.finish()

async def process_taxi_class(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['taxi_class'] = message.text
    await message.answer('Вы подтверждаете отправку? Y/N', reply_markup=confirm_keyboard)
    await FormSend.next()

async def process_confirm(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['confirm_send'] = message.text.lower()
    if data['confirm_send'] == 'n':
        await message.answer('Отменяю отправку')
        await state.finish()
        return

    try:
        if data['confirm_send'] == 'y' and data['taxi_class'] == 'Экспресс':
            call_express(data['first_comment'], data['second_comment'], data['long'], data['lat'], data['client_long'], data['client_lat'], data['client_phone'], data['fulladdress'], data['client_fulladdress'], data['quantity'], data['product_name'], 'express')
            await message.answer('Вызываю экспресс доставку, Подождите немного идёт отправка.')
        elif data['confirm_send'] == 'y' and data['taxi_class'] == 'Курьер':
            call_express(data['first_comment'], data['second_comment'], data['long'], data['lat'], data['client_long'], data['client_lat'], data['client_phone'], data['fulladdress'], data['client_fulladdress'], data['quantity'], data['product_name'], 'courier')
            await message.answer('Вызываю доставку курьером, Подождите немного идёт отправка.')
        elif data['confirm_send'] == 'y' and data['taxi_class'] == 'Доставка за 4 часа':
            hour = datetime.now().hour
            date_start = datetime.now().strftime(f"%Y-%m-%dT{hour-4}:00:00Z")
            date_end = datetime.now().strftime(f"%Y-%m-%dT{hour-4+4}:00:00Z")
            call_during_day(data['first_comment'], data['second_comment'], data['long'], data['lat'], data['client_long'], data['client_lat'], data['client_phone'], data['fulladdress'], data['client_fulladdress'], data['quantity'], data['product_name'], date_start, date_end)
            await message.answer('Вызываю')
        elif data['confirm_send'] == 'y' and data['taxi_class'].lower().split()[0] == 'запланировать':
            date = data['taxi_class'].split()[2]
            time = int(data['taxi_class'].split()[3].split(':')[0])-3
            print(time)
            start_datetime = f"{date}T{str(time)}:00:00Z"
            end_datetime = f"{date}T{str(time+4)}:00:00Z"
            call_during_day(data['first_comment'], data['second_comment'], data['long'], data['lat'], data['client_long'], data['client_lat'], data['client_phone'], data['fulladdress'], data['client_fulladdress'], data['quantity'], data['product_name'], start_datetime, end_datetime)
            await message.answer('Запланировал доставку.')
    except:
        await message.answer('Не удаётся вызвать доставку. Попробуйте заново.')
        await state.finish()
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
        write_delivering(post_number)
    elif status == 'Последняя миля':
        write_last_mile(post_number)
    elif status == 'Доставлено':
        write_delivered(post_number)
    elif status == 'Отправлено продавцом':
        write_sended_by_seller(post_number)
    await state.finish()


def register_handlers_adjust(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=["start", "help"])
    dp.register_message_handler(watch_orders, commands=["watch_orders"])
    dp.register_callback_query_handler(process_callback_button1, lambda c: c.data == 'change')
    dp.register_callback_query_handler(process_callback_button2, lambda c: c.data == 'send')
    dp.register_message_handler(process_data, state=FormSend.data)
    dp.register_message_handler(process_taxi_class, state=FormSend.taxi_class)
    dp.register_message_handler(process_confirm, state=FormSend.confirm)
    dp.register_message_handler(process_status, state=FormStatus.status)
