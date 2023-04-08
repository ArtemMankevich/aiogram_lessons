from aiogram import Dispatcher, Bot, types, executor
from сonfig import TOKEN


bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_upper(messege: types.Message):
    if messege.text.count(' ') >= 1:
        await messege.answer(text=messege.text.upper())


if __name__ == '__main__':
    executor.start_polling(dp)


