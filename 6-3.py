import socket
import time
import colorama
from colorama import Fore

clientSocket = socket.socket()

host = '192.168.230.5'
port = 8889

clientSocket.connect((host,port))

print('\nConnecting to ', host, '....')

time.sleep(1)

response = clientSocket.recv(1024)
print(response.decode('utf-8'))
colorama.init()
print(Fore.CYAN)
while True:
	print('\n*****************')
	print('Online Calculator')
	print('*****************')
	print('1. Logarithm')
	print('2. Square Root')
	print('3. Exponential')
	print('4. Exit')
	choice = input('\nPlease select one : ')

	clientSocket.send(choice.encode('utf-8'))

	if int(choice) == 1:
		num = input('\nPlease enter a number to Log : ')
		clientSocket.send(num.encode('utf-8'))
		answer = clientSocket.recv(1024)
		print('Answer for Log ',num,':',answer.decode('utf-8'))
	elif int(choice) == 2:
		num = input('\nPlease enter a number to Square Root: ')
		clientSocket.send(num.encode('utf-8'))
		answer = clientSocket.recv(1024)
		print('Answer for Square Root ',num,':',answer.decode('utf-8'))
	elif int(choice) == 3:
		num = input('\nPlease enter a number to Exponent: ')
		clientSocket.send(num.encode('utf-8'))
		answer = clientSocket.recv(1024)
		print('Answer for Exponential ',num,':',answer.decode('utf-8'))
	else:
		False
		clientSocket.send(choice.encode('utf-8'))
		print('\nThank You!')
		clientSocket.close()
		break

clientSocket.close()
