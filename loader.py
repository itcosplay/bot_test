from aiogram import Bot
from aiogram import Dispatcher
from aiogram.types import ParseMode

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)

dp = Dispatcher(bot)