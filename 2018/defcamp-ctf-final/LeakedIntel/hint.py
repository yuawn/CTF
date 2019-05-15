#!/usr/bin/env python
import re

s = open( 'hint.txt' ).read()

print len( s ) % 8

#print ''.join( chr( int( _ , 16 ) ) for _ in re.findall( '..' , s[:0x100] ) )


