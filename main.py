import asyncio
import logging
from aiogram import Bot, Dispatcher

from app.config import settings
from app.handlers import user


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    bot = Bot(token=settings.bot_token)
    dp = Dispatcher()

    dp.include_router(user.router)

    logging.info("Бот запущен и готов к работе!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Бот остановлен")