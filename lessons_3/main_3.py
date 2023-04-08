from aiogram import Dispatcher, Bot, executor, types
from config import TOKEN
import string
import random


count = 0

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['description'])
async def desc_command(message: types.Message):
    await message.reply('бот умеет отправлять рандомные символу латинского алфавита')
    await message.delete()


@dp.message_handler(commands=['count'])
async def cheac_count(message: types.Message):
    global count
    await message.reply(f'COUNT: {count}')
    count += 1


@dp.message_handler()
async def cheac_zero(messege: types.Message):
    if '0' in messege.text:
        return await messege.reply('YES')
    await messege.reply('NO')



@dp.message_handler()
async def random_letter(messege: types.Message):
    await messege.reply(random.choice(string.ascii_letters))
    #await messege.delete()


if __name__ == '__main__':
    executor.start_polling(dp)
