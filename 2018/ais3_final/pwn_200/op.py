#!/usr/bin/env python
from pwn import *


context.arch = 'amd64'


for i in range( 0xff , -1 , -1 ):
    print '--------'
    print disasm( chr( i ) + chr( i ) )