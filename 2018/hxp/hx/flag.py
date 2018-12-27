#!/usr/bin/env python

a = open( './pic.jpeg' ).read()
b = open( 'tmp.jpg' , 'w+' )

m = '\xef\xbf\xbd'

s = a.replace( m , '' )
b.write( s )
b.close()