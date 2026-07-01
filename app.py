from aiogram import Dispatcher,  Bot
from os import getenv
from dotenv import load_dotenv
import asyncio
from handlers.routers import router
load_dotenv()
TOKEN = getenv("BOT_TOKEN")


dp = Dispatcher()
dp.include_router(router)


async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
