import asyncio

from aiogram import Bot, Dispatcher
from handlers import CommandRouter
from configs.config import Config

bot = Bot(token=Config.bot_token)
dp = Dispatcher()

async def main():
    dp.include_router(CommandRouter)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")