import telebot
token='6669520620:AAFfFBfUGP95_mOl27j-_ccmDqH9ppZDUow'
bot=telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,"Привет!")

@bot.message_handler(content_types=["text"])
def parrot(message):
    bot.send_message(message.chat.id, message.text)


bot.infinity_polling()