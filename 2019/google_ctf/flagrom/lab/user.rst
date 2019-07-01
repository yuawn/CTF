                                      1 ;--------------------------------------------------------
                                      2 ; File Created by SDCC : free open source ANSI-C Compiler
                                      3 ; Version 3.5.0 #9253 (Apr  3 2018) (Linux)
                                      4 ; This file was generated Sat Jun 22 18:51:58 2019
                                      5 ;--------------------------------------------------------
                                      6 	.module user
                                      7 	.optsdcc -mmcs51 --model-small
                                      8 	
                                      9 ;--------------------------------------------------------
                                     10 ; Public variables in this module
                                     11 ;--------------------------------------------------------
                                     12 	.globl _SEEPROM_I2C_ADDR_SECURE
                                     13 	.globl _SEEPROM_I2C_ADDR_WRITE
                                     14 	.globl _SEEPROM_I2C_ADDR_READ
                                     15 	.globl _SEEPROM_I2C_ADDR_MEMORY
                                     16 	.globl _main
                                     17 	.globl _recv_ack
                                     18 	.globl _recv_byte
                                     19 	.globl _send_byte
                                     20 	.globl _send_bit
                                     21 	.globl _send_stop
                                     22 	.globl _send_start
                                     23 	.globl _seeprom_wait_until_idle
                                     24 	.globl _print
                                     25 	.globl _I2C_STATE
                                     26 	.globl _RAW_I2C_SDA
                                     27 	.globl _RAW_I2C_SCL
                                     28 	.globl _CHAROUT
                                     29 	.globl _DEBUG
                                     30 	.globl _POWEROFF
                                     31 	.globl _I2C_DATA
                                     32 	.globl _I2C_ERROR_CODE
                                     33 	.globl _I2C_RW_MASK
                                     34 	.globl _I2C_LENGTH
                                     35 	.globl _I2C_ADDR
                                     36 	.globl _FLAG
                                     37 ;--------------------------------------------------------
                                     38 ; special function registers
                                     39 ;--------------------------------------------------------
                                     40 	.area RSEG    (ABS,DATA)
      000000                         41 	.org 0x0000
                           0000FF    42 _POWEROFF	=	0x00ff
                           0000FE    43 _DEBUG	=	0x00fe
                           0000FD    44 _CHAROUT	=	0x00fd
                           0000FA    45 _RAW_I2C_SCL	=	0x00fa
                           0000FB    46 _RAW_I2C_SDA	=	0x00fb
                           0000FC    47 _I2C_STATE	=	0x00fc
                                     48 ;--------------------------------------------------------
                                     49 ; special function bits
                                     50 ;--------------------------------------------------------
                                     51 	.area RSEG    (ABS,DATA)
      000000                         52 	.org 0x0000
                                     53 ;--------------------------------------------------------
                                     54 ; overlayable register banks
                                     55 ;--------------------------------------------------------
                                     56 	.area REG_BANK_0	(REL,OVR,DATA)
      000000                         57 	.ds 8
                                     58 ;--------------------------------------------------------
                                     59 ; internal ram data
                                     60 ;--------------------------------------------------------
                                     61 	.area DSEG    (DATA)
                                     62 ;--------------------------------------------------------
                                     63 ; overlayable items in internal ram 
                                     64 ;--------------------------------------------------------
                                     65 	.area	OSEG    (OVR,DATA)
                                     66 	.area	OSEG    (OVR,DATA)
                                     67 	.area	OSEG    (OVR,DATA)
                                     68 	.area	OSEG    (OVR,DATA)
                                     69 ;--------------------------------------------------------
                                     70 ; Stack segment in internal ram 
                                     71 ;--------------------------------------------------------
                                     72 	.area	SSEG
      000008                         73 __start__stack:
      000008                         74 	.ds	1
                                     75 
                                     76 ;--------------------------------------------------------
                                     77 ; indirectly addressable internal ram data
                                     78 ;--------------------------------------------------------
                                     79 	.area ISEG    (DATA)
                                     80 ;--------------------------------------------------------
                                     81 ; absolute internal ram data
                                     82 ;--------------------------------------------------------
                                     83 	.area IABS    (ABS,DATA)
                                     84 	.area IABS    (ABS,DATA)
                                     85 ;--------------------------------------------------------
                                     86 ; bit data
                                     87 ;--------------------------------------------------------
                                     88 	.area BSEG    (BIT)
                                     89 ;--------------------------------------------------------
                                     90 ; paged external ram data
                                     91 ;--------------------------------------------------------
                                     92 	.area PSEG    (PAG,XDATA)
                                     93 ;--------------------------------------------------------
                                     94 ; external ram data
                                     95 ;--------------------------------------------------------
                                     96 	.area XSEG    (XDATA)
                           00FF00    97 _FLAG	=	0xff00
                           00FE00    98 _I2C_ADDR	=	0xfe00
                           00FE01    99 _I2C_LENGTH	=	0xfe01
                           00FE02   100 _I2C_RW_MASK	=	0xfe02
                           00FE03   101 _I2C_ERROR_CODE	=	0xfe03
                           00FE08   102 _I2C_DATA	=	0xfe08
                                    103 ;--------------------------------------------------------
                                    104 ; absolute external ram data
                                    105 ;--------------------------------------------------------
                                    106 	.area XABS    (ABS,XDATA)
                                    107 ;--------------------------------------------------------
                                    108 ; external initialized ram data
                                    109 ;--------------------------------------------------------
                                    110 	.area XISEG   (XDATA)
                                    111 	.area HOME    (CODE)
                                    112 	.area GSINIT0 (CODE)
                                    113 	.area GSINIT1 (CODE)
                                    114 	.area GSINIT2 (CODE)
                                    115 	.area GSINIT3 (CODE)
                                    116 	.area GSINIT4 (CODE)
                                    117 	.area GSINIT5 (CODE)
                                    118 	.area GSINIT  (CODE)
                                    119 	.area GSFINAL (CODE)
                                    120 	.area CSEG    (CODE)
                                    121 ;--------------------------------------------------------
                                    122 ; interrupt vector 
                                    123 ;--------------------------------------------------------
                                    124 	.area HOME    (CODE)
      000000                        125 __interrupt_vect:
      000000 02 00 06         [24]  126 	ljmp	__sdcc_gsinit_startup
                                    127 ;--------------------------------------------------------
                                    128 ; global & static initialisations
                                    129 ;--------------------------------------------------------
                                    130 	.area HOME    (CODE)
                                    131 	.area GSINIT  (CODE)
                                    132 	.area GSFINAL (CODE)
                                    133 	.area GSINIT  (CODE)
                                    134 	.globl __sdcc_gsinit_startup
                                    135 	.globl __sdcc_program_startup
                                    136 	.globl __start__stack
                                    137 	.globl __mcs51_genXINIT
                                    138 	.globl __mcs51_genXRAMCLEAR
                                    139 	.globl __mcs51_genRAMCLEAR
                                    140 	.area GSFINAL (CODE)
      00005F 02 00 03         [24]  141 	ljmp	__sdcc_program_startup
                                    142 ;--------------------------------------------------------
                                    143 ; Home
                                    144 ;--------------------------------------------------------
                                    145 	.area HOME    (CODE)
                                    146 	.area HOME    (CODE)
      000003                        147 __sdcc_program_startup:
      000003 02 01 42         [24]  148 	ljmp	_main
                                    149 ;	return from main will return to caller
                                    150 ;--------------------------------------------------------
                                    151 ; code
                                    152 ;--------------------------------------------------------
                                    153 	.area CSEG    (CODE)
                                    154 ;------------------------------------------------------------
                                    155 ;Allocation info for local variables in function 'print'
                                    156 ;------------------------------------------------------------
                                    157 ;str                       Allocated to registers 
                                    158 ;------------------------------------------------------------
                                    159 ;	user.c:22: void print(const char *str) {
                                    160 ;	-----------------------------------------
                                    161 ;	 function print
                                    162 ;	-----------------------------------------
      000062                        163 _print:
                           000007   164 	ar7 = 0x07
                           000006   165 	ar6 = 0x06
                           000005   166 	ar5 = 0x05
                           000004   167 	ar4 = 0x04
                           000003   168 	ar3 = 0x03
                           000002   169 	ar2 = 0x02
                           000001   170 	ar1 = 0x01
                           000000   171 	ar0 = 0x00
      000062 AD 82            [24]  172 	mov	r5,dpl
      000064 AE 83            [24]  173 	mov	r6,dph
      000066 AF F0            [24]  174 	mov	r7,b
                                    175 ;	user.c:23: while (*str) {
      000068                        176 00101$:
      000068 8D 82            [24]  177 	mov	dpl,r5
      00006A 8E 83            [24]  178 	mov	dph,r6
      00006C 8F F0            [24]  179 	mov	b,r7
      00006E 12 02 56         [24]  180 	lcall	__gptrget
      000071 FC               [12]  181 	mov	r4,a
      000072 60 09            [24]  182 	jz	00104$
                                    183 ;	user.c:24: CHAROUT = *str++;
      000074 8C FD            [24]  184 	mov	_CHAROUT,r4
      000076 0D               [12]  185 	inc	r5
      000077 BD 00 EE         [24]  186 	cjne	r5,#0x00,00101$
      00007A 0E               [12]  187 	inc	r6
      00007B 80 EB            [24]  188 	sjmp	00101$
      00007D                        189 00104$:
      00007D 22               [24]  190 	ret
                                    191 ;------------------------------------------------------------
                                    192 ;Allocation info for local variables in function 'seeprom_wait_until_idle'
                                    193 ;------------------------------------------------------------
                                    194 ;	user.c:28: void seeprom_wait_until_idle() {
                                    195 ;	-----------------------------------------
                                    196 ;	 function seeprom_wait_until_idle
                                    197 ;	-----------------------------------------
      00007E                        198 _seeprom_wait_until_idle:
                                    199 ;	user.c:29: while (I2C_STATE != 0) {}
      00007E                        200 00101$:
      00007E E5 FC            [12]  201 	mov	a,_I2C_STATE
      000080 70 FC            [24]  202 	jnz	00101$
      000082 22               [24]  203 	ret
                                    204 ;------------------------------------------------------------
                                    205 ;Allocation info for local variables in function 'send_start'
                                    206 ;------------------------------------------------------------
                                    207 ;	user.c:33: void send_start() {
                                    208 ;	-----------------------------------------
                                    209 ;	 function send_start
                                    210 ;	-----------------------------------------
      000083                        211 _send_start:
                                    212 ;	user.c:34: RAW_I2C_SCL = 0;
      000083 75 FA 00         [24]  213 	mov	_RAW_I2C_SCL,#0x00
                                    214 ;	user.c:35: RAW_I2C_SDA = 1;
      000086 75 FB 01         [24]  215 	mov	_RAW_I2C_SDA,#0x01
                                    216 ;	user.c:36: RAW_I2C_SCL = 1;
      000089 75 FA 01         [24]  217 	mov	_RAW_I2C_SCL,#0x01
                                    218 ;	user.c:37: RAW_I2C_SDA = 0;
      00008C 75 FB 00         [24]  219 	mov	_RAW_I2C_SDA,#0x00
      00008F 22               [24]  220 	ret
                                    221 ;------------------------------------------------------------
                                    222 ;Allocation info for local variables in function 'send_stop'
                                    223 ;------------------------------------------------------------
                                    224 ;	user.c:40: void send_stop() {
                                    225 ;	-----------------------------------------
                                    226 ;	 function send_stop
                                    227 ;	-----------------------------------------
      000090                        228 _send_stop:
                                    229 ;	user.c:41: RAW_I2C_SCL = 0;
      000090 75 FA 00         [24]  230 	mov	_RAW_I2C_SCL,#0x00
                                    231 ;	user.c:42: RAW_I2C_SDA = 0;
      000093 75 FB 00         [24]  232 	mov	_RAW_I2C_SDA,#0x00
                                    233 ;	user.c:43: RAW_I2C_SCL = 1;
      000096 75 FA 01         [24]  234 	mov	_RAW_I2C_SCL,#0x01
                                    235 ;	user.c:44: RAW_I2C_SDA = 1;
      000099 75 FB 01         [24]  236 	mov	_RAW_I2C_SDA,#0x01
      00009C 22               [24]  237 	ret
                                    238 ;------------------------------------------------------------
                                    239 ;Allocation info for local variables in function 'send_bit'
                                    240 ;------------------------------------------------------------
                                    241 ;a2                        Allocated to registers r7 
                                    242 ;------------------------------------------------------------
                                    243 ;	user.c:47: void send_bit(unsigned char a2) {
                                    244 ;	-----------------------------------------
                                    245 ;	 function send_bit
                                    246 ;	-----------------------------------------
      00009D                        247 _send_bit:
      00009D AF 82            [24]  248 	mov	r7,dpl
                                    249 ;	user.c:48: RAW_I2C_SCL = 0;
      00009F 75 FA 00         [24]  250 	mov	_RAW_I2C_SCL,#0x00
                                    251 ;	user.c:49: RAW_I2C_SDA = (a2 & 1) != 0;
      0000A2 53 07 01         [24]  252 	anl	ar7,#0x01
      0000A5 E4               [12]  253 	clr	a
      0000A6 BF 00 01         [24]  254 	cjne	r7,#0x00,00103$
      0000A9 04               [12]  255 	inc	a
      0000AA                        256 00103$:
      0000AA FF               [12]  257 	mov	r7,a
      0000AB B4 01 00         [24]  258 	cjne	a,#0x01,00105$
      0000AE                        259 00105$:
      0000AE E4               [12]  260 	clr	a
      0000AF 33               [12]  261 	rlc	a
      0000B0 F5 FB            [12]  262 	mov	_RAW_I2C_SDA,a
                                    263 ;	user.c:50: RAW_I2C_SCL = 1;
      0000B2 75 FA 01         [24]  264 	mov	_RAW_I2C_SCL,#0x01
      0000B5 22               [24]  265 	ret
                                    266 ;------------------------------------------------------------
                                    267 ;Allocation info for local variables in function 'send_byte'
                                    268 ;------------------------------------------------------------
                                    269 ;a2                        Allocated to registers r7 
                                    270 ;i                         Allocated to registers r5 r6 
                                    271 ;------------------------------------------------------------
                                    272 ;	user.c:53: void send_byte(unsigned char a2) {
                                    273 ;	-----------------------------------------
                                    274 ;	 function send_byte
                                    275 ;	-----------------------------------------
      0000B6                        276 _send_byte:
      0000B6 AF 82            [24]  277 	mov	r7,dpl
                                    278 ;	user.c:56: for ( i = 0; i <= 7; ++i ) {
      0000B8 7D 00            [12]  279 	mov	r5,#0x00
      0000BA 7E 00            [12]  280 	mov	r6,#0x00
      0000BC                        281 00102$:
                                    282 ;	user.c:57: RAW_I2C_SCL = 0;
      0000BC 75 FA 00         [24]  283 	mov	_RAW_I2C_SCL,#0x00
                                    284 ;	user.c:58: RAW_I2C_SDA = ((a2 >> (7 - i)) & 1) != 0;
      0000BF 74 07            [12]  285 	mov	a,#0x07
      0000C1 C3               [12]  286 	clr	c
      0000C2 9D               [12]  287 	subb	a,r5
      0000C3 FB               [12]  288 	mov	r3,a
      0000C4 E4               [12]  289 	clr	a
      0000C5 9E               [12]  290 	subb	a,r6
      0000C6 FC               [12]  291 	mov	r4,a
      0000C7 8B F0            [24]  292 	mov	b,r3
      0000C9 05 F0            [12]  293 	inc	b
      0000CB EF               [12]  294 	mov	a,r7
      0000CC 80 02            [24]  295 	sjmp	00111$
      0000CE                        296 00110$:
      0000CE C3               [12]  297 	clr	c
      0000CF 13               [12]  298 	rrc	a
      0000D0                        299 00111$:
      0000D0 D5 F0 FB         [24]  300 	djnz	b,00110$
      0000D3 54 01            [12]  301 	anl	a,#0x01
      0000D5 FC               [12]  302 	mov	r4,a
      0000D6 E4               [12]  303 	clr	a
      0000D7 BC 00 01         [24]  304 	cjne	r4,#0x00,00112$
      0000DA 04               [12]  305 	inc	a
      0000DB                        306 00112$:
      0000DB FC               [12]  307 	mov	r4,a
      0000DC B4 01 00         [24]  308 	cjne	a,#0x01,00114$
      0000DF                        309 00114$:
      0000DF E4               [12]  310 	clr	a
      0000E0 33               [12]  311 	rlc	a
      0000E1 F5 FB            [12]  312 	mov	_RAW_I2C_SDA,a
                                    313 ;	user.c:59: RAW_I2C_SCL = 1;
      0000E3 75 FA 01         [24]  314 	mov	_RAW_I2C_SCL,#0x01
                                    315 ;	user.c:56: for ( i = 0; i <= 7; ++i ) {
      0000E6 0D               [12]  316 	inc	r5
      0000E7 BD 00 01         [24]  317 	cjne	r5,#0x00,00115$
      0000EA 0E               [12]  318 	inc	r6
      0000EB                        319 00115$:
      0000EB C3               [12]  320 	clr	c
      0000EC 74 07            [12]  321 	mov	a,#0x07
      0000EE 9D               [12]  322 	subb	a,r5
      0000EF 74 80            [12]  323 	mov	a,#(0x00 ^ 0x80)
      0000F1 8E F0            [24]  324 	mov	b,r6
      0000F3 63 F0 80         [24]  325 	xrl	b,#0x80
      0000F6 95 F0            [12]  326 	subb	a,b
      0000F8 50 C2            [24]  327 	jnc	00102$
      0000FA 22               [24]  328 	ret
                                    329 ;------------------------------------------------------------
                                    330 ;Allocation info for local variables in function 'recv_byte'
                                    331 ;------------------------------------------------------------
                                    332 ;i                         Allocated to registers r5 r6 
                                    333 ;v3                        Allocated to registers r7 
                                    334 ;------------------------------------------------------------
                                    335 ;	user.c:63: unsigned char recv_byte() {
                                    336 ;	-----------------------------------------
                                    337 ;	 function recv_byte
                                    338 ;	-----------------------------------------
      0000FB                        339 _recv_byte:
                                    340 ;	user.c:67: v3 = 0;
      0000FB 7F 00            [12]  341 	mov	r7,#0x00
                                    342 ;	user.c:68: for ( i = 0; i <= 7; ++i ) {
      0000FD 7D 00            [12]  343 	mov	r5,#0x00
      0000FF 7E 00            [12]  344 	mov	r6,#0x00
      000101                        345 00102$:
                                    346 ;	user.c:69: RAW_I2C_SCL = 0;
      000101 75 FA 00         [24]  347 	mov	_RAW_I2C_SCL,#0x00
                                    348 ;	user.c:70: RAW_I2C_SCL = 1;
      000104 75 FA 01         [24]  349 	mov	_RAW_I2C_SCL,#0x01
                                    350 ;	user.c:71: v3 = (v3 << 1) | ((RAW_I2C_SDA & 1) != 0);
      000107 EF               [12]  351 	mov	a,r7
      000108 2F               [12]  352 	add	a,r7
      000109 FC               [12]  353 	mov	r4,a
      00010A 74 01            [12]  354 	mov	a,#0x01
      00010C 55 FB            [12]  355 	anl	a,_RAW_I2C_SDA
      00010E FB               [12]  356 	mov	r3,a
      00010F E4               [12]  357 	clr	a
      000110 BB 00 01         [24]  358 	cjne	r3,#0x00,00113$
      000113 04               [12]  359 	inc	a
      000114                        360 00113$:
      000114 FB               [12]  361 	mov	r3,a
      000115 B4 01 00         [24]  362 	cjne	a,#0x01,00115$
      000118                        363 00115$:
      000118 E4               [12]  364 	clr	a
      000119 33               [12]  365 	rlc	a
      00011A FB               [12]  366 	mov	r3,a
      00011B 4C               [12]  367 	orl	a,r4
      00011C FF               [12]  368 	mov	r7,a
                                    369 ;	user.c:68: for ( i = 0; i <= 7; ++i ) {
      00011D 0D               [12]  370 	inc	r5
      00011E BD 00 01         [24]  371 	cjne	r5,#0x00,00116$
      000121 0E               [12]  372 	inc	r6
      000122                        373 00116$:
      000122 C3               [12]  374 	clr	c
      000123 74 07            [12]  375 	mov	a,#0x07
      000125 9D               [12]  376 	subb	a,r5
      000126 74 80            [12]  377 	mov	a,#(0x00 ^ 0x80)
      000128 8E F0            [24]  378 	mov	b,r6
      00012A 63 F0 80         [24]  379 	xrl	b,#0x80
      00012D 95 F0            [12]  380 	subb	a,b
      00012F 50 D0            [24]  381 	jnc	00102$
                                    382 ;	user.c:73: return v3;
      000131 8F 82            [24]  383 	mov	dpl,r7
      000133 22               [24]  384 	ret
                                    385 ;------------------------------------------------------------
                                    386 ;Allocation info for local variables in function 'recv_ack'
                                    387 ;------------------------------------------------------------
                                    388 ;	user.c:76: unsigned char recv_ack() {
                                    389 ;	-----------------------------------------
                                    390 ;	 function recv_ack
                                    391 ;	-----------------------------------------
      000134                        392 _recv_ack:
                                    393 ;	user.c:77: RAW_I2C_SCL = 0;
      000134 75 FA 00         [24]  394 	mov	_RAW_I2C_SCL,#0x00
                                    395 ;	user.c:78: RAW_I2C_SCL = 1;
                                    396 ;	user.c:79: return (((unsigned char)RAW_I2C_SDA) & 1 != 0) ^ 1;
      000137 74 01            [12]  397 	mov	a,#0x01
      000139 F5 FA            [12]  398 	mov	_RAW_I2C_SCL,a
      00013B 55 FB            [12]  399 	anl	a,_RAW_I2C_SDA
      00013D 64 01            [12]  400 	xrl	a,#0x01
      00013F F5 82            [12]  401 	mov	dpl,a
      000141 22               [24]  402 	ret
                                    403 ;------------------------------------------------------------
                                    404 ;Allocation info for local variables in function 'main'
                                    405 ;------------------------------------------------------------
                                    406 ;i                         Allocated to registers r6 r7 
                                    407 ;c                         Allocated to registers r5 
                                    408 ;------------------------------------------------------------
                                    409 ;	user.c:82: void main(void) {
                                    410 ;	-----------------------------------------
                                    411 ;	 function main
                                    412 ;	-----------------------------------------
      000142                        413 _main:
                                    414 ;	user.c:85: print("Hello World\n");
      000142 90 02 7E         [24]  415 	mov	dptr,#___str_0
      000145 75 F0 80         [24]  416 	mov	b,#0x80
      000148 12 00 62         [24]  417 	lcall	_print
                                    418 ;	user.c:86: seeprom_wait_until_idle();
      00014B 12 00 7E         [24]  419 	lcall	_seeprom_wait_until_idle
                                    420 ;	user.c:88: print("start\n");
      00014E 90 02 8B         [24]  421 	mov	dptr,#___str_1
      000151 75 F0 80         [24]  422 	mov	b,#0x80
      000154 12 00 62         [24]  423 	lcall	_print
                                    424 ;	user.c:89: send_start();
      000157 12 00 83         [24]  425 	lcall	_send_start
                                    426 ;	user.c:91: print("op load_address\n");
      00015A 90 02 92         [24]  427 	mov	dptr,#___str_2
      00015D 75 F0 80         [24]  428 	mov	b,#0x80
      000160 12 00 62         [24]  429 	lcall	_print
                                    430 ;	user.c:92: send_byte(SEEPROM_I2C_ADDR_WRITE);
      000163 90 02 7A         [24]  431 	mov	dptr,#_SEEPROM_I2C_ADDR_WRITE
      000166 E4               [12]  432 	clr	a
      000167 93               [24]  433 	movc	a,@a+dptr
      000168 FE               [12]  434 	mov	r6,a
      000169 74 01            [12]  435 	mov	a,#0x01
      00016B 93               [24]  436 	movc	a,@a+dptr
      00016C 8E 82            [24]  437 	mov	dpl,r6
      00016E 12 00 B6         [24]  438 	lcall	_send_byte
                                    439 ;	user.c:93: if (!recv_ack()) { print("failed 0\n"); goto end; }
      000171 12 01 34         [24]  440 	lcall	_recv_ack
      000174 E5 82            [12]  441 	mov	a,dpl
      000176 70 0C            [24]  442 	jnz	00102$
      000178 90 02 A3         [24]  443 	mov	dptr,#___str_3
      00017B 75 F0 80         [24]  444 	mov	b,#0x80
      00017E 12 00 62         [24]  445 	lcall	_print
      000181 02 02 52         [24]  446 	ljmp	00112$
      000184                        447 00102$:
                                    448 ;	user.c:95: print("addr 0\n");
      000184 90 02 AD         [24]  449 	mov	dptr,#___str_4
      000187 75 F0 80         [24]  450 	mov	b,#0x80
      00018A 12 00 62         [24]  451 	lcall	_print
                                    452 ;	user.c:96: send_byte(0);
      00018D 75 82 00         [24]  453 	mov	dpl,#0x00
      000190 12 00 B6         [24]  454 	lcall	_send_byte
                                    455 ;	user.c:97: if (!recv_ack()) { print("failed 1\n"); goto end; }
      000193 12 01 34         [24]  456 	lcall	_recv_ack
      000196 E5 82            [12]  457 	mov	a,dpl
      000198 70 0C            [24]  458 	jnz	00104$
      00019A 90 02 B5         [24]  459 	mov	dptr,#___str_5
      00019D 75 F0 80         [24]  460 	mov	b,#0x80
      0001A0 12 00 62         [24]  461 	lcall	_print
      0001A3 02 02 52         [24]  462 	ljmp	00112$
      0001A6                        463 00104$:
                                    464 ;	user.c:99: print("restart\n");
      0001A6 90 02 BF         [24]  465 	mov	dptr,#___str_6
      0001A9 75 F0 80         [24]  466 	mov	b,#0x80
      0001AC 12 00 62         [24]  467 	lcall	_print
                                    468 ;	user.c:100: send_start();
      0001AF 12 00 83         [24]  469 	lcall	_send_start
                                    470 ;	user.c:101: print("op secure\n");
      0001B2 90 02 C8         [24]  471 	mov	dptr,#___str_7
      0001B5 75 F0 80         [24]  472 	mov	b,#0x80
      0001B8 12 00 62         [24]  473 	lcall	_print
                                    474 ;	user.c:102: send_byte(SEEPROM_I2C_ADDR_SECURE | 0b1111);
      0001BB 90 02 7C         [24]  475 	mov	dptr,#_SEEPROM_I2C_ADDR_SECURE
      0001BE E4               [12]  476 	clr	a
      0001BF 93               [24]  477 	movc	a,@a+dptr
      0001C0 FE               [12]  478 	mov	r6,a
      0001C1 74 01            [12]  479 	mov	a,#0x01
      0001C3 93               [24]  480 	movc	a,@a+dptr
      0001C4 43 06 0F         [24]  481 	orl	ar6,#0x0F
      0001C7 8E 82            [24]  482 	mov	dpl,r6
      0001C9 12 00 B6         [24]  483 	lcall	_send_byte
                                    484 ;	user.c:103: if (!recv_ack()) { print("failed 2\n"); goto end; }
      0001CC 12 01 34         [24]  485 	lcall	_recv_ack
      0001CF E5 82            [12]  486 	mov	a,dpl
      0001D1 70 0B            [24]  487 	jnz	00106$
      0001D3 90 02 D3         [24]  488 	mov	dptr,#___str_8
      0001D6 75 F0 80         [24]  489 	mov	b,#0x80
      0001D9 12 00 62         [24]  490 	lcall	_print
      0001DC 80 74            [24]  491 	sjmp	00112$
      0001DE                        492 00106$:
                                    493 ;	user.c:105: print("restart 2\n");
      0001DE 90 02 DD         [24]  494 	mov	dptr,#___str_9
      0001E1 75 F0 80         [24]  495 	mov	b,#0x80
      0001E4 12 00 62         [24]  496 	lcall	_print
                                    497 ;	user.c:106: send_start();
      0001E7 12 00 83         [24]  498 	lcall	_send_start
                                    499 ;	user.c:108: print("op read\n");
      0001EA 90 02 E8         [24]  500 	mov	dptr,#___str_10
      0001ED 75 F0 80         [24]  501 	mov	b,#0x80
      0001F0 12 00 62         [24]  502 	lcall	_print
                                    503 ;	user.c:109: send_byte(SEEPROM_I2C_ADDR_READ);
      0001F3 90 02 78         [24]  504 	mov	dptr,#_SEEPROM_I2C_ADDR_READ
      0001F6 E4               [12]  505 	clr	a
      0001F7 93               [24]  506 	movc	a,@a+dptr
      0001F8 FE               [12]  507 	mov	r6,a
      0001F9 74 01            [12]  508 	mov	a,#0x01
      0001FB 93               [24]  509 	movc	a,@a+dptr
      0001FC 8E 82            [24]  510 	mov	dpl,r6
      0001FE 12 00 B6         [24]  511 	lcall	_send_byte
                                    512 ;	user.c:110: if (!recv_ack()) { print("failed 3\n"); goto end; }
      000201 12 01 34         [24]  513 	lcall	_recv_ack
      000204 E5 82            [12]  514 	mov	a,dpl
      000206 70 0B            [24]  515 	jnz	00122$
      000208 90 02 F1         [24]  516 	mov	dptr,#___str_11
      00020B 75 F0 80         [24]  517 	mov	b,#0x80
      00020E 12 00 62         [24]  518 	lcall	_print
                                    519 ;	user.c:112: for (i=0; i<256; i++) {
      000211 80 3F            [24]  520 	sjmp	00112$
      000213                        521 00122$:
      000213 7E 00            [12]  522 	mov	r6,#0x00
      000215 7F 00            [12]  523 	mov	r7,#0x00
      000217                        524 00113$:
                                    525 ;	user.c:113: c = recv_byte();
      000217 C0 07            [24]  526 	push	ar7
      000219 C0 06            [24]  527 	push	ar6
      00021B 12 00 FB         [24]  528 	lcall	_recv_byte
      00021E AD 82            [24]  529 	mov	r5,dpl
                                    530 ;	user.c:114: if (!recv_ack()) { print("failed read\n"); goto end; }
      000220 C0 05            [24]  531 	push	ar5
      000222 12 01 34         [24]  532 	lcall	_recv_ack
      000225 E5 82            [12]  533 	mov	a,dpl
      000227 D0 05            [24]  534 	pop	ar5
      000229 D0 06            [24]  535 	pop	ar6
      00022B D0 07            [24]  536 	pop	ar7
      00022D 70 0B            [24]  537 	jnz	00110$
      00022F 90 02 FB         [24]  538 	mov	dptr,#___str_12
      000232 75 F0 80         [24]  539 	mov	b,#0x80
      000235 12 00 62         [24]  540 	lcall	_print
      000238 80 18            [24]  541 	sjmp	00112$
      00023A                        542 00110$:
                                    543 ;	user.c:115: CHAROUT = c;
      00023A 8D FD            [24]  544 	mov	_CHAROUT,r5
                                    545 ;	user.c:112: for (i=0; i<256; i++) {
      00023C 0E               [12]  546 	inc	r6
      00023D BE 00 01         [24]  547 	cjne	r6,#0x00,00143$
      000240 0F               [12]  548 	inc	r7
      000241                        549 00143$:
      000241 C3               [12]  550 	clr	c
      000242 EF               [12]  551 	mov	a,r7
      000243 64 80            [12]  552 	xrl	a,#0x80
      000245 94 81            [12]  553 	subb	a,#0x81
      000247 40 CE            [24]  554 	jc	00113$
                                    555 ;	user.c:117: print("\n");
      000249 90 03 08         [24]  556 	mov	dptr,#___str_13
      00024C 75 F0 80         [24]  557 	mov	b,#0x80
      00024F 12 00 62         [24]  558 	lcall	_print
                                    559 ;	user.c:119: end:
      000252                        560 00112$:
                                    561 ;	user.c:120: POWEROFF = 1;
      000252 75 FF 01         [24]  562 	mov	_POWEROFF,#0x01
      000255 22               [24]  563 	ret
                                    564 	.area CSEG    (CODE)
                                    565 	.area CONST   (CODE)
      000276                        566 _SEEPROM_I2C_ADDR_MEMORY:
      000276 A0 00                  567 	.byte #0xA0,#0x00	;  160
      000278                        568 _SEEPROM_I2C_ADDR_READ:
      000278 A1 00                  569 	.byte #0xA1,#0x00	;  161
      00027A                        570 _SEEPROM_I2C_ADDR_WRITE:
      00027A A0 00                  571 	.byte #0xA0,#0x00	;  160
      00027C                        572 _SEEPROM_I2C_ADDR_SECURE:
      00027C 50 00                  573 	.byte #0x50,#0x00	;  80
      00027E                        574 ___str_0:
      00027E 48 65 6C 6C 6F 20 57   575 	.ascii "Hello World"
             6F 72 6C 64
      000289 0A                     576 	.db 0x0A
      00028A 00                     577 	.db 0x00
      00028B                        578 ___str_1:
      00028B 73 74 61 72 74         579 	.ascii "start"
      000290 0A                     580 	.db 0x0A
      000291 00                     581 	.db 0x00
      000292                        582 ___str_2:
      000292 6F 70 20 6C 6F 61 64   583 	.ascii "op load_address"
             5F 61 64 64 72 65 73
             73
      0002A1 0A                     584 	.db 0x0A
      0002A2 00                     585 	.db 0x00
      0002A3                        586 ___str_3:
      0002A3 66 61 69 6C 65 64 20   587 	.ascii "failed 0"
             30
      0002AB 0A                     588 	.db 0x0A
      0002AC 00                     589 	.db 0x00
      0002AD                        590 ___str_4:
      0002AD 61 64 64 72 20 30      591 	.ascii "addr 0"
      0002B3 0A                     592 	.db 0x0A
      0002B4 00                     593 	.db 0x00
      0002B5                        594 ___str_5:
      0002B5 66 61 69 6C 65 64 20   595 	.ascii "failed 1"
             31
      0002BD 0A                     596 	.db 0x0A
      0002BE 00                     597 	.db 0x00
      0002BF                        598 ___str_6:
      0002BF 72 65 73 74 61 72 74   599 	.ascii "restart"
      0002C6 0A                     600 	.db 0x0A
      0002C7 00                     601 	.db 0x00
      0002C8                        602 ___str_7:
      0002C8 6F 70 20 73 65 63 75   603 	.ascii "op secure"
             72 65
      0002D1 0A                     604 	.db 0x0A
      0002D2 00                     605 	.db 0x00
      0002D3                        606 ___str_8:
      0002D3 66 61 69 6C 65 64 20   607 	.ascii "failed 2"
             32
      0002DB 0A                     608 	.db 0x0A
      0002DC 00                     609 	.db 0x00
      0002DD                        610 ___str_9:
      0002DD 72 65 73 74 61 72 74   611 	.ascii "restart 2"
             20 32
      0002E6 0A                     612 	.db 0x0A
      0002E7 00                     613 	.db 0x00
      0002E8                        614 ___str_10:
      0002E8 6F 70 20 72 65 61 64   615 	.ascii "op read"
      0002EF 0A                     616 	.db 0x0A
      0002F0 00                     617 	.db 0x00
      0002F1                        618 ___str_11:
      0002F1 66 61 69 6C 65 64 20   619 	.ascii "failed 3"
             33
      0002F9 0A                     620 	.db 0x0A
      0002FA 00                     621 	.db 0x00
      0002FB                        622 ___str_12:
      0002FB 66 61 69 6C 65 64 20   623 	.ascii "failed read"
             72 65 61 64
      000306 0A                     624 	.db 0x0A
      000307 00                     625 	.db 0x00
      000308                        626 ___str_13:
      000308 0A                     627 	.db 0x0A
      000309 00                     628 	.db 0x00
                                    629 	.area XINIT   (CODE)
                                    630 	.area CABS    (ABS,CODE)
