# -*- coding: utf-8 -*-

import os
from config import bot
from dbAPI import *
from msUtils import split_message, split_message_multiple
from grafo import *
import telebot


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Bueno cabros se viene la hora de pagar. \nUsar los comandos para agregar las deudas pendientes. " + \
		"\nAgregar deuda con commando /medebe @tagdeudor monto" + \
		"\nSaldar deuda o ya pago usar commando /mepago @tagdeudor monto" + \
		"\nMostrar deudas pendientes del usuario usar commando /ledebo" + \
		"\nPara ver mis deudores /paguenctm")


@bot.message_handler(commands=['mePago', 'mepago'])
def pagar_handler(message):
	try:
		name, monto = split_message(message.text)
		if not existe_usuario(name):
			agregar_usuario(name)
		r = pagar_deuda(name, '@' + message.from_user.username, monto)
		if r == -1:
			bot.reply_to(message, u"No hay deudas m3n")
		else:
			bot.reply_to(message, u"👌")
	except Exception:
		bot.reply_to(message, "Mensaje incorrecto")


@bot.message_handler(commands=['meDebe', 'medebe'])
def me_debe_handler(message):
	try:
		names, monto = split_message_multiple(message.text)
		for name in names:
			if not existe_usuario(name):
				agregar_usuario(name)
			agregar_deuda(name, '@' + message.from_user.username, monto)
		bot.reply_to(message, u"👌")
	except Exception as e:
		print e
		bot.reply_to(message, "Mensaje incorrecto")


@bot.message_handler(commands=['leDebo', 'ledebo'])
def le_debo_handler(message):
	deudas = consultar_deuda('@' + message.from_user.username)
	builder = "Deudas de @%s:\n" % message.from_user.username
	for deuda in deudas:
		builder += "A %s le debe $%d\n" % (deuda[0], deuda[2])
	bot.reply_to(message, builder)


@bot.message_handler(commands=['paguenCTM', 'paguenctm'])
def paguen_ctm_handler(message):
	deudas = consultar_deudores('@' + message.from_user.username)
	builder = "Deudas a @%s:\n" % message.from_user.username
	for deuda in deudas:
		builder += "%s debe $%d\n" % (deuda[1], deuda[2])
	bot.reply_to(message, builder)


@bot.message_handler(commands=['all'])
def all_handler(message):
	buildGraph()
	f = open("network.png")
	bot.send_photo(message.chat.id, f)


# bot.polling()
with open("PID","w") as f:
 	f.write(str(os.getpid())+"\n")

c = 0

while c<50:
	try:
		bot.polling()
	except Exception as e:
		c += 1
		print "uff m3n"
		with open("log.txt","a") as f:
			f.write("Error " + str(c) + "\n");
			f.write(str(e) + "\n");
			f.write("----------\n");
