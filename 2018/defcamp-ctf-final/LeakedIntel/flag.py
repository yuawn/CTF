#!/usr/bin/env python
from PIL import Image
import re


n = Image.open( './flag2.png' )
m = Image.open( './normal2.png' )
x , y = 14 , 5
#o = Image.new( 'RGB' , ( a , b ) )
#pix = o.load()
#a = n.convert( 'RGB' )
#b = m.convert( 'RGB' )
# 16

print n.getpixel( (1,1) ) , m.getpixel( (1,1) )
print n.getpixel( (1,2) ) , m.getpixel( (1,2) )
print n.getpixel( (1,3) ) , m.getpixel( (1,3) )

fr = ''
fg = ''
fb = ''

for j in xrange( 1 , y - 1 ):
    for i in xrange( 1 , x - 1 ):
        rc , gc , bc = n.getpixel( (0,j) )[0] ^ m.getpixel( (0,j) )[0] , n.getpixel( (0,j) )[1] ^ m.getpixel( (0,j) )[1] , n.getpixel( (0,j) )[2] ^ m.getpixel( (0,j) )[2]
        r , g , b = n.getpixel( ( i , j ) )[0] , n.getpixel( ( i , j ) )[1] , n.getpixel( ( i , j ) )[2]
        r2 , g2 , b2 = m.getpixel( ( i , j ) )[0] , m.getpixel( ( i , j ) )[1] , m.getpixel( ( i , j ) )[2]
        #print '-' * 0x70
        #print hex( r ) , hex( g ) , hex( b )
        #print chr( r ) , chr( g ) , chr( b )
        #print hex( r2 ) , hex( g2 ) , hex( b2 )
        #print chr( r2 ) , chr( g2 ) , chr( b2 )
        #print hex( r ^ r2 ) , hex( g ^ g2 ) , hex( b ^ b2 )
        #print hex( r | r2 ) , hex( g | g2 ) , hex( b | b2 )
        #print hex( r - r2 ) , hex( g - g2 ) , hex( b - b2 )
        #print hex( r ^ r2 ^ rc ) , hex( g ^ g2 ^ gc ) , hex( b ^ b2 ^ bc )
        #print chr( r ^ r2 ^ g ^ g2 ^ b ^ b2 )
        fr += chr( r )
        fg += chr( g )
        fb += chr( b )
        print chr( b ) , chr( b2 )
        #print chr( b ^ b2 )
        #print chr( b ^ b2 ) , hex( b ^ b2 )
    print '-' * 0x70


print fr
print fg
print fb

#o.show()
#o.save( 'flag.png' )


