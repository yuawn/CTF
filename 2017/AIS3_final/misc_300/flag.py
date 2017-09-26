#!/usr/bin/env python
from pwn import *


a = open( 'new' , 'r+' )
b = open('xor.9bit.txt').read()

bit = ''.join(['{:08b}'.format(ord(x)) for x in b])
out = [ int(x, 2) for x in group(9, bit) ]

for i in out:
    a.write( chr( i ) )

