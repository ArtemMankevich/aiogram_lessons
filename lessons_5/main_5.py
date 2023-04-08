from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN


bot = Bot(TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('БОТ ЗАПУЩЕН')


async def set_commands():
    await bot.set_my_commands(commands=[
        types.BotCommand(command='start', description='register user'),
        types.BotCommand(command='help', description='show commands list'),
        types.BotCommand(command='listServers', description='list servers'),
        types.BotCommand(command='addServer', description='add server'),
        types.BotCommand(command='sendCommand', description='execute command on server'),
        types.BotCommand(command='menu', description='show main menu'),
    ])


HELP_COMMOND ='''
<b>/start</b> - <em>Начало работы бота</em>
<b>/help</b> - <em>Помощь</em>
<b>/test</b> - <em>Стикер</em>
'''


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply(text=HELP_COMMOND, parse_mode='HTML')


@dp.message_handler(commands=['test'])
async def cat(message: types.Message):
    await message.answer('смотри какой котик 🙃')
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEIeLJkLdFF4kYcAUMXQecKjvUanEZxowACgmIAAp7OCwABxjogBFIwtlAvBA')


@dp.message_handler()
async def heart(message: types.Message):
    if message.text == '❤️':
        return await message.answer('😘')
    await message.answer(text=str(message.text.count('😀')))

@dp.message_handler()
async def count(message: types.Message):
    await message.answer(text=str(message.text.count('😀')))



if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)