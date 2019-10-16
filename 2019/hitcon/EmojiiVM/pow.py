#!/usr/bin/env python

# hitcon{M0mmy_I_n0w_kN0w_h0w_t0_d0_9x9_em0j1_Pr0gr4mM!ng}

import subprocess

from pwn import *

r = remote('3.115.122.69', 30261)

r.recvuntil('token:\n')
cmd = r.recvline().strip()

res = subprocess.check_output(cmd.split()).strip()
print res

r.recvuntil('token: ')
r.sendline(res)

p = open( './payload' ).read()
r.sendlineafter( ')' , str( len(p) ) )

r.send( p )


r.interactive()