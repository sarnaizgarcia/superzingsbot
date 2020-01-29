import telebot
from secrets import token
from superzings import list

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    # tu_mensaje = tufuncion() <- te la importas de otro lado
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, "/list para enseñar una lista")

@bot.message_handler(commands=['list'])
def send_list(message):
	bot.reply_to(message, list)

@bot.message_handler(regexp='Rocketzing')
def send_rocket(message):
    rocket_url = 'https://www.superzings.com/es/characters/rocketzing'
    bot.reply_to(message, rocket_url)



@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
