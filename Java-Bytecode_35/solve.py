# If con(x) % 10 == 1, then we've passed the check.
def con(x):
    i = 0
    d = 0
    while i < len(x) - 1:
        d += ord(x[i]) - 48
        i+=2
    i = 1
    while i < len(x) - 1:
        d += (ord(x[i]) - 48) * 3
        i+=2
    return d

print con('0258691432369')


