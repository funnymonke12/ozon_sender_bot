# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from geopy.geocoders import Nominatim
# from aiogram import Dispatcher
# from aiogram import types
# from create_bot import bot
# from call_taxi import call_taxi
# from ozon import get_data
# from config import client_id, api_key
#
# class Form(StatesGroup):
#     data = State()
#     confirm = State()
#
# async def process_data(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['address'] = message.text.split(' / ')[0]
#         if not isNumeric(data["address"].split(', ')[0]):
#             data['lat'] = get_coords(data['address'])[0]
#             data['long'] = get_coords(data['address'])[1]
#         else:
#             data['lat'] = data['address'].split(', ')[0]
#             data['long'] = data['address'].split(', ')[1]
#         data['company_name'] = message.text.split(' / ')[1]
#         data['order_id'] = message.text.split(' / ')[2]
#         data['client_phone'] = message.text.split(' / ')[3].strip()
#         data['data'] = get_clients_data(card_id)
#         data['quantity'] = get_clients_data(card_id)["quantity"]
#         data['product_name'] = get_clients_data(card_id)["product_name"]
#         data['client_lat'] = get_clients_coords(card_id)[0]
#         data['client_long'] = get_clients_coords(card_id)[1]
#         data['client_fulladdress'] = get_clients_data(card_id)['second_address']
#         fulladdress = get_address(data['lat'], data['long'])
#         data['fulladdress'] = fulladdress
#         data['description'] = f"Магазин {data['company_name']}. Забрать заказ {data['order_id']}. Если у вас возникают вопрос по доставке, напишите Вотсапе +79055935860\n Для 2 точки: Отдавать БЕЗ чека! Это подарок! Звони получателю {data['client_phone']}"
#     print(message.text)
#     print(f'Адрес отправителя: {data["fulladdress"]}')
#     print(f"Адрес клиента: {data['client_fulladdress']}")
#     await bot.send_location(message.chat.id, data['lat'], data['long'])
#     await message.answer(
# f"""ТОВАР: {data['data']['product_name']}\n
# {data['data']['delivery_date_begin']} - {data['data']['delivery_date_end']}'\n
# АДРЕС 1: {data['address']}\n
# {data['description']}\n
# АДРЕС 2: {data['data']['second_address']}
# """, reply_markup=confirm_keyboard)
#
#     await FormSend.next()
#     await message.reply("Вы подтверждаете отправку? Y/N")
#
# # state=FormSend.confirm
# async def process_confirm(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['confirm_send'] = message.text.lower()
#     if data['confirm_send'] == 'n':
#         await message.answer('Отменяю отправку')
#         await state.finish()
#         return
#     await message.answer('Вызываю экспресс доставку, Подождите немного идёт отправка.')
#     print('Отправка подтверждена вызываю такси')
#     call_taxi(data['description'], data['long'], data['lat'], data['client_long'], data['client_lat'], data['client_phone'], data['fulladdress'], data['client_fulladdress'], data['quantity'], data['product_name'])
#     await state.finish()
#
#
# def register_handlers_send(dp: Dispatcher):
#     dp.register_message_handler(process_data, state=)

