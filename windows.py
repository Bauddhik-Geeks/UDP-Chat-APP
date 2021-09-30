import os
os.system("cls")
os.system("color 6")

from pyfiglet import Figlet 
f = Figlet(font="puffy")
a = f.renderText("UDP CHAT APP")
print(a)

# importing required modules...
import socket
import threading

# AF_INET = Network Address Family : ipv4
# SOCK_DGRAM = DataGram Socket : UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# System IP
ip = "Ip of the System"
port = 2222

# Reciever IP
sendip = input("\n\t\tEnter Reciever IP : ")
sendport = 1111

# Binding system IP and port
s.bind((ip, port))

# Function for sending message
def send():
	while True:
		x = input("")
		s.sendto(x.encode(), (sendip, sendport))
		if (("bye" in x) or ("exit" in x)):
			os._exit(1)
			
# Function for recieving message
def recieve():
	while True:
		x = s.recvfrom(1024)
		print("\n\t\t\t" + "{} : ".format(sendip) + x[0].decode())

# Applying Multi-Threading
send = threading.Thread( target=send )
recieve = threading.Thread( target=recieve )

send.start()
recieve.start()
