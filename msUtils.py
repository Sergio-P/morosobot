

def split_message(message):
	#: string -> string, int
	messageList = message.split(" ")
	if (len(messageList) != 3):
		raise Exception('input wrong')

	nombre = messageList[1]
	monto = 0
	try:
		monto = int(messageList[2])
	except ValueError:
		raise Exception('input wrong')

	return nombre, monto
