#!/usr/bin/env python
from pwn import *
import re , string , itertools

# AIS3{So you had some skill about reverse windows shellcode. Contact inndy.lin@cycarrier.com for an internship if you like. :D}

context.arch = 'amd64'
s = open('native_checker').read()

for i in range( 200 ):
    print i , '-' * 0x10
    sc = s[i*0x21:(i+1)*0x21]
    o = disasm(sc)
    o = o.split('\n')
    base = int(o[0][o[0].find('# 0x')+4:],16)
    l = u32( sc[10:10+4] )
    print o[3]
    num = int( re.findall( ', 0x([0-9a-f]+)' , o[3] )[0] , 16 )
    #print hex(l) , hex(num) , hex(base)

    s = list(map(ord,s))
    for j in range(l):
        if 'add' in o[3]:
            s[(i+1)*0x21+j] += num
            s[(i+1)*0x21+j] &= 0xff
        elif 'sub' in o[3]:
            s[(i+1)*0x21+j] -= num
            s[(i+1)*0x21+j] &= 0xff
        elif 'xor' in o[3]:
            s[(i+1)*0x21+j] ^= num
        else:
            print o[3]
            exit(0)

    s = ''.join(list(map(chr,s)))
    print hex((i+1)*0x21)

f = open('native_checker2','w+')
f.write(s)
f.close()


s = open('native_checker2').read()
o = disasm( s[0x253f:] )

pool = string.printable
d = {}

for i in itertools.product( pool , repeat=3 ):
    hsh = 1
    for c in i:
        hsh = (hsh - ord(c)) & 0xffffffff
        hsh = (hsh * 0x314159) & 0xffffffff
        hsh ^= hsh >> 3
    hsh -= 4
    d[hsh] = ''.join(i)

flag = ''
for hsh in re.findall( 'xor    eax, 0x([0-9a-f]+)' , o ):
    flag += d[int(hsh,16)]
print flag