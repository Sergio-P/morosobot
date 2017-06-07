from config import bot
import telebot

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Bueno cabros se viene la hora de pagar. \n Usar los comandos para agregar las deudas pendientes.")

bot.polling()

