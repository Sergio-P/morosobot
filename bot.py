from config import bot
import telebot

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Wena m3n")

@bot.message_handler(commands=['pagar'])
def send_welcome(message):
	print message
        bot.reply_to(message, "Wena m3n")

bot.polling()

