#!/usr/bin/env python

s = open( './jac2.ori' ).read()

o = open( './jac2.patch' , 'w+' )
o.write( s[:0x17b1] + '\x90' * ( 0x17b6 - 0x17b1 ) + s[0x17b6:0x17E1] + '\x90' * 5 + s[0x17E6:])
o.close()