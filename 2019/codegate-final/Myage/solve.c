#include <stdint.h>
#include <string.h>


unsigned int a , b , ans;


uint64_t sub_4008B4()
{
  uint64_t result; // rax

  result = (unsigned int)(b + a + ans + 540945);
  ans += b + a + 540945;
  return result;
}

uint64_t sub_4008DC()
{
  uint64_t result; // rax

  result = (unsigned int)(a - b + ans + 743330);
  ans += a - b + 743330;
  return result;
}

uint64_t sub_400904()
{
  uint64_t result; // rax

  result = (unsigned int)(b + a + ans - 1028044);
  ans = b + a + ans - 1028044;
  return result;
}

uint64_t sub_40092C()
{
  uint64_t result; // rax

  result = (unsigned int)(a - b + ans + 771649);
  ans += a - b + 771649;
  return result;
}

uint64_t sub_400954()
{
  uint64_t result; // rax

  result = (unsigned int)(b + a + ans - 761028);
  ans = b + a + ans - 761028;
  return result;
}

uint64_t sub_40097C()
{
  uint64_t result; // rax

  result = (unsigned int)(b + a + ans - 79117);
  ans = b + a + ans - 79117;
  return result;
}

uint64_t sub_4009A4()
{
  uint64_t result; // rax

  result = (unsigned int)(a - b + ans - 392458);
  ans = a - b + ans - 392458;
  return result;
}

uint64_t sub_4009CC()
{
  uint64_t result; // rax

  result = (unsigned int)(b + a + ans - 1017446);
  ans = b + a + ans - 1017446;
  return result;
}

uint64_t sub_4009F4()
{
  uint64_t result; // rax

  result = (unsigned int)(a - b + ans + 105555);
  ans += a - b + 105555;
  return result;
}

uint64_t sub_400A1C()
{
  uint64_t result; // rax

  result = (unsigned int)(b + a + ans - 181559);
  ans = b + a + ans - 181559;
  return result;
}

uint64_t sub_400A44()
{
  uint64_t result; // rax

  result = (unsigned int)(a - b + ans - 163035);
  ans = a - b + ans - 163035;
  return result;
}

uint64_t sub_400A6C()
{
  uint64_t result; // rax

  result = (unsigned int)(b + a + ans - 1029972);
  ans = b + a + ans - 1029972;
  return result;
}

uint64_t sub_400A94()
{
  uint64_t result; // rax

  result = (unsigned int)(a - b + ans - 831715);
  ans = a - b + ans - 831715;
  return result;
}

uint64_t sub_400ABC()
{
  uint64_t result; // rax

  result = (unsigned int)(b + a + ans + 972836);
  ans += b + a + 972836;
  return result;
}

uint64_t sub_400AE4()
{
  uint64_t result; // rax

  result = (unsigned int)(b + a + ans + 214648);
  ans += b + a + 214648;
  return result;
}

uint64_t sub_400B0C()
{
  uint64_t result; // rax

  result = (unsigned int)(a - b + ans + 810227);
  ans += a - b + 810227;
  return result;
}

uint64_t sub_400B34()
{
  uint64_t result; // rax

  result = (unsigned int)(a - b + ans + 899067);
  ans += a - b + 899067;
  return result;
}

uint64_t sub_400B5C()
{
  uint64_t result; // rax

  result = (unsigned int)(a - b + ans + 370723);
  ans += a - b + 370723;
  return result;
}

uint64_t sub_400B84()
{
  uint64_t result; // rax

  result = (unsigned int)(a - b + ans - 663606);
  ans = a - b + ans - 663606;
  return result;
}

uint64_t sub_400BAC()
{
  uint64_t result; // rax

  result = (unsigned int)(b + a + ans + 913033);
  ans += b + a + 913033;
  return result;
}


void sub_400BD4()
{
  


  int v[20] = { 20 , 4 , 3 , 7 , 11 , 6 , 7 , 8 , 5 , 18 , 20 , 8 , 12 , 17 , 18 , 19 , 6 , 7 , 12 , 13 };

  for ( int i = 0; i <= 19; ++i )
  {
    switch ( v[i] )
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
        return;
    }
  }
}

int main(int argc, char *argv[])
{

    klee_make_symbolic(&a, 4, "a");
    klee_make_symbolic(&b, 4, "b");

    sub_400BD4();
    
    if( ans == 1945331996 )
        klee_assert(0);

    return 0;
}