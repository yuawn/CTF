#!/usr/bin/env python
from pwn import *

context.arch = 'amd64'

'''
for i in xrange( 0x100 ):
    if i & 3:
        continue
    print '-' * 0x30
    print disasm( chr(i) )
'''


for i in xrange( 0x100 ):
    for j in xrange( 0x100 ):
        if i & 3 or j & 3:
            continue
        print '-' * 0x30
        print disasm( chr(i) + chr(j))
