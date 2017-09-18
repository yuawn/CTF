#!/usr/bin/env python
# -*- coding: ascii -*-

a = open( 'UNKOWN' , 'r+' )
o = open( 'UNKOWN2' , 'r+' )

t = a.read()

for i in range( len( t ) - 1 , -1 , -1 ):
    o.write( t[ i ] )