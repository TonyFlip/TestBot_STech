import telebot
import datetime

token="6669520620:AAFfFBfUGP95_mOl27j-_ccmDqH9ppZDUow"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Привет! Напиши мне команду /date , что бы узнать какой сегодня день.")

@bot.message_handler(commands=['date'])
def send_date(message):
    today = datetime.datetime.today().strftime("%d-%m-%Y")
    day_of_week = datetime.datetime.today().strftime("%A")
    bot.reply_to(message, f"Сегодняшняя дата: {today}\n День недели: {day_of_week}")


bot.polling()
