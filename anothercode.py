# import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.webhook import configure_app
from aiohttp import web

# Токен Telegram-бота
API_TOKEN = '123456:Abcdefghijk'

# Настройка логирования
# logging.basicConfig(level=logging.INFO)

# Бот и диспетчер бота
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Создаём объект веб-сервера
app = web.Application()


# Обработка входящих запросов от стороннего API
async def api_handler(request):
    return web.json_response({"status": "ok", "message": "hello from api handler"}, status=200)


# Хэндлер на любое сообщение боту
@dp.message_handler(content_types=types.ContentType.ANY)
async def echo(message: types.Message):
    await message.reply("I'm bot and I see your message!")


async def on_startup():
    # Установка telegram-вебхука и подключение бота к aiohttp
    await bot.set_webhook("http://127.0.0.1:9900/bot")
    configure_app(dp, app, "/bot")
    # Установка роутинга для приёма входящих от сторонних клиентов
    app.add_routes([web.get('/api', api_handler)])


async def on_shutdown():
    await bot.close()


if __name__ == '__main__':
    # Предстартовая подготовка (вызов on_startup())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(on_startup())
    app.on_shutdown.append(on_shutdown)

    # Запуск
    web.run_app(app, port=9900, access_log=None)