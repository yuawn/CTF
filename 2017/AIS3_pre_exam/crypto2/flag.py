#!/usr/bin/env python2
from pwn import *
import hashpumpy , base64

host , port = 'quiz.ais3.org' , 3212
y = remote( host , port )

def reg( name , psw ):
    y.sendafter( 'choice:' , '0\n' )
    y.sendafter( 'name?' , name + '\n' )
    y.sendafter( 'password:' , psw + '\n' )
    y.recvuntil( 'token: ' )
    return y.recvline()

def lgn( name , psw , tok ):
    y.sendafter( 'choice:' , '1\n' )
    y.sendafter( 'token:' , tok + '\n' )
    y.sendafter( 'username:' , name + '\n' )
    y.sendafter( 'password:' , psw + '\n' )
    return
    



#o = reg( 'yuan' , 'aaaaaaaaaa' ) 
#log.success( o )


lgn( 'yuan' , 'aaaaaaaaaa' , 'Rx99N3Y3zZpeXJsDeqQaHfxYQc9Xpl2n8oqzQthccBaI+8uijd2dSrLqcN/McHqVU9yLILEin/6/PW+LRlWLKw=='  )




"""
token = 'Rx99N3Y3zZpeXJsDeqQaHfxYQc9Xpl2n8oqzQthccBbXWq9fAlAPezCrP64yaDOS'

for i in range( 2000 ):
    y = remote( host , port )
    tok , para = hashpumpy.hashpump( token , 'name=yuan&role=student&password=yass' , '&role=admin' , i )
    print tok , para
    lgn( 'yuan' , 'yass' , tok )
    o = y.recvline()
    log.success( '{} {}'.format( i , o ) )
    if b'QAQ' not in o:
        y.interactive()
        break
    y.close()
"""
y.interactive()

#name=aaaaaaaaaaa aaaaaaaaa&role=s tudent&password= admin           [48:64]
# vZ4rNRpfpwFZUP83L5Jigce1lFMKRtEeCbp9X3W7/Dn8WEHPV6Zdp/KKs0LYXHAWU9yLILEin/6/PW+LRlWLKw==

#name=aaaaaaaaaaa aaaaaaaaaa&role= student&password =a              [16:32] 
# vZ4rNRpfpwFZUP83L5JigYj7y6KN3Z1Ksupw38xwepV24mRvjDCs4aopIOB2u/UPxzCJzWUn2mqoOZlAU0pmJg==

#name=yuan&role=s tudent&password= aaaaaaaaaa                       [:32]
# Rx99N3Y3zZpeXJsDeqQaHfxYQc9Xpl2n8oqzQthccBaA/irutRA80R5dATPkMwul

#name=yuan&role=s tudent&password= aaaaaaaaaa&role= admin(padding)
# 


#6474253735e7ddb33933a323a0c357b0 b094f511e46049808b8157d64b6620b5 8bfc2c5ab03c997040d640c6afa6fb2f 

#name=yuawn&role= student&password =yass
#ZHQlNzXn3bM5M6MjoMNXC3biZG+MMKzhqikg4Ha79Q+v2v0nfDYWaUK0Erc+rMe0 [:16]





#name=yuan&role=student&password=yass
#Rx99N3Y3zZpeXJsDeqQaHfxYQc9Xpl2n8oqzQthccBbXWq9fAlAPezCrP64yaDOS 

#bd9e2b351a5fa715
#950ff372f926281a
#1656b8dad7272570
#adc23061ad41d9c9
#bc20ca88be235db1
#89fe571b7aa1f355
#2898edd276fc4b37
#4abbfebcd1e5
