#!/usr/bin/env python
# -*- coding: ascii -*-
import re


a = open( 'hex' , 'r+' )
o = open( 'ans.zip' , 'r+' )

b = a.read().split('\n')

print b[0][9:-18].replace( ' ' , '' ) , re.findall( '..' , b[0][9:-18].replace( ' ' , '' ) )

#print b[0][-16:]

for i in range( len( b ) ):
    print b[i]
    for j in re.findall( '..' , b[i][9:-18].replace( ' ' , '' ) ):
        o.write( chr( int( j , 16 ) ) )

