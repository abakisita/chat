import zmq
import random
import sys
import time

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://10.0.0.11:%s" % port)

while True:
    msg = socket.recv()
    print msg
    socket.send("message recieved")

    time.sleep(1)
