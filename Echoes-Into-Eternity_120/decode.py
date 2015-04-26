import base64

with open("getrekt.m9", "r") as f:
    data = f.read()
    data = data.decode('rot13')
    data = base64.b64decode(data)
    pcap = open("output.pcap", "w")
    pcap.write(data)
    pcap.close()
