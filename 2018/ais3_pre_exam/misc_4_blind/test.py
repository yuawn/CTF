#!/usr/bin/env python
from pwn import *
from hashlib import sha256
import random , string , re
from Crypto.Cipher import AES
from base64 import b64encode as b64e
from base64 import b64decode as b64d

key = 'abcdefgh01234567'


def p128( n ):
    h = hex( n )[2:]
    if len( h ) % 2:
        h = '0' + h
    s = ''.join( chr( int( c , 16 ) ) for c in re.findall( '..' , h ) ).rjust( 16 , '\x00' ) 
    return s
    
def u128( s ):
    #print ''.join( hex( ord( c ) ).replace( '0x' , '' ).rjust( 2 , '0' ) for c in s )
    return  int( ''.join( hex( ord( c ) ).replace( '0x' , '' ).rjust( 2 , '0' ) for c in s ) , 16 )


def decrypt(text):
    key = 'abcdefgh01234567'
    #key = 'k' * 0x10 
    iv, text = text[:16], text[16:]
    aes = AES.new(key, AES.MODE_CBC, iv)
    return aes.decrypt(text)

def encrypt(text ,key = '\x00' * 0x10  ):
    iv = '\x00' * 16
    aes = AES.new(key, AES.MODE_CBC, iv)
    return aes.encrypt(text)

iv = '\x00' * 16

#ci = '\x00' * 0x10
'''
for i in xrange( 0x100 ):
    iv = '\x00' * 16
    print hex(i) , hex( u128( decrypt( iv + encrypt( '\x00' * 16 , key = chr( i ) + '\x00' * 15 ) ) ) )
'''
key = 'abcdefgh01234567'
k = ''
for i in key:
    k += i
    print hex( u128( decrypt( iv + encrypt( '\x00' * 16 , key = k.ljust( 16 , '\x00' ) ) ) ) )


#print p128( 0x12345678 )
#print hex( u128( p128( 0x12345678 ) ) )

#print hex( u128( decrypt( iv + encrypt( p128( 0x10 ) ) ) ) )
#print hex( u128( decrypt( iv + encrypt( p128( 0x11 ) ) ) ) )
#print hex( u128( decrypt( iv + encrypt( p128( 0x12 ) ) ) ) )



'''
p = 'a' * 16
enc = encrypt( p )
print enc , len( enc )
dec = decrypt( iv + enc )
print dec
'''