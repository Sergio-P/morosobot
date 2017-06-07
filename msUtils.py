

def splitMessage(message):
	#: string -> string, int
	messageList = message.split(" ")
	if (len(messageList) != 2):
		raise Exception('input wrong')

	nombre = messageList[0]
	monto = 0
	try:
		monto = int(messageList[1])
	except ValueError:
		raise Exception('input wrong')

	return nombre, monto
