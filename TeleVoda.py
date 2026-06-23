import telebot
import requests
import time
from telebot import types
bot = telebot.TeleBot('ВАШ ТОКЕН')
voda = 0
voda_old = 0
voda_sum = 0
reminder = 0
reminder_old = 0
reminder_sum = 0
voda_reccomend = 2000
def reminderr(timelow):
    time.sleep(timelow)
@bot.message_handler(commands=['start'])
def start_privet(message):
    bot.send_message(message.chat.id,"Здравствуйте это бот напоминалка для напоминания о питье. \n команда /setreminder для напоминания пример /setreminder 1 \n команда для питья воды /drank \n команда /status чтобы узнать сколько выпито и сколько осталось выпить \n но для начала поставьте для себя сколько литров воды вы будете пить в день")
    bot.register_next_step_handler(message,reccomendmes)
def reccomendmes(message):
    bot.send_message(message.chat.id,"впишите нужное количество литров воды которое вы хотите пить в день(не менее 2 литров в день)")
    bot.register_next_step_handler(message,smenareccomend)
def smenareccomend(message):
    global voda_reccomend
    vremya = int(message.text)
    vremya *= 1000
    if vremya >= 2000:
        voda_reccomend = vremya
        bot.send_message(message.chat.id,"для работы бота дальше впишите /setreminder чтобы поставить напоминание")
    else:
        bot.send_message(message.chat.id,"поставлено рекомендованное количество воды в день(2 литра)")
    
@bot.message_handler(commands=['setreminder'])
def reminderprinatie(message):
    try:
        global reminder,reminder_old,reminder_sum
        command,tim = message.text.split()
        reminder = int(tim) * 60
        reminder_old = reminder 
        reminder_sum += reminder
        reminderr(reminder)
        bot.send_message(message.chat.id,f"Пора пить воду! /drank для подтверждения о том что ты попил")
    except ValueError:
        bot.reply_to(message.chat.id,"Please enter the correct amount.")
@bot.message_handler(commands=['drank'])
def mamamasssa(message):
    global reminder_old,voda_sum
    command,vod = message.text.split()
    voda_sum += int(vod)
    bot.send_message(message.chat.id,f"вы попили {vod} мили литров воды")
    reminderr(reminder_old)
    bot.send_message(message.chat.id,f"Пора пить воду! /drank для подтверждения о том что ты попил")
@bot.message_handler(commands=['status'])
def summavodi(message):
    global voda_sum,voda_reccomend
    ostalosb = voda_reccomend - voda_sum
    if ostalosb > 0:
        bot.send_message(message.chat.id,f"выпито {voda_sum}, осталось выпить {ostalosb}")
    else:
        bot.send_message(message.chat.id,"поздравляю вы выпили рекоммендованное количество воды")
        voda_sum = 0

bot.infinity_polling()
