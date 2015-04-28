heap32 = [94,70,68,80,65,64,81,88,84,91,65]
string32 = ""
for num in heap32:
    string32 += chr(num)

heap8 = []
# This is the reversal of _testChar
# _testChar checks that the (first input) ^ (second input) = 46 + iteration (which goes from 0 to 10)
for i in range(0, 11):
    sol = 46 + i
    flag_char = sol ^ heap32[i]
    heap8.append(flag_char)

string8 = ""
for num in heap8:
    string8 += chr(num)

print string8
# Flag: pitassembly
