from tkinter import *
import socket
class MyWindow:
	def __init__(self, win):
		self.lbl1=Label(win, text='Section')
		self.lbl2=Label(win, text='Information')
		self.lbl3=Label(win, text='Result')
		self.t1=Entry(bd=3)
		self.t2=Entry()
		self.t3=Entry()
		self.btn1 = Button(win, text='Add')
		self.btn2=Button(win, text='Find')
		self.lbl1.place(x=100, y=50)
		self.t1.place(x=200, y=50)
		self.lbl2.place(x=100, y=100)
		self.t2.place(x=200, y=100)
		self.b1=Button(win, text='Add', command=self.add)
		self.b2=Button(win, text='Subtract')
		self.b2.bind('<Button-1>', self.sub)
		self.b1.place(x=100, y=150)
		self.b2.place(x=200, y=150)
		self.lbl3.place(x=100, y=200)
		self.t3.place(x=200, y=200)
	def add(self):
		self.t3.delete(0, 'end')
		num1=int(self.t1.get())
		num2=int(self.t2.get())
		result=num1+num2
		self.t3.insert(END, str(result))
	def sub(self, event):
		self.t3.delete(0, 'end')
		section=str(self.t1.get())
		info=str(self.t2.get())
		msgFromClient="FETCH/"+section+"/"+info
		bytesToSend=str.encode(msgFromClient)
		serverAddressPort=("127.0.0.1", 20001)
		bufferSize=1024
		# Create a UDP socket at client side
		UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
		# Send to server using created UDP socket
		UDPClientSocket.sendto(bytesToSend, serverAddressPort)
		msgFromServer = UDPClientSocket.recvfrom(bufferSize)
		msg = "Message from Server {}".format(msgFromServer[0])
		self.t3.insert(END, str(msg))

window=Tk()
mywin=MyWindow(window)
window.title('Hello Python')
window.geometry("400x300+10+10")
window.mainloop()
