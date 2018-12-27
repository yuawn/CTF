BITS 32

; ref. http://www.muppetlabs.com/~breadbox/software/tiny/teensy.html 
; nasm -f bin -o tiny.elf tiny.asm

org     0x00010000

db      0x7F, "ELF"             ; e_ident
dd      1                                       ; p_type
dd      0                                       ; p_offset
dd      $$                                      ; p_vaddr
dw      2                       ; e_type        ; p_paddr
dw      3                       ; e_machine
dd      _start                  ; e_version     ; p_filesz
dd      _start                  ; e_entry       ; p_memsz
dd      4                       ; e_phoff       ; p_flags

_start:

mov     al, 3                  ; e_shoff       ; p_align
mov     ecx, esp
dec     edx
int     0x80
jmp     esp
dw      0x20                    ; e_phentsize
db      1                       ; e_phnum
; e_shentsize
; e_shnum
; e_shstrndx

filesize      equ     $ - $$