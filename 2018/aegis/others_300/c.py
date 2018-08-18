#!/usr/bin/env python
from pwn import *
#from keystone import *
#ks = Ks(KS_ARCH_X86, KS_MODE_64)

context.arch = 'amd64'

'''
mov rax, 0x4444444444444444
48 b8 44 44 44 44 44 44 44 44
'''


while True:
    inp = raw_input('>')
    if inp == 'a\n':
        exit()
    try:
        op = asm( inp )
    except:
        print 'crash'
        continue
    no = 0
    for c in op:
        if ord(c) & 3 or c == '\x00':
            no = 1
            break
    print ' '.join( hex( ord( i ) )[2:].rjust( 2 , '0' ) for i in op )
    if no:
        print 'NO'
    else:
        print 'OK'
