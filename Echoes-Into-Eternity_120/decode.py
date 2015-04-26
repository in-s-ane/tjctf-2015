import base64
import zlib

with open("getrekt.m9", "r") as f:
    data = f.read()
    data = base64.b64decode(data)
    data = zlib.decompress(data[599869:615110])
    print data
