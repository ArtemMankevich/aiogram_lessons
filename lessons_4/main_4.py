from aiogram import Dispatcher, Bot, executor, types
from config import TOKEN


bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(content_types=['new_chat_member'])  # или '/'
async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("help", "Помощь"),
        types.BotCommand("test", "Тест"),
        types.BotCommand("form", "Форма"),
        types.BotCommand("menu", "Меню"),
    ])


async def on_startup(_):
    print("БОТ ЗАПУЩЕН")


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(f'<em>Привет! <b>{message.from_user.username}</b> </em>', parse_mode="HTML")


@dp.message_handler(commands=['test'])
async def start_command(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEIeLJkLdFF4kYcAUMXQecKjvUanEZxowACgmIAAp7OCwABxjogBFIwtlAvBA')
    await message.delete()


@dp.message_handler()
async def emoji(messege: types.Message):
    await messege.reply(messege.text + '🌝')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)