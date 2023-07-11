from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import bot_api

storage = MemoryStorage()
bot = Bot(token=bot_api)
dp = Dispatcher(bot, storage=storage)