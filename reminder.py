from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token='5300873799:AAHI2Tel_yCprOkXnEJm2LlGoQE9gl1LsAo')
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


executor.start_polling(dp, skip_updates=True)
