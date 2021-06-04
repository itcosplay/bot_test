import logging

from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook


API_TOKEN = 'BOT_TOKEN_HERE'

# webhook settings
WEBHOOK_HOST = 'localhost'
WEBHOOK_PATH = ''
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = 'localhost'  # or ip
WEBAPP_PORT = 5000


# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)
# dp.middleware.setup(LoggingMiddleware())


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    # executor.start_polling(dp)

    start_webhook (
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        # on_startup=on_startup,
        # on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )