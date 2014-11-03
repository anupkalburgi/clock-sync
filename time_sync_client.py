import socket
import sys
import time
import signal

HOST, PORT = "zeus.vse.gmu.edu", 9999
# SOCK_DGRAM is the socket type to use for UDP sockets
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# As you can see, there is no connect() call; UDP has no connections.
# Instead, data is directly sent to the recipient via sendto().


# class TimeSync(object):
#     def __init__(self):


def handler(signum, frame):
    print "Did Not hearback form the server"
    print frame.f_locals['pay_load']
    return "Exception(\s\"end of time\")"

def gen_numbers():
    i = 1 
    while True:
        yield i
        i = i + 1 

signal.signal(signal.SIGALRM, handler)

numbers = gen_numbers()
for seq in numbers:
    pay_load =  str(seq) +" "+ str(time.time())
    sock.sendto(pay_load , (HOST, PORT))
    signal.alarm(11)
    try:
        received = sock.recv(1024)
    except:
        #print exc
        continue
    print "Sent:     {}".format(pay_load)
    print "Received: {}".format(received)
    time.sleep(10)



