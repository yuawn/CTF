#!/usr/bin/env python2
import requests 
import urllib2 
import hashlib

#Flag1: AIS3{SHA1111l111111_is_broken}</br>Flag2: AIS3{Any_limitation_can_not_stop_me!!!!!l!!!!}
#AIS3{SHA1111l111111_is_broken}

aa = open( 'shattered-1.pdf' , 'r' ).read()
bb = open( 'shattered-2.pdf' , 'r' ).read()

#a = urllib2.urlopen("http://shattered.io/static/shattered-1.pdf").read()[:500]; 
#b = urllib2.urlopen("http://shattered.io/static/shattered-2.pdf").read()[:500];

#aa.write( a )
#bb.write( b )

# brute force with SHA1() startswith 'f00d'
"""
p = 0

for j in range( 1000 ):
    for i in range(5000):
        print i , j
        a = aa[:i] + '\x00Snoopy_do_not_like_cats_hahahaha\x00ddaa_is_PHD' + '\x00' * j
        b = bb[:i] + '\x00Snoopy_do_not_like_cats_hahahaha\x00ddaa_is_PHD' + '\x00' * j
        print hashlib.sha1( a ).hexdigest()
        print hashlib.sha1( b ).hexdigest()
        if hashlib.sha1( a ).hexdigest().startswith( 'f00d' ) or hashlib.sha1( b ).hexdigest().startswith( 'f00d' ):
            p = 1
            break
    
    if p:
        break

"""

l = 3754
preffix = ''

a = aa[ : l ] + '\x00Snoopy_do_not_like_cats_hahahaha\x00ddaa_is_PHD' + '\x00' * 18 # 18 is the result of brute force
b = bb[ : l ] + '\x00Snoopy_do_not_like_cats_hahahaha\x00ddaa_is_PHD' + '\x00' * 18

url = 'https://web2.nasa.yuawn.idv.tw/ais3.php' # self host test
url = 'https://quiz.ais3.org:32670/'

r = requests.post( url, data={'username': a , 'password': b });

print r.text

print hashlib.sha1( a ).hexdigest()
print hashlib.sha1( b ).hexdigest()
