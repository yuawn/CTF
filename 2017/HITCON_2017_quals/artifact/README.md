# 完美無瑕\~Impeccable Artifact\~
## Perfection , Pwn 192
> 72 solved
* SECCOMP
* https://github.com/david942j/seccomp-tools
```C
 line  CODE  JT   JF      K
=================================
 0000: 0x20 0x00 0x00 0x00000004  A = arch
 0001: 0x15 0x00 0x10 0xc000003e  if (A != ARCH_X86_64) goto 0018
 0002: 0x20 0x00 0x00 0x00000020  A = args[2]
 0003: 0x07 0x00 0x00 0x00000000  X = A
 0004: 0x20 0x00 0x00 0x00000000  A = sys_number
 0005: 0x15 0x0d 0x00 0x00000000  if (A == read) goto 0019
 0006: 0x15 0x0c 0x00 0x00000001  if (A == write) goto 0019
 0007: 0x15 0x0b 0x00 0x00000005  if (A == fstat) goto 0019
 0008: 0x15 0x0a 0x00 0x00000008  if (A == lseek) goto 0019
 0009: 0x15 0x01 0x00 0x00000009  if (A == mmap) goto 0011
 0010: 0x15 0x00 0x03 0x0000000a  if (A != mprotect) goto 0014
 0011: 0x87 0x00 0x00 0x00000000  A = X
 0012: 0x54 0x00 0x00 0x00000001  A &= 0x1
 0013: 0x15 0x04 0x05 0x00000001  if (A == 1) goto 0018 else goto 0019
 0014: 0x1d 0x04 0x00 0x0000000b  if (A == X) goto 0019
 0015: 0x15 0x03 0x00 0x0000000c  if (A == brk) goto 0019
 0016: 0x15 0x02 0x00 0x0000003c  if (A == exit) goto 0019
 0017: 0x15 0x01 0x00 0x000000e7  if (A == exit_group) goto 0019
 0018: 0x06 0x00 0x00 0x00000000  return KILL
 0019: 0x06 0x00 0x00 0x7fff0000  return ALLOW
```
* `read`,`write`,`fstat`,`lseek` are directly allowed.
* `mmap` and `mprotect` are killed when the third arg is odd, because the third arg for `mmap` and `mprotect` are prot of the memory, the execution bit is not allowed to be set.
* When the syscall is not all of above and the syscall number of it is equal to the third arg, it could pass the seccomp rule.
> case1: `read`,`write`,`fstat`,`lseek` , these are directly going to `0019 ALLOW`.
> case2: `mmap` and `mprotect` , be judge at `X = args[2] ; 0011:A = X ; 0012 A &= 0x1` ,  if the third argument of these two syscall is odd it will go to `0018 KILL` else go to `0019 ALLOW`.
> case3: All others syscall would continue at `0014 if (A == X) goto 0019`, obviously the syscalls with its `args[2]` is equal to syscall number can pass the rules `goto 0019 ALLOW`.
* Therefor, `open` is great for this XD
* In the end, ORW.