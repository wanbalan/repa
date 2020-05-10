#-*-coding: utf-8-*-
import socket
import sys
from tkinter import*
import threading
import time
class sok(Frame):
	count=0
	def __init__(self,**conf):
		self.port,self.host=conf["Порт"],conf["Хост"]
		Frame.__init__(self)
		self.pack()
		self.connect()
		self.gia()
	def gia(self):
		Button(text="close connect",command=self.close).pack()
		Button(text="quit",command=lambda:root.destroy()).pack()
		self.thread=threading.Thread(target=self.load,daemon=True)
		self.thread.start()	
	def connect(self):
		self.d=True
		self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
		self.s.bind((self.host, self.port))
	def load(self,**conf):
		while self.d==True:
			data, addr = self.s.recvfrom(10000000)
			if not data:
				break
			print ('client is at', addr , data)
			self.s.sendto(data,(addr))
		time.sleep(1)
		self.load()
	def close(self):
		co.count+=1
		if co.count%2!=0:self.d=False
		else:self.d=True

if __name__=="__main__":
	root=Tk()
	config={"Порт":8008,"Хост":"0.0.0.0"}
	co=sok(**config)
	root.mainloop()
	#root.protocol('WM_DELETE_WINDOW', con.close)
	