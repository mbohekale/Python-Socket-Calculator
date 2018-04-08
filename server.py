import socket

server = socket.socket()
server.bind(('', 3000))
print 'Server ready at 127.0.0.1'
server.listen(1)
client, address = server.accept()
print 'Got connection from', address
while True:
	data = []
	data.append(client.recv(1024))
	if data[0] == 'exit':
		print 'Exiting'
		server.close()
		client.close()
		break
	data.append(client.recv(1024))
	data.append(client.recv(1024))
	if data[1] == '+':
		hasil = int(data[0]) + int(data[2])
	elif data[1] == '-':
		hasil = int(data[0]) - int(data[2])
	elif data[1] == '*':
		hasil = int(data[0]) * int(data[2])
	elif data[1] == '/':
		hasil = int(data[0]) / int(data[2])
	print data[0], data[1], data[2], '=', hasil
	client.send(str(hasil))