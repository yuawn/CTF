#!/usr/bin/env python
from pwn import *
import re , os

e = open( './elf' ).read()

dump = re.findall( '\x01\xd0(.....)' , e , re.DOTALL )
dump = [ (i[0] , u32(i[1:])) for i in dump ]
#print dump  , len( dump  )

code = '''#!/usr/bin/env python
from ctypes import *
from z3 import *
ans , a , b = 0 , 0 , 0

'''

f = '''
__int64 sub_4008B4()
{
  __int64 result; // rax

  result = (unsigned int)(b + a + ans + 274999);
  ans += b + a + 274999;
  return result;
}
nt64 sub_4008DC()
{
  __int64 result; // rax

  result = (unsigned int)(a - b + ans + 707020);
  ans += a - b + 707020;
  return result;
}
__int64 sub_400904()
{
  __int64 result; // rax

  result = (unsigned int)(b + a + ans - 192605);
  ans = b + a + ans - 192605;
  return result;
}
int64 sub_40092C()
{
  __int64 result; // rax

  result = (unsigned int)(a - b + ans + 642612);
  ans += a - b + 642612;
  return result;
}
_int64 sub_400954()
{
  __int64 result; // rax

  result = (unsigned int)(b + a + ans - 204677);
  ans = b + a + ans - 204677;
  return result;
}
__int64 sub_40097C()
{
  __int64 result; // rax

  result = (unsigned int)(b + a + ans - 652696);
  ans = b + a + ans - 652696;
  return result;
}
__int64 sub_4009A4()
{
  __int64 result; // rax

  result = (unsigned int)(a - b + ans - 772264);
  ans = a - b + ans - 772264;
  return result;
}
__int64 sub_4009CC()
{
  __int64 result; // rax

  result = (unsigned int)(b + a + ans - 244530);
  ans = b + a + ans - 244530;
  return result;
}
__int64 sub_4009F4()
{
  __int64 result; // rax

  result = (unsigned int)(a - b + ans + 73570);
  ans += a - b + 73570;
  return result;
}
_int64 sub_400A1C()
{
  __int64 result; // rax

  result = (unsigned int)(b + a + ans - 231243);
  ans = b + a + ans - 231243;
  return result;
}
__int64 sub_400A44()
{
  __int64 result; // rax

  result = (unsigned int)(a - b + ans - 930879);
  ans = a - b + ans - 930879;
  return result;
}
_int64 sub_400A6C()
{
  __int64 result; // rax

  result = (unsigned int)(b + a + ans - 34927);
  ans = b + a + ans - 34927;
  return result;
}
__int64 sub_400A94()
{
  __int64 result; // rax

  result = (unsigned int)(a - b + ans - 533566);
  ans = a - b + ans - 533566;
  return result;
}
__int64 sub_400ABC()
{
  __int64 result; // rax

  result = (unsigned int)(b + a + ans + 78742);
  ans += b + a + 78742;
  return result;
}
__int64 sub_400AE4()
{
  __int64 result; // rax

  result = (unsigned int)(b + a + ans + 394997);
  ans += b + a + 394997;
  return result;
}
__int64 sub_400B0C()
{
  __int64 result; // rax

  result = (unsigned int)(a - b + ans + 770045);
  ans += a - b + 770045;
  retu

__int64 sub_400B34()
{
  __int64 result; // rax

  result = (unsigned int)(a - b + ans + 599838);
  ans += a - b + 599838;
  return result;
}
_int64 sub_400B5C()
{
  __int64 result; // rax

  result = (unsigned int)(a - b + ans + 89598);
  ans += a - b + 89598;
  return result;
}
__int64 sub_400B84()
{
  __int64 result; // rax

  result = (unsigned int)(a - b + ans - 1047610);
  ans = a - b + ans - 1047610;
  return result;
}
_int64 sub_400BAC()
{
  __int64 result; // rax

  result = (unsigned int)(b + a + ans + 252336);
  ans += b + a + 252336;
  return result;
}


'''

f_name = re.findall( '64 (.*)\(' , f )
c = re.findall( ';\n  (.*);' , f )

for i in range( len( f_name ) ):
    o = c[i].split( ' ' )
    code += '''
def %s():
    global ans , a , b
    %s
    %s
    %s
''' % ( f_name[i] , 'a -= 1' if o[ o.index('a') - 1 ] == '-' else 'a += 1' , 'b -= 1' if o[ o.index('b') - 1 ] == '-' else 'b += 1' , 'ans -= %d' % dump[i][1] if dump[i][0] == '-' else 'ans += %d' % dump[i][1] )



sw = '''
 {
      case 1:
        sub_400BAC();
        break;
      case 2:
        sub_400B84();
        break;
      case 3:
        sub_400B5C();
        break;
      case 4:
        sub_400B34();
        break;
      case 5:
        sub_400B0C();
        break;
      case 6:
        sub_400AE4();
        break;
      case 7:
        sub_400ABC();
        break;
      case 8:
        sub_400A94();
        break;
      case 9:
        sub_400A6C();
        break;
      case 10:
        sub_400A44();
        break;
      case 11:
        sub_400A1C();
        break;
      case 12:
        sub_4009F4();
        break;
      case 13:
        sub_4009CC();
        break;
      case 14:
        sub_4009A4();
        break;
      case 15:
        sub_40097C();
        break;
      case 16:
        sub_400954();
        break;
      case 17:
        sub_40092C();
        break;
      case 18:
        sub_400904();
        break;
      case 19:
        sub_4008DC();
        break;
      case 20:
        sub_4008B4();
        break;
      default:
        puts("You cannot be here. Absolutely!!");
        exit(0);
        return result;
'''

ar = [ u32( i ) for i in re.findall( '\xc7\x45.(....)' , e , re.DOTALL )[2:22] ]

code += '''
v = %s

for i in v:
''' % str( ar )


for i , f in enumerate( re.findall( '(sub_.*)\(' , sw ) ):
    code +='''
    if i == %d:
        %s()
    ''' % ( i + 1 , f )


#print hex( u32( re.findall( '\xc7\x45\xfc(....)' , e )[0] ) )

#print re.findall( '\xc7\x45\xfc(....)' , e )[0]

code += '''
final = c_int( %s ).value
print a , b , ans
print ( final - ans ) %s 20

n1 = BitVec("num1",32)
n2 = BitVec("num2",32)

s = Solver()

s.add( n1 * a + n2 * b + ans == final )

print s.check()

print s.model()[n1].as_long()
print s.model()[n2].as_long()
''' % ( hex( u32( re.findall( '\xc7\x45\xfc(....)' , e )[0] ) ) , '%' )


print code

os.system( 'chmod +x ./tmp.py' )