import asyncio

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import bot_api

loop = asyncio.get_event_loop()
storage = MemoryStorage()
bot = Bot(token=bot_api, loop=loop, parse_mode='html')
dp = Dispatcher(bot, storage=storage)