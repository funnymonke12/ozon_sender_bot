from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from geopy.geocoders import Nominatim
from aiogram import Dispatcher
from aiogram import types
from create_bot import bot



class Form(StatesGroup):
    position = State()
    message_to_order = State()
    confirm = State()


schema = 'Магазин ___. Забрать заказ ___. Если у вас возникают вопрос по доставке, напишите Вотсапе +79055935860'

# @dp.message_handler(commands=["send_loc"])
async def send_loc(message: types.Message):
    await Form.position.set()
    await message.reply("Введи адрес или координаты через пробел.")

# @dp.message_handler(state=Form.position)
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

# @dp.message_handler(state=Form.message_to_order)
async def process_descr(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['message_to_order'] = f"Магазин {message.text.split()[0]}. Забрать заказ {message.text.split()[1]}. Если у вас возникают вопрос по доставке, напишите Вотсапе +79055935860 "

    await message.answer(data['message_to_order'])
    await Form.next()
    await message.answer('Вы подтверждаете отправку? Y/N')

# @dp.message_handler(state=Form.confirm)
async def process_confirm(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['confirm'] = message.text
    schema = 'Отдавать БЕЗ чека! Это подарок!' # Номер получателя
    if data['confirm'].lower() == 'y':
        await message.answer('Вызываем такси')
    elif data["confirm"].lower == 'n':
        await message.answer('Отправка отменена')

    await state.finish()

def register_handlers_send(dp: Dispatcher):
    dp.register_message_handler(send_loc, commands=["send_loc"])
    dp.register_message_handler(process_position, state=Form.position)
    dp.register_message_handler(process_descr, state=Form.message_to_order)
    dp.register_message_handler(process_confirm, state=Form.confirm)
