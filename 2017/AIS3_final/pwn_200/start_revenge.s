global _start

section .text
_start :
	xor rax,rax
	xor rbx,rbx
	xor rcx,rcx
	xor rdx,rdx
	xor rdi,rdi
	xor rsi,rsi
	call main
	mov rax,0x3c
	xor rdi,rdi
	syscall


main:
	push rdx
	push rsi
	push rdi
	call magic
	pop rdi
	pop rsi
	pop rdx
	ret

write:
	xor rax,rax
	mov rdx,rsi
	mov rsi,rdi
	xor rdi,rdi
	inc rdi
	inc rax
	syscall
	ret
	

magic:
	push rbp
	mov rbp,rsp
	sub rsp,0x30
	call message
	mov rdi,rsp
	mov rsi,0x80
	call read_input
	leave
	ret
	

message:
	push rax
	mov r8,0xa203f20656d6167
	push r8
	mov r8,0x20612079616c7020
	push r8
	mov r8,0x6577206c6c656853
	push r8
	mov rsi,24
	mov rdi,rsp
	call write
	add rsp,0x18
	pop rax
	ret

read_input:
	mov rdx,rsi
	mov rsi,rdi
	xor rdi,rdi
	xor rax,rax
	syscall
	ret
