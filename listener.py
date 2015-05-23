import os.path
import struct

import bcolz
import numpy as np
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

if not os.path.exists('db'):
    print("db not found, creating")
    ct = bcolz.ctable([np.empty(0, dtype="i8"),
                       np.empty(0, dtype="i8")],
                      names=['time', 'value'],
                      rootdir='db',
                      )
else:
    print("db found, initializing")
    ct = bcolz.open('db')

while True:
    message = socket.recv()
    print("Received request: %s" % message)
    time = struct.unpack('l', message[:8])
    value = struct.unpack('d', message[8:])
    ct.append((time, value))
    ct.flush()
    socket.send(b"OK")
