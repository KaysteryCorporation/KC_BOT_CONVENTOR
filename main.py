from utils import *
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
from aiogram.dispatcher import FSMContext

import logging

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await Form.check.set()
    markup = types.ReplyKeyboardRemove()
    reply_markup = markup
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("Yes!", "Later")
    await message.reply("Hi there! \nI'm KaysteryBot \nStart of work?", reply_markup=markup)

@dp.message_handler(state='*', commands='cancel')
async def cancel_handler(message: types.Message, state: FSMContext):
    await state.finish()
    markup = types.ReplyKeyboardRemove()
    reply_markup = markup
    await message.reply('Cancelled.', reply_markup=markup)

@dp.message_handler(state=Form.check)
async def check_valute(message: types.Message, state=FSMContext):
    if message.text=="Yes!":
        await Form.inpu.set()
        async with state.proxy() as data:
            data["outpu"] = [0, 0, 0, 0, 0, 0]
        markup = types.ReplyKeyboardRemove()
        reply_markup = markup
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        markup.add("Dollars", "Euro", "Russian Rubles", "Turkish Lira")
        markup.add("Cryptocurrencies", "Finish entering the currency")
        await message.reply("Please fill in your account information", reply_markup=markup)
    if message.text=="Later":
        await message.reply("if you change your mind, click [Yes]")

@dp.message_handler(state=Form.inpu)
async def inpu_valute(message: types.Message, state=FSMContext):
    if message.text == "Dollars":
        markup = types.ReplyKeyboardRemove()
        reply_markup = markup
        await message.reply("Account balance in dollars:",reply_markup=markup)
        await Form.usd.set()
    if message.text == "Euro":
        markup = types.ReplyKeyboardRemove()
        reply_markup = markup
        await message.reply("Account balance in euros:",reply_markup=markup)
        await Form.eur.set()
    if message.text == "Russian Rubles":
        markup = types.ReplyKeyboardRemove()
        reply_markup = markup
        await message.reply("Account balance in Russian rubles:",reply_markup=markup)
        await Form.rub.set()
    if message.text == "Turkish Lira":
        markup = types.ReplyKeyboardRemove()
        reply_markup = markup
        await message.reply("Account balance in Turkish Lira:",reply_markup=markup)
        await Form.tur.set()
    if message.text == "Bitcoin":
        markup = types.ReplyKeyboardRemove()
        reply_markup = markup
        await message.reply("Account balance in bitcoins:",reply_markup=markup)
        await Form.bit.set()
    if message.text == "Go back to the main currencies":
        markup = types.ReplyKeyboardRemove()
        reply_markup = markup
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        markup.add("Dollars", "Евро", "Russian Rubles", "Turkish Lira")
        markup.add("Cryptocurrencies", "Finish entering the currency")
        await message.reply("We return it to the main currency section",reply_markup=markup)
    if message.text == "Cryptocurrencies":
        markup = types.ReplyKeyboardRemove()
        reply_markup = markup
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        markup.add("Bitcoin", "Go back to the main currencies")
        await message.reply("Переходим в раздел Cryptocurrencies", reply_markup=markup)
    if message.text == "Finish entering the currency":
        markup = types.ReplyKeyboardRemove()
        reply_markup = markup
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        markup.add("View the invoice", "Start conversion")
        await Form.outpu.set()
        await message.reply("Great, Currency entry completed\nYou can view your account or start converting", reply_markup=markup)

