from ozon import get_data
from config import bot_api, api_key, client_id
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from geopy.geocoders import Nominatim
from keyboards import main_kb


storage = MemoryStorage()
bot = Bot(token=bot_api)
dp = Dispatcher(bot, storage=storage)

class Form(StatesGroup):
    position = State()
    message_to_order = State()
    confirm = State()

schema = 'Магазин ___. Забрать заказ ___. Если у вас возникают вопрос по доставке, напишите Вотсапе +79055935860'

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer('Приветствую, сдесь ты можешь управлять своими заказами', reply_markup=main_kb)
#     await message.answer(
# f"""Артикул: {articul}
# Дата отправления-доставки: {date}
# Количество: {quantity}
# Цена: {price}
# Адресс: {address}
# Адресс клиента: {address_client}
# Телефон клиента: {phone_client}
# Комментарий клиента {comment_client}
# Комментарий для водителя: {comment_taxi}""", reply_markup=main_kb, )

@dp.message_handler(commands=['watch_orders'])
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
Комментарий для водителя: {comment_taxi}""")
    

@dp.message_handler(commands=["send_loc"])
async def send_loc(message: types.Message):
    await Form.position.set()
    await message.reply("Введи адрес или координаты через пробел.")
@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    pass


@dp.message_handler(state=Form.position)
async def process_position(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['position'] = message.text

    if data['position'].split()[0].isdigit():
        long = float(data['position'].split()[0])
        lat = float(data['position'].split()[1])
    else:
        geolocator = Nominatim(user_agent="Tester")
        location = geolocator.geocode(data['position'])
        print(location)
        print(location.latitude, location.longitude)
        long = location.latitude
        lat = location.longitude
    print(data['position'])

    await bot.send_location(message.chat.id, long, lat)
    await Form.next()
    await message.answer(f'Впишите слова вместо пропусков в {schema} через пробел')

@dp.message_handler(state=Form.message_to_order)
async def process_descr(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['message_to_order'] = f"Магазин {message.text.split()[0]}. Забрать заказ {message.text.split()[1]}. Если у вас возникают вопрос по доставке, напишите Вотсапе +79055935860 "

    await message.answer(data['message_to_order'])
    await Form.next()
    await message.answer('Вы подтверждаете отправку? Y/N')

@dp.message_handler(state=Form.confirm)
async def process_confirm(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['confirm'] = message.text
    schema = 'Отдавать БЕЗ чека! Это подарок!' # Номер получателя
    if data['confirm'].lower() == 'y':
        await message.answer('Вызываем такси')
    elif data["confirm"].lower == 'n':
        await message.answer('Отправка отменена')

    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)