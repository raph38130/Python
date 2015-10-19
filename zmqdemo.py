from tkinter import *
import zmq
from threading import Thread


class App():
    def __init__(self):
        context = zmq.Context()
        self.socket = context.socket(zmq.PUB)
        self.socket.bind("tcp://*:5556")
        root = Tk()
        self.canvas = Canvas(root, background='white')
        self.canvas.bind('<B1-Motion>', self.on_motion)
        self.canvas.pack()
        try:
                thread = Thread(target = self.display)
                thread.start()
        except:
                print ("Error: unable to start thread")
        root.mainloop()

    def display(self):
        context = zmq.Context()
        socket = context.socket(zmq.SUB)
        socket.setsockopt_string(zmq.SUBSCRIBE,"")
        socket.connect ("tcp://localhost:5556")
        socket.connect ("tcp://172.16.116.78:5556")
        socket.connect ("tcp://172.16.116.176:5556")
        while True :
            string =socket.recv()
            a=int(string[5:8])
            b=int(string[11:14])
            if string[0:2]==bytes('rp','utf-8'):
               self.canvas.create_line(a,b,a+1,b+1,fill="red")
            elif string[0:2]==bytes('lp','utf-8'):
               self.canvas.create_line(a,b,a+1,b+1,fill="green")
            elif string[0:2]==bytes('mf','utf-8'):
               self.canvas.create_line(a,b,a+1,b+1,fill="blue")
            else :
               self.canvas.create_line(a,b,a+1,b+1,fill="black")

    def on_motion(self, event):
        self.socket.send_string("rp x=%03d y=%03d" % (event.x,event.y))
   	 
App()

