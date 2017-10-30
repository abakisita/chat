import zmq
import random
import sys
import time
import thread

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:%s" % port)



def listener():
    while(True):
        msg = socket.recv()
        print "Com 1 : " + msg

thread.start_new_thread(listener)

while True:
    mess = raw_input("enter message")
    socket.send(mess)

    time.sleep(1)
