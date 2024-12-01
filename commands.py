from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command  # Фильтр для обработки команд

router = Router()  # Роутер для маршрутизации сообщений


# Обработчик команды /start
@router.message(Command("start"))  # Указываем фильтр для команды "start"
async def start_command_handler(message: Message) -> None:  # Обрабатываем входящее сообщение
    # Ответ бота на команду /start
    await message.answer("Скоро здесь можно будет купить наикрутейшие гаджеты со всего света!")


# Обработчик команды /help
@router.message(Command("help"))  # Указываем фильтр для команды "help"
async def help_command_handler(message: Message) -> None:  # Обрабатываем входящее сообщение
    await message.answer(
        "Чем могу помочь?"  # Ответ бота на команду /help
    )
