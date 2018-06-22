#!/usr/bin/env python
from pwn import *
from hashlib import sha256
import random , string , re
from Crypto.Cipher import AES
from base64 import b64encode as b64e
from base64 import b64decode as b64d

# 

host , port = '104.199.235.135' , 20004
y = remote( host , port )

def pppp( n ):
    a = hex( n )[2:]
    if len( a ) % 2:
        a = '0' + a
    return (''.join( chr( int( i , 16 ) ) for i in re.findall( '..' , a ) )).ljust( 16 , '\x00' )




y.recvuntil( '== \'' )
a = y.recv( 6 )
print a
y.recvuntil( '== \'' )
b = y.recv( 6 )
print b

p = range(48,58) + range(65,91) + range(97,123)

sol = ''

for i in xrange( 0x100000000 ):
    sol = a + str( i )
    if sha256( sol ).hexdigest().startswith( b ):
        break

y.sendlineafter( '=' , sol )


def ppp( n ):
    a = hex( n )[2:]
    if len( a ) % 2:
        a = '0' + a
    return ''.join( chr( int( i , 16 ) ) for i in re.findall( '..' , a ) )



def crack2( p , ans , bloc ):
    prev = 0
    for i in xrange( 127 - 16 , 0 , -16 ):
        for j in xrange( 1 << bloc , -1 , -1 ):
            now = prev ^ ( j << ( (( i / bloc ) + 1) * bloc ) )
            #print hex(now)
            p2 = p ^ now
            #print hex( p2 ) , hex( p2 ^ flip( i ) ) , hex( ans )
            if i == -1:
                i = 0
            if ( p2 > ans ) ^ ( ( p2 ^ flip( i ) ) > ans ):
                prev = now
                print hex( p2 ) , hex( p2 ^ flip( i ) ) , hex( ans )
                break
            elif not j:
                 print 'fail %d' % i
                 return 0
    return 1


def crack( iv , ci , bloc ):
    iv = 0
    for i in xrange( 127 - 16 , 0 , -16 ):
        for j in xrange( 1 << bloc , -1 , -1 ):
            tmp = iv ^ ( j << ( (( i / bloc ) + 1) * bloc ) )
            #y.interactive()
            y.sendlineafter( ':' , b64e( ppp( tmp ) + ci ) )
            a = y.recvline()
            y.sendlineafter( ':' , b64e( ppp( tmp ^ flip( i ) ) + ci ) )
            b = y.recvline()
            print a , b


    return 1


ci = ''
for _ in xrange(0x10000):
    ci = os.urandom(16)
    iv = 0
    if crack( iv , ci , 16 ):
        print 'win!!!!!!!'
        break
    else:
        print 'gen'





y.interactive()
