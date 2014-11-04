import socket
import sys
import time
import signal

HOST, PORT = "zeus.vse.gmu.edu", 9999

import logging
logger = logging.getLogger('TIMESYNC')
hdlr = logging.FileHandler('time_sync_client.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.INFO)


cal_logger = logging.getLogger("CAL_LOGGER")
cal_hdlr = logging.FileHandler('CAL_LOG.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
cal_hdlr.setFormatter(formatter)
cal_logger.addHandler(cal_hdlr)
cal_logger.setLevel(logging.INFO)

#zeus.vse.gmu.edu
# SOCK_DGRAM is the socket type to use for UDP sockets
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# As you can see, there is no connect() call; UDP has no connections.
# Instead, data is directly sent to the recipient via sendto().


# class TimeSync(object):
#     def __init__(self):


def handler(signum, frame):
    print "Did Not hearback form the server"
    print frame.f_locals['pay_load']
    logger.error("Failed SEQ_NO: {}".format(frame.f_locals['pay_load']))
    return "Exception(\s\"end of time\")"

def gen_numbers():
    i = 1 
    while True:
        yield i
        i = i + 1 

signal.signal(signal.SIGALRM, handler)

numbers = gen_numbers()
for seq in numbers:
    pay_load =  str(seq) +" "+ "%f" % time.time()
    sock.sendto(pay_load , (HOST, PORT))
    signal.alarm(11)
    try:
        received = sock.recv(1024)
    except:
        continue
    client_rec = "{} {:f}".format(received,time.time())
    logger.info( client_rec)
    data = client_rec.split(" ")
    rec_seq = data[0]
    if seq == int(rec_seq):
        rtt =  (float(data[2]) - float(data[1])) + (float(data[4]) - float(data[3])) 
        theta = (float(data[2]) - float(data[1]) ) - (  float(data[4]) - float(data[3]) ) /2.00
        cal_logger.info(  str(rtt) + " "+ str(theta) )
    else:
        log_string = "Response out of order {}".format(received) 
        logger.info( log_string )

    #print "Received: {} {:f}".format(received,time.time() )
    time.sleep(10)