@dp.message_handler(state=Form.usd)
async def usd_valute(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data["outpu"][0] +=float(message.text)
        sum=data["outpu"][0]
    s="The input value was successful\nAccount in dollars: "+str(sum)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("Dollars", "Euro", "Russian Rubles", "Turkish Lira")
    markup.add("Cryptocurrencies", "Finish entering the currency")
    await message.reply(s, reply_markup=markup)
    await Form.inpu.set()

@dp.message_handler(state=Form.eur)
async def eur_valute(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data["outpu"][1] +=float(message.text)
        sum=data["outpu"][1]
    s="The input value was successful\nAccount in euros: "+str(sum)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("Dollars", "Euro", "Russian Rubles", "Turkish Lira")
    markup.add("Cryptocurrencies", "Finish entering the currency")
    await message.reply(s, reply_markup=markup)
    await Form.inpu.set()

@dp.message_handler(state=Form.rub)
async def rub_valute(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data["outpu"][2] +=float(message.text)
        sum=data["outpu"][2]
    s="The input value was successful\nAccount in Russian rubles: "+str(sum)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("Dollars", "Euro", "Russian Rubles", "Turkish Lira")
    markup.add("Cryptocurrencies", "Finish entering the currency")
    await message.reply(s, reply_markup=markup)
    await Form.inpu.set()

@dp.message_handler(state=Form.tur)
async def tur_valute(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data["outpu"][3] +=float(message.text)
        sum=data["outpu"][3]
    s="The input value was successful\nAccount in Turkish Lira: "+str(sum)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("Dollars", "Euro", "Russian Rubles", "Turkish Lira")
    markup.add("Cryptocurrencies", "Finish entering the currency")
    await message.reply(s, reply_markup=markup)
    await Form.inpu.set()

@dp.message_handler(state=Form.bit)
async def bit_valute(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data["outpu"][4] +=float(message.text)
        sum=data["outpu"][4]
    s="The input value was successful\nBitcoin account: "+str(sum)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("Dollars", "Euro", "Russian Rubles", "Turkish Lira")
    markup.add("Cryptocurrencies", "Finish entering the currency")
    await message.reply(s, reply_markup=markup)
    await Form.inpu.set()


@dp.message_handler(state=Form.outpu)
async def outpu_valute(message: types.Message, state=FSMContext):
    if message.text == "View the invoice":
        async with state.proxy() as data:
            l = data["outpu"]
        await message.reply(await outputvalute(l))
    if message.text == "Start conversion":
        markup = types.ReplyKeyboardRemove()
        reply_markup = markup
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        markup.add("Dollars", "Euro", "Russian Rubles", "Turkish Lira")
        markup.add("Bitcoin", "Abort conversion")
        await message.reply("The currency in which we will convert?",reply_markup=markup)
        await Form.val1.set()

@dp.message_handler(state=Form.val1)
async def val1_valute(message: types.Message, state=FSMContext):
    k=-1
    if message.text == "Dollars":
        k=0
    if message.text == "Euro":
        k=1
    if message.text == "Russian Rubles":
        k=2
    if message.text == "Turkish Lira":
        k=3
    if message.text == "Bitcoin":
        k=4
    if message.text =="Start conversion":
        markup = types.ReplyKeyboardRemove()
        reply_markup = markup
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        markup.add("View the invoice", "Start conversion")
        await message.reply("Conversion aborted",reply_markup=markup)
        await Form.outpu.set()
    if k != -1:
        async with state.proxy() as data:
            data["val1"]=k
        await message.reply("OK, enter the original currency")
        await Form.val2.set()

@dp.message_handler(state=Form.val2)
async def val2_valute(message: types.Message, state=FSMContext):
    k=-1
    if message.text == "Dollars":
        k=0
    if message.text == "Euro":
        k=1
    if message.text == "Russian Rubles":
        k=2
    if message.text == "Turkish Lira":
        k=3
    if message.text == "Bitcoin":
        k=4
    if message.text =="Start conversion":
        markup = types.ReplyKeyboardRemove()
        reply_markup = markup
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        markup.add("View the invoice", "Start conversion")
        await message.reply("Conversion aborted",reply_markup=markup)
        await Form.outpu.set()
    async with state.proxy() as data:
        l = data["outpu"]
    if l[k] <= 0:
        markup = types.ReplyKeyboardRemove()
        reply_markup = markup
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        markup.add("View the invoice", "Start conversion")
        await message.reply("Conversion aborted\nThe account balance of the source currency is less than or equal to 0", reply_markup=markup)
        await Form.outpu.set()
        k=-1
    if k != -1:
        async with state.proxy() as data:
            data["val2"]=k
        markup = types.ReplyKeyboardRemove()
        reply_markup = markup
        await message.reply("Enter the amount of currency you want to convert",reply_markup=markup)
        await Form.inmon.set()

@dp.message_handler(state=Form.inmon)
async def inmon_valute(message: types.Message, state=FSMContext):
    if is_digit(message.text):
        if float(message.text) > 0:
            async with state.proxy() as data:
                k=data["outpu"][data["val2"]]
            if k - float(message.text) >= 0:
                async with state.proxy() as data:
                    data["inmon"]=float(message.text)
                await Form.startcon.set()
                markup = types.ReplyKeyboardRemove()
                reply_markup = markup
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
                markup.add("Yes", "No")
                async with state.proxy() as data:
                    k = data["inmon"]
                    i1 = data["val2"]
                    i2 = data["val1"]
                    if i1 == 0:
                        v1 = "USD"
                    if i1 == 1:
                        v1 = "EUR"
                    if i1 == 2:
                        v1 = "RUB"
                    if i1 == 3:
                        v1 = "TRY"
                    if i1 == 4:
                        v1 = "BTC"
                    if i2 == 0:
                        v2 = "USD"
                    if i2 == 1:
                        v2 = "EUR"
                    if i2 == 2:
                        v2 = "RUB"
                    if i2 == 3:
                        v2 = "TRY"
                    if i2 == 4:
                        v2 = "BTC"
                    p1 = float(await get_currency(v1))
                    p2 = float(await get_currency(v2))
                    curs="1 "+v1+" to "+v2+" exchange rate: "+str(p2/p1)+"\nComplete the conversion?"
                await message.reply(curs, reply_markup=markup)
            else:
                await message.reply("Entered a number exceeding the balance in the original currency\nTry again")
        else:
            await message.reply("The specified number is less than 0, only positive numbers can be converted\nTry again")
    else:
        message.reply("This character set is not a number\nTry again")

@dp.message_handler(state=Form.startcon)
async def convert_valute(message: types.Message, state=FSMContext):
    if message.text == "Yes":
        async with state.proxy() as data:
            k =data["inmon"]
            i1=data["val2"]
            i2=data["val1"]
            if i1 == 0:
                v1="USD"
            if i1 == 1:
                v1="EUR"
            if i1 == 2:
                v1="RUB"
            if i1 == 3:
                v1="TRY"
            if i1 == 4:
                v1="BIT"
            if i2 == 0:
                v2="USD"
            if i2 == 1:
                v2="EUR"
            if i2 == 2:
                v2="RUB"
            if i2 == 3:
                v2="TRY"
            if i2 == 4:
                v2="BIT"
            p1=float(await get_currency(v1))
            p2=float(await get_currency(v2))
            data["outpu"][i2]+=k*(1/p1)*p2
            data["outpu"][i1]-=k
        markup = types.ReplyKeyboardRemove()
        reply_markup = markup
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        markup.add("View the invoice", "Start conversion")
        await Form.outpu.set()
        await message.reply("Successful conversion",reply_markup=markup)
    if message.text == "No":
        markup = types.ReplyKeyboardRemove()
        reply_markup = markup
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        markup.add("View the invoice", "Start conversion")
        await message.reply("Conversion aborted", reply_markup=markup)
        await Form.outpu.set()




if __name__ == '__main__':
    executor.start_polling(dp)
