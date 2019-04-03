#!/usr/bin/env python
from pwn import *
from ctypes import *
import re

# VolgaCTF{ptr@ce_ant1_r3verse_@ll_in_va1n}

def rol( n , c ):
    c %= 32
    n &= 0xffffffff
    r = ( ( n << c ) & 0xffffffff ) + ( n >> ( 32 - c ) )
    return c_int( r ).value

def ror( n , c ):
    c %= 32
    n &= 0xffffffff
    r = ( n >> c ) + ( ( n << ( 32 - c ) ) & 0xffffffff )
    return c_int( r ).value


t = [0x04, 0x08, 0x15, 0x16, 0x23, 0x42, 0xA0, 0x15, 0x33, 0x97, 0x57, 0x1D, 0x7F, 0x45, 0x9C, 0x25 , 0x0]
r = [0] * 26
s = []

def func2( _a , _b ):
    global r
    a = s[ _a ]
    b = s[ _b ]
    n = r[0] + a
    m = r[1] + b

    for i in range( 1 , 12 + 1 ):
        n = rol( m ^ n , m & 0x1f ) + r[ 2 * i ]
        m = rol( n ^ m , n & 0x1f ) + r[ 2 * i + 1 ]
  
    s[_a] = n
    s[_b] = m


def de_func2( _a , _b ):
    global r
    n = s[_a]
    m = s[_b]

    for i in range( 12 , 0 , -1 ):
        m = ror( m - r[ 2 * i + 1 ] , n & 0x1f ) ^ n
        n = ror( n - r[ 2 * i ] , m & 0x1f ) ^ m

    s[_a] = c_int( n - r[0] ).value
    s[_b] = c_int( m - r[1] ).value


def encode():
    global t , r , s
    ptr = [0] * 4
    a = 4
    b = 4
    buf = [0] * 4

    ptr = [ 0x8faea09e , 0x60b671a , 0x606fe6cc , 0x30bb606b ]

    r[0] = c_int( 0xB7E15163 ).value

    for i in range( 1 , 26 ):
        r[i] = c_int( r[ i - 1 ] - 0x61C88647 ).value


    j , i , p , q , n = 0 , 0 , 0 , 0 , 26
    m = max( n , b )

    for k in range( 1 , 3 * m + 1 ):
        r[i] = rol( c_int( q + r[i] + p ).value , 3 )
        q = r[i]
        i = ( i + 1 ) % n

        ptr[j] = rol( c_int( q + ptr[j] + p ).value , c_int( q + p ).value & 0x1f )
        p = ptr[j]
        j = ( j + 1 ) % b

    for i in range( ( len( s ) + 7 ) >> 3 ):
        func2( 2 * i , 2 * i + 1 )



s = 'yuawn777'
s = [ u32( _ ) for _ in re.findall( '....' , s ) ]
encode()

# decode
s = open( './data.jac2' ).read()
s = [ u32( _ ) for _ in re.findall( '....' , s ) ]

for i in range( len(s) >> 1 ):
    de_func2( 2 * i , 2 * i + 1 )

flag = ''.join( p32( _ ) for _ in s ).strip('\0')
print flag