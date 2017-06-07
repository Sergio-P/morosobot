from config import bot
from dbAPI import *
from msUtils import splitMessage
import telebot


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Bueno cabros se viene la hora de pagar. \n Usar los comandos para agregar las deudas pendientes.")


@bot.message_handler(commands=['pagar'])
def pagar_handler(message):
	try:
		name, monto = splitMessage(message.text)
		if not existe_usuario(name):
			agregar_usuario(name)
		pagar_deuda(message.from_user.username, name, monto)
		bot.reply_to(message, "ACK")
	except Exception:
		bot.reply_to(message, "Mensaje incorrecto")


@bot.message_handler(commands=['meDebe'])
def me_debe_handler(message):
	try:
		name, monto = splitMessage(message.text)
		if not existe_usuario(name):
			agregar_usuario(name)
		agregar_deuda(name, message.from_user.username, monto)
		bot.reply_to(message, "ACK")
	except Exception as e:
		print e
		bot.reply_to(message, "Mensaje incorrecto")


@bot.message_handler(commands=['leDebo'])
def le_debo_handler(message):
	deudas = consultar_deuda(message.from_user.username)
	builder = ""
	for deuda in deudas:
		pass
	bot.reply_to(message, builder)


@bot.message_handler(commands=['paguenCTM'])
def paguen_ctm_handler(message):
	deudas = consultar_deudores(message.from_user.username)
	builder = "Deudas:\n"
	for deuda in deudas:
		builder += str(deuda) + "\n"
	bot.reply_to(message, builder)


@bot.message_handler(commands=['all'])
def all_handler(message):
	print message
	bot.reply_to(message, "Wena m3n aun no somos tan pro")


bot.polling()

