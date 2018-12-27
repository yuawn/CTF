#!/usr/bin/env python
from pwn import *

context.arch = 'amd64'



for i in xrange( 0xff ):
    #for j in xrange( 0xff ):
    print '-' * 0x30
    print disasm( chr( i ))