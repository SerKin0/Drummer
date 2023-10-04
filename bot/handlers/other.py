from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message

from bot.keyboards.inline import creatInlineButtonIndex


async def start(message: Message):
    await message.answer("Привет!👋\n\nЯ помогу тебе проработать некоторые задания и ЕГЭ, на примерах.")


def register_other_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(start, commands="start")
