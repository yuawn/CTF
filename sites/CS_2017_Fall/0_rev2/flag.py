import re

# FLAG{X0r_to_Cr4ck_M3}

'''
0x8b8d808a                                          ; XREF=sub_401000+181
004120c0         db  0xb7 ; '.'
004120c1         db  0x94 ; '.'
004120c2         db  0xfc ; '.'
004120c3         db  0xbe ; '.'
004120c4         db  0x93 ; '.'
004120c5         db  0xb8 ; '.'
004120c6         db  0xa3 ; '.'
004120c7         db  0x93 ; '.'
004120c8         db  0x8f ; '.'
004120c9         db  0xbe ; '.'
004120ca         db  0xf8 ; '.'
004120cb         db  0xaf ; '.'
004120cc         db  0xa7 ; '.'
004120cd         db  0x93 ; '.'
004120ce         db  0x81 ; '.'
004120cf         db  0xff ; '.'
004120d0         db  0xb1
'''

s = '8a808d8bb794fcbe93b8a3938fbef8afa79381ffb1'

print ''.join( chr( int( i , 16 ) ^ 0xcc ) for i in re.findall( '..' , s ) )
