with open("irc.log", "r") as f:
    data = f.readlines()
    output = ""
    for line in data:
        if "PRIVMSG #rekt :" in line and len(line) > 100:
            b64encoded_string = line[line.find(":")+1:]
            output += b64encoded_string
    pcap = open("output3.pcap", "w")
    pcap.write(output.decode('base64'))
