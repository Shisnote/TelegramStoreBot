from aiogram.types import BotCommand  # BotCommand для установки команд в меню бота


async def set_bot_commands(bot):
    bot_commands = [
        BotCommand(command="start", description="Вперёд за покупками!"),
        BotCommand(command="help", description="Помощь святых сусликов всевышних")
    ]

    await bot.set_my_commands(bot_commands)  # Устанавливаем команды для бота
