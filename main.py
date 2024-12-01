from aiogram import Bot, Dispatcher
from commands import router  # Подключаем роутер для маршрутизации сообщений
from menu import set_bot_commands

import asyncio  # Для управления асинхронным кодом

from config.myToken import myToken  # Мой токен под секретом и надёжно защищён верой в святых сусликов всевышних
import log  # Логирование программы # noqa

# Инициализация бота
API_TOKEN = myToken  # Токен вашего бота
bot = Bot(token=API_TOKEN)  # Создаём объект бота
dp = Dispatcher()  # Диспетчер для управления логикой бота


# Основная функция
async def main() -> None:
    dp.include_router(router)  # Подключаем роутер к диспетчеру

    await set_bot_commands(bot)  # Устанавливаем команды для бота

    await bot.delete_webhook(drop_pending_updates=True)  # Удаляем старые обновления
    await dp.start_polling(bot)  # Запускаем бота в режиме long polling


# Запуск бота
if __name__ == "__main__":
    asyncio.run(main())  # Запускаем основной цикл приложения
