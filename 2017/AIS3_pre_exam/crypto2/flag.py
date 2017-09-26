#!/usr/bin/env python3

from base64 import b64encode as b64e
from base64 import b64decode as b64d

'''
AES ECB
Weak ECB
plain text encrypted text one to one block
combine

ais3{ABCDEFGHIJKLMNOPQRSTUVWXYZZZZZZZ}
'''

'''
name=aaaaaaaaaaa aaaaaaaaa&role=s tudent&password= admin           [48:64]
vZ4rNRpfpwFZUP83L5Jigce1lFMKRtEeCbp9X3W7/Dn8WEHPV6Zdp/KKs0LYXHAWU9yLILEin/6/PW+LRlWLKw==

name=aaaaaaaaaaa aaaaaaaaaa&role= student&password =a              [16:32] 
vZ4rNRpfpwFZUP83L5JigYj7y6KN3Z1Ksupw38xwepV24mRvjDCs4aopIOB2u/UPxzCJzWUn2mqoOZlAU0pmJg==

name=yuan&role=s tudent&password= aaaaaaaaaa                       [:32]
Rx99N3Y3zZpeXJsDeqQaHfxYQc9Xpl2n8oqzQthccBaA/irutRA80R5dATPkMwul

name=yuan&role=s tudent&password= aaaaaaaaaa&role= admin(padding)
'''


ans = b64d('Rx99N3Y3zZpeXJsDeqQaHfxYQc9Xpl2n8oqzQthccBaA/irutRA80R5dATPkMwul')[:32] + b64d('vZ4rNRpfpwFZUP83L5JigYj7y6KN3Z1Ksupw38xwepV24mRvjDCs4aopIOB2u/UPxzCJzWUn2mqoOZlAU0pmJg==')[16:32] + b64d('vZ4rNRpfpwFZUP83L5Jigce1lFMKRtEeCbp9X3W7/Dn8WEHPV6Zdp/KKs0LYXHAWU9yLILEin/6/PW+LRlWLKw==')[48:64]
ans = b64e( ans )
print( ans )