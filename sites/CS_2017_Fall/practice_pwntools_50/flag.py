#!/usr/bin/env python
from pwn import *

# FLAG{h02Ooysbv4O5Lf1Fmdrt2QKts7buYz0J}

host , port = 'csie.ctf.tw' , 10123
y = remote( host , port )

a = 1
b = 50000000

while True:
    mid = ( a + b - 1 ) / 2 
    y.sendlineafter( '=' , str( mid ) )
    print a , b
    o = y.recvline()
    if 'small' in o:
        a = mid - 1
    elif 'big' in o:
        b = mid + 1
    elif 'FLAG' in o:
        print o
        break