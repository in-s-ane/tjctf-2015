flag = [0] * 8

flag[0] -= 10
flag[1] -= -6
flag[2] -= 11
flag[3] -= 3
flag[4] -= -2
flag[5] -= -4
flag[6] -= -13
flag[7] -= 8

for i in range(0, len(flag)):
    flag[i] += 109
    flag[i] -= 1

flag_decrypted = [chr(ch) for ch in flag]
print ''.join(flag_decrypted)
