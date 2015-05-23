import zmq
import time


context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
for request in range(10):
    print("Sending request %s" % request)
    time.sleep(1)
    socket.send(str(request).encode('ascii'))
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))
