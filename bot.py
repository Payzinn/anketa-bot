import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import router  
from config import BOT_TOKEN  

# Основная функция для инициализации бота и запуска опроса
async def main():
    bot = Bot(token=BOT_TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    dp.include_router(router)
    await dp.start_polling(bot)

# Запуск программы
if __name__ == "__main__":
    asyncio.run(main())
