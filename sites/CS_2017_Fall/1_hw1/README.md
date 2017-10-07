# HW1
## hw1
* encrypt行為：
```C
a = ( i + 1 ) << ( i + 2 ) % 10
c = a * flag[i] + 9011
fwrite( c , 4 , 1 , enc_fd )
```
* decrypt回去：
```python=
#!/usr/bin/env python
from pwn import *
import re

# FLAG{Iost4SXskSmu53CbCAI5e52FBJkj1JKl}

en = open( 'enc' , 'r' ).read()

a = 0
flag = ''
for i in re.findall( '....' , en ):
    c = ( u32( i ) - 9011 ) / ( ( a + 1 ) << ( a + 2 ) % 10 )
    a = a + 1
    flag += chr( c )


print flag
```