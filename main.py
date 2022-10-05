#from lib2to3.pgen2 import token
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # for reply keyboard (sends message)

from time import sleep
from rqsts import reqs, reqs_form

bot = Bot(token = '5570488759:AAGZMemAss0TuVg-hvPAmWcRTdKCcjRE-RM')
dp = Dispatcher(bot)

answers = []

@dp.message_handler(commands=['start'])
async def city(message: types.Message):
    await message.answer('Hello, send the place where you want to know the temperature.\nFormat is <your city>,<your country abbreviation>\nExample: London,uk')

@dp.message_handler()
async def city(message: types.Message):
    try:
        res = reqs(message.text)
        res1 = reqs_form(res)
        print('Successful request.')
    except(BaseException):
        #await message.answer('Wrong place name.')
        res1 = 'Wrong place name.'
        print("Unsuccessful request.")
    #print(message.text)
    #answers.append(message.text)
    #print(answers)
    #i = 1
    await message.answer(res1)

executor.start_polling(dp)

