#!/usr/bin/env python
import re

# AIS3{tHere_1s_a_VErY_VerY_VeRY_1OoO00O0oO0OOoO0Oo000OOoO00o00oG_f1@g_iN_my_m1Nd}


s = '''
000000000201020 secret          dd 312Fh, 0E07h, 13BFh, 1BBFh, 257Fh, 477h, 4DFh, 2177h
.data:0000000000201020                 dd 38F7h, 79Fh, 38F7h, 17Fh, 2437h, 398Fh, 391Fh, 537h
.data:0000000000201020                 dd 2D2Fh, 31B7h, 1B3Fh, 2AF7h, 1C4Fh, 196Fh, 38DFh, 0E07h
.data:0000000000201020                 dd 1047h, 2F17h, 15AFh, 1F1Fh, 3787h, 0F6Fh, 15FFh, 15D7h
.data:0000000000201020                 dd 1F27h, 1117h, 1ADFh, 2FD7h, 1BC7h, 1D47h, 3B57h, 15E7h
.data:0000000000201020                 dd 0C4Fh, 3457h, 3AFh, 379Fh, 1F17h, 244Fh, 298Fh, 0E97h
.data:0000000000201020                 dd 79Fh, 1Fh, 1EE7h, 222Fh, 5DFh, 1E47h, 3177h, 18EFh
.data:0000000000201020                 dd 35FFh, 32EFh, 35B7h, 1417h, 87h, 0DBFh, 2BF7h, 1DAFh
.data:0000000000201020                 dd 8BFh, 2D3Fh, 35EFh, 268Fh, 34CFh, 30DFh, 24DFh, 2C4Fh
.data:0000000000201020                 dd 1807h, 2BBFh, 2777h, 326Fh, 3987h, 35AFh, 2B27h, 3E17h
.data:0000000000201020                 dd 23B7h, 31DFh, 227Fh, 2B5Fh, 0F0Fh
'''

r = '''
1637
502
549
837
1237
249
210
1096
1903
151
1858
31
1270
1903
1859
250
1522
1648
788
1284
983
890
1919
461
606
1470
738
903
1725
437
737
648
940
590
789
1481
839
1000
1881
724
455
1721
59
1725
910
1223
1280
414
157
50
1003
1140
245
904
1602
851
1678
1644
1754
689
63
473
1338
1003
368
1431
1788
1207
1735
1651
1236
1495
658
1295
1202
1569
1822
1786
1287
1980
1141
1594
1102
1386
480
'''

pool = re.findall( '([0-9A-Z]*)h' , s )
rnd = re.findall( '([0-9]+)\n' , r )

flag = ''
for c , r in zip( pool , rnd ):
    flag += chr( ((((int( c , 16 ) + 5) >> 1) - 10) >> 2) ^ int( r ) )

print flag