import pyotp
import subprocess
import sys

'''
So the story is, I messed up my query string, and I thought the factors that
we're given were out of order.... So here's the code I wrote to figure out the
order of the factors (assuming they were out of order).

def advance(ordered):
    cookie = ''
    for factor in ordered:
        totp = pyotp.TOTP(factor).now()
        output = subprocess.Popen(
                "curl -s http://501.p.tjctf.org/ -d 'password=%s' -b 'session=%s' --cookie-jar - "
                % (totp, cookie),
                shell=True,
                stdout=subprocess.PIPE).stdout.read()
        new_cookie = output[output.find("session"):].split()[1]
        if cookie == new_cookie:
            print "FAIL"
        else:
            cookie = new_cookie
    return cookie


ordered = []
with open('ordered.txt', 'r') as f: # List of known ordered factors
    ordered = [x.strip() for x in f.readlines()]

with open('factors.txt', 'r') as f:
    factors = [x.strip() for x in f.readlines()]
    for factor in factors:
        if factor in ordered:
            continue
        print "Trying: " + factor
        cookie = advance(ordered)
        print "Cookie: " + cookie
        totp = pyotp.TOTP(factor).now()
        output = subprocess.Popen(
                "curl -s http://501.p.tjctf.org/ -d 'password=%s' -b 'session=%s' --cookie-jar - "
                % (totp, cookie),
                shell=True,
                stdout=subprocess.PIPE).stdout.read()
        if output.find("Yup") != -1:
            print "SUCCESS"
            with open('ordered.txt', 'a') as g:
                g.write(factor + '\n')
            sys.exit(0)
'''

cookie = ''
counter = 1
factors = []
with open('factors.txt', 'r') as f:
    factors = [x.strip() for x in f.readlines()]
    for factor in factors:
        print "COOKIE: " + cookie
        print factor
        totp = pyotp.TOTP(factor).now()
        print "TOTP: " + str(totp)
        output = subprocess.Popen(
                "curl -s http://501.p.tjctf.org/ -d 'password=%s' -b 'session=%s' --cookie-jar - "
                % (totp, cookie),
                shell=True,
                stdout=subprocess.PIPE).stdout.read()
        if output.lower().find("flag") != -1 or counter >= 501:
            print output
        if output.find("Yup") != -1:
            new_cookie = output[output.find("session"):].split()[1]
            if cookie == new_cookie:
                print "FAIL"
                sys.exit(1)
            else:
                print "SUCCESS: " + str(counter)
                cookie = new_cookie
                counter += 1
