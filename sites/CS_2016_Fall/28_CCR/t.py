from pwn import *

#y = process('./ccr-f311dc41963d5cb68a97909189f30644')


box = [i for i in range(32,127)]
check = [0x195,0x1b2,0x1c9,0x1fa,0x1d3,0x1c1,0x1d1,0x18e,0x17d,0x1cb,0x1d1,0x1d2,0x21a,0x21e,0x222,0x1d3,0x1c1,0x1c5,0x1cf,0x1c0,0x20b,0x1c9,0x1c0,0x1ba,0x1c7,0x1c4,0x209,0x218,0x1cf,0x1cc,0x1d3,0x1d2,0x1c5,0x1d3,0x1e3,0x174]
a = [0 for i in range(40)]



def ff(i):
    #print i
    if i > max:
        max = i
    if i == 39:
        s = ''.join(chr(c) for c in a)
        print s
    for b in box:
        if a[i] + a[i+1] + a[i+2] + a[i+3] + b != check[i]:
            continue
        a[i+4] = b
        f(i+1)
    return


def f(i):
    s = ''.join(chr(c) for c in a)
    print s
    if i == 36:
        s = ''.join(chr(c) for c in a)
        print s
        exit(0)
    if check[i] - (a[i] + a[i+1] + a[i+2] + a[i+3]) not in box:
        return
    a[i+4] = check[i] - (a[i] + a[i+1] + a[i+2] + a[i+3])
    f(i+1)
    return
"""
for i1 in box:
    print 'i1 ->' , i1
    for i2 in box:
        for i3 in box:
            for i4 in box:
                for i5 in box:
                    if i1 + i2 + i3 + i4 + i5 != check[0]:
                        continue
                    a[0] = i1
                    a[1] = i2
                    a[2] = i3
                    a[3] = i4
                    a[4] = i5
                    f(1)
"""
a[0] = 70
a[1] = 76
a[2] = 65
a[3] = 71
a[4] = 123

f(1)
