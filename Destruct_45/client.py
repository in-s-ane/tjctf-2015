import socket

HOST = "p.tjctf.org"
PORT = 8085

def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    sock.settimeout(0.3)
    while True:
        received = ""
        try:
            while True:
                received += sock.recv(4096)
        except Exception, e:
            print repr(received)
        to_send = raw_input("> ")
        to_send = [ch for ch in to_send]
        for i in xrange(0, len(to_send)):
            if i < len(to_send):
                if to_send[i] == "\\":
                    if to_send[i+1] == "x":
                        to_send[i] = ''.join(to_send[i+2:i+4]).decode('hex')
                        del to_send[i+3]
                        del to_send[i+2]
                        del to_send[i+1]
        to_send = ''.join(to_send)
        sock.send(to_send + "\n")

    sock.close()

client()
