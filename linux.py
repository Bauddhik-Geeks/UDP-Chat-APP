import os
os.system("clear")

from pyfiglet import Figlet
f = Figlet(font='puffy')
a = f.renderText("UDP CHAT APP")
os.system("tput setaf 3")
print(a)

# importing required modules...

import socket
import threading

# AF_INET = Network Address Family : ipv4
# SOCK_DGRAM = DataGram Socket : UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# System IP
ip = " IP "
port = 1111

# Reciever IP
os.system("tput setaf 6")
sendip = input("\n\t\tEnter Reciever IP: ")
sendport = 2222
os.system("tput setaf 7")

# Binding system IP and port
s.bind((ip, port))

os.system("tput setaf 2")

# Function for recieving message
def recieve():
    while True:
      x = s.recvfrom(1024)
      print("\n\t\t\t" + "{} : ".format(sendip) + x[0].decode())
       
# Function for sending message
def send():
    while True:
      x = input("")
      s.sendto(x.encode(), (sendip, sendport))
      if (("bye" in x) or ("exit" in x)):
        os.system("tput setaf 7")
        os._exit(1)
        

# Applying Multi-Threading
recieve = threading.Thread( target=recieve )
send = threading.Thread( target=send )

recieve.start()
send.start()

