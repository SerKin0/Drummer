from aiogram.utils import executor
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from bot.filters import register_all_filters
from bot.misc import TgKeys
from bot.handlers import register_all_handlers


async def on_startup(dp: Dispatcher) -> None:
    register_all_filters(dp)
    register_all_handlers(dp)


def start_bot():
    bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')
    dp = Dispatcher(bot, storage=MemoryStorage())
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
