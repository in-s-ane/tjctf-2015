def base_conv(v1, a1, a2):
    n1 = {c: i for i, c in enumerate(a1)}
    print n1
    b1 = len(a1)
    b2 = len(a2)

    d1 = 0
    for i, c in enumerate(v1):
        d1 += n1[c] * pow(b1, len(v1) - i - 1)

    v2 = ""
    while d1:
        v2 = a2[d1 % b2] + v2
        d1 //= b2


    return v2

a1 = "0123456789"
a2 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

print base_conv("fabcab", a2, a1)
print base_conv("38102360685", a1, a2)
