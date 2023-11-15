import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from config import Config


async def main():
    bot = Bot(token=Config.TOKEN_BOT, parse_mode=ParseMode.HTML)  # Создание экземпляра бота
    dp = Dispatcher()  # Создание экземпляра диспетчера

    await bot.delete_webhook(drop_pending_updates=True)  # Отключаем функцию ответа на запросы, которые были пока бот выключен

    try:
        await dp.start_polling(bot)
    except Exception as _ex:
        print(_ex)
        sys.exit(1)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
