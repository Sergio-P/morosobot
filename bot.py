from config import bot
import telebot


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Bueno cabros se viene la hora de pagar. \n Usar los comandos para agregar las deudas pendientes.")


@bot.message_handler(commands=['pagar'])
def pagar_handler(message):
	print message
	bot.reply_to(message, "Wena m3n")


@bot.message_handler(commands=['meDebe'])
def me_debe_handler(message):
	print message
	bot.reply_to(message, "Wena m3n")


@bot.message_handler(commands=['leDebo'])
def le_debo_handler(message):
	print message
	bot.reply_to(message, "Wena m3n")


@bot.message_handler(commands=['paguenCTM'])
def paguen_ctm_handler(message):
	print message
	bot.reply_to(message, "Wena m3n")


@bot.message_handler(commands=['all'])
def all_handler(message):
	print message
	bot.reply_to(message, "Wena m3n")


bot.polling()

