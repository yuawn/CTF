#!/usr/bin/env python
from PIL import Image
import re


m = Image.open( './leak.png' )
#m = Image.open( './normal.png' )
x , y = 14 , 5
o = Image.new( 'RGB' , ( x , y ) )
pix = o.load()
#a = n.convert( 'RGB' )
#b = m.convert( 'RGB' )
# 16

#print a.getpixel( (0,0) )

for i in xrange( x ):
    for j in xrange( y ):
        pix[ i , j ] = m.getpixel( ( i + 712 + 16 , j + 365 ) )
        


#o.show()
o.save( 'normal2.png' )


