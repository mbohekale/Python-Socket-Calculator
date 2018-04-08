import socket

client = socket.socket()
ipaddr = raw_input('Connect to IP: ')
client.connect((ipaddr, 3000))
print 'Connected to server'
while True:
	operator = raw_input('Operator: ')
	operandA = raw_input('Operand 1: ')
	operandB = raw_input('Operand 2: ')
	client.send(operandA)
	client.send(operator)
	client.send(operandB)
	print 'Hasil:', client.recv(1024)
	if 'exit' == raw_input('Type "exit" to exit, no input to continue '):
		client.send('exit')
		client.close()
		exit()