import math
import struct
import time

import zmq

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

while True:
    current = int(time.time())
    request = struct.pack('l', current) + struct.pack('d', math.sin(current))
    time.sleep(1)
    socket.send(bytes(request))
    message = socket.recv()
