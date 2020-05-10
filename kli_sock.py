#-*-coding: utf-8-*-
import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 8009
s.connect((host, port))
s.send(b'hello')
data = s.recv(10000000)
print ('received', data, len(data), 'bytes')
s.send(b'helloooo')
