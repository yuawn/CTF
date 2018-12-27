#!/usr/bin/env python
from pwn import *

context.arch = 'amd64'


f = '\x7fELF'
f += p8( 2 )        # 32 or 64
f += p8( 1 )        # little-endian 
f += p8( 1 )        # ELF version
f += p8( 0 )        # platform.
f += p64( 0 )       # e_ident[EI_PAD] currently unused
f += p16( 2 )       # e_type 0x02	ET_EXEC
f += p16( 0x3e )    #  e_machine 0x3E	x86-64
f += p32( 1 )       #  e_version
f += p64( 0 )        #  e_entry
f += p64( 0 )        # e_phoff Points to the start of the program header table
f += p64( 0 )[:-3]   # e_shoff Points to the start of the section header table.

elf = open( 'gen.elf' , 'w+' )
elf.write( f )
elf.close()