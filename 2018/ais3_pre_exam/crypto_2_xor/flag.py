#!/usr/bin/env python
import os
import random

# AIS3{captAIn aMeric4 - Wh4T3V3R HapPenS t0mORr0w YOU mUst PR0Mis3 ME on3 tHIng. TH4T yOu WiLL stAY Who Y0U 4RE. Not A pERfect sO1dIER, buT 4 gOOD MAn.}

enc = open('./flag-encrypted').read()
print ' '.join( hex( ord(c) ).replace( '0x' , '' ) for c in enc) , len( enc )

enc_end = '\x1f\x75\xbb\x1a\x92\x61\xbc\x35\x58\xe9'

k = '\x16\x09\x7c\xc7\xdd\x4f\x2e\x92\xa7\xff'
kt = '\x16\x09\x7c\xc7\xdd'

print '---'
print ' '.join( hex( ord(k[i]) ^ ord( k[(i+1) %10]) ).replace( '0x' , '' ) for i in xrange( 10 ) )
print ' '.join( hex( ord(c) ).replace( '0x' , '' ) for c in enc_end )
print '---'

a = open('./xortool_out/04669.out').read()[:10]
b = enc[:10]
print ' '.join( hex( ord(k[i]) ^ ord(b[i]) ).replace( '0x' , '' ) for i in xrange(10))

flag = 'AIS3{aaaaaaaaaa}'

def extend(key, L):
    kL = len(key)
    return key * (L // kL) + key[:L % kL]

def xor(X, Y):
    c = ''
    return ''.join( chr( ord(x) ^ ord(y) ) for x, y in zip(X, Y))

key = '123456789'
plain = flag + key
print plain , len( plain )
key = extend(key, len(plain))
print key , len( key )
cipher = xor(plain, key)

print ' '.join( hex( ord(c) ).replace( '0x' , '' ) for c in cipher )

print '---'
print ''.join( chr( ord(k[i%10]) ^ ord(enc[i]) ) for i in xrange( len( enc ) ) )