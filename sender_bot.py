from aiogram import executor
from create_bot import dp
from handlers import adjust_orders_handlers
from handlers import send_orders_handlers

if __name__ == '__main__':
    send_orders_handlers.register_handlers_send(dp)
    adjust_orders_handlers.register_handlers_adjust(dp)
    executor.start_polling(dp, skip_updates=True)
    