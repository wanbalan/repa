#-*-coding: utf-8-*-
import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

host = "255.255.255.255"
port = 8008
#s.connect((host, port))
s.sendto(b'hello',(host,port))
data = s.recvfrom(10000000)
print ('received', data, len(data), 'bytes')
