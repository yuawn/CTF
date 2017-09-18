import re

# Bugs_Bunny{X0r_1s_fun}

a = '614140376d77342c5f41426007347d12577a22254f28'
b = '23342744323541423138393837462223242544502155'

a = re.findall( '..' , a )
b = re.findall( '..' , b )

flag = ''

for i in range( 22 ):
    flag += chr( int( a[i] , 16 ) ^ int( b[i] , 16 ) )

print flag