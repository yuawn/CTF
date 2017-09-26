#!/usr/bin/env python2
from libnum import *
from binascii import *
import os , subprocess , itertools , re

#ais3{Euc1id3an_a1g0ri7hm_i5_u53fu1}

publickeys_file =  os.listdir('./rsa2048/pub/')

N = []
e = 0xab1ce13

for i in publickeys_file:
    res = subprocess.check_output( ['openssl' , 'rsa' , '-noout' , '-modulus', '-pubin', '-inform' , 'pem' , '-text' , '-in', './rsa2048/pub/' + i ]  )
    n = int( re.findall( 'Modulus=(.+?)\n' , res )[0] , 16 )
    N.append( n )


flag_enc = int( ''.join( hex( ord( c ) ).replace('0x','').rjust( 2 , '0' ) for c in open( './rsa2048/flag.enc' , 'r' ).read() ) , 16 )
#f2 = int( hexlify(open( './rsa2048/flag.enc' , 'r' ).read()), 16


for n1 , n2 in itertools.product(N,N):
    p = gcd( n1 , n2 )
    if p == 1 or n1 == n2: continue
    q = n1 / p
    d = invmod( e , (p - 1) * (q - 1) )
    flag = ''.join( chr( int( i , 16 ) ) for i in re.findall( '..' , format( pow( flag_enc , d , n1 ) , 'x' ) ) ) 
    if 'ais3' in flag :
        print flag
        break



