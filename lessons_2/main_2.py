from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
import emoji
from asyncio import sleep

HELP_COMMAND = '''
/start - Начать работу с ботом
/help - Список команд
/games - Игра
'''


bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_commands(message: types.Message):
    await message.reply(text=HELP_COMMAND)  # reply - это ответить на сообщение


@dp.message_handler(commands=['help'])
async def help_commond(message: types.Message):
    await message.answer(text="Спасибо что пользуетесь нашим ботом!")  # answer - это означает ответить(написать)
    await message.delete()


@dp.message_handler(commands=['games'])
async def reply_dice(message: types.Message):
    await message.answer(text="Да начнётся игра!")
    await sleep(1)

    await message.answer(text="Моя кость")
    bot_data = await bot.send_dice(message.from_user.id)
    bot_data = bot_data["dice"]["value"]
    await sleep(4)

    await message.answer(text="Твоя кость")
    user_data = await bot.send_dice(message.from_user.id)
    user_data = user_data["dice"]["value"]
    await sleep(5)

    if bot_data > user_data:
        await message.answer(text="Проигрыш" + emoji.emojize(":moai:"))
    elif bot_data < user_data:
        await message.answer(text="Победа за тобой" + emoji.emojize(":trophy:"))
    else:
        await message.answer(text="Ничья" + emoji.emojize(":handshake:"))


if __name__ == '__main__':
    executor.start_polling(dp)