lines = []
buf = ''
with open('out.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        (coord, colors) = line.split(' :: ')
        (r, g, b) = colors[1:-2].split(' ')
        buf += bin(int(b))[-1]
        #print bin(int(r))[-1], bin(int(g))[-1], bin(int(b))[-1]

print ''.join(chr(int(buf[i:i+8], 2)) for i in xrange(0, len(buf), 8))

'''
>> python solve.py
qQmNin3!
'''
