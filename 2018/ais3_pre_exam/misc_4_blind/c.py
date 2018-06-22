#!/usr/bin/env python2
import os
from Crypto.Cipher import AES
from base64 import b64decode

key = os.urandom(16)
#key = '\xf6\x90ou\x10\x01"=\x19\x94\xda\xd5|{\xfa\x0c'
#ansr = 'ur\xf3\xb6\xb3\r#U\xc2WSe\xbb$\xcap'
ansr = os.urandom(16)
ans = int( ''.join( hex( ord( i ) ).replace( '0x' , '' ).rjust( 2 , '0' ) for i in ansr ) , 16 )
print 'anser -> %s' % hex( ans )

def t( s ):
    return int( ''.join( hex( ord( i ) ).replace( '0x' , '' ).rjust( 2 , '0' ) for i in s ) , 16 )

def flip( n ):
    return 1 << n



def check( p , ans , i , bloc , prev ):
    for j in xrange( 1 << bloc , -1 , -1 ):
        now = prev ^ ( j << ( ( i / bloc ) * bloc ) )
        p2 = p ^ now
        if ( p2 > ans ) ^ ( ( p2 ^ flip( i ) ) > ans ):
            print i
            if not i % bloc:
                prev = now
                print prev
            break
        elif not j:
            print 'fial %d' % i
            if not i % bloc:

            return -1

    return prev



def crack( p , ans ):
    prev = 0
    for i in xrange( 127 , 110 , -1 ):
        prev = check( p , ans , i , 16 , prev )   
        if prev == -1:
            return 0     
                #print hex(p2) , hex(p2 ^ flip( i )) , hex( ans )
    return 1


ci = ''
for _ in xrange(1):
    iv = '\x00' * 16
    aes = AES.new(key, AES.MODE_CBC, iv)
    ci = os.urandom(16)
    p = aes.decrypt( ci )
    #print hex( t(p) )
    if crack( t(p) , ans ):
        print 'win!!!!!!!'
        break
    else:
        print 'gen'
    




'''
p = aes.decrypt( ci )

p = t(p)

bloc = 16
t = 0
prev = 0

for i in xrange( 127 , -1 , -1 ):
    t += 1
    #print 't -> %d %d' % ( t , i )
    for j in xrange( 1 << bloc , -1 , -1 ):
        now = j << ( ( i / bloc ) * bloc ) ^ prev
        p2 = p ^ now
        if ( p2 > ans ) ^ ( ( p2 ^ flip( i ) ) > ans ):
            print i
            if not i % bloc:
                prev = now
            break
        elif not j:
            print 'Fail on %d' % i
            break

'''
'''
for i in xrange( 127 , -1 , -1 ):
    a = t(p)
    b = t(p) ^ flip( i )
    print i , (a>ans) ^ (b>ans) , hex( a ) , hex( b ) , hex( ans )
    if ( a > ans ) ^ ( b > ans ):
        print hex( a ) , hex( b ) , hex( ans )
    elif ( a > ans ) ^ ( b > ans ):
'''



