;--------------------------------------------------------
; File Created by SDCC : free open source ANSI-C Compiler
; Version 3.5.0 #9253 (Apr  3 2018) (Linux)
; This file was generated Sat Jun 22 18:51:58 2019
;--------------------------------------------------------
	.module user
	.optsdcc -mmcs51 --model-small
	
;--------------------------------------------------------
; Public variables in this module
;--------------------------------------------------------
	.globl _SEEPROM_I2C_ADDR_SECURE
	.globl _SEEPROM_I2C_ADDR_WRITE
	.globl _SEEPROM_I2C_ADDR_READ
	.globl _SEEPROM_I2C_ADDR_MEMORY
	.globl _main
	.globl _recv_ack
	.globl _recv_byte
	.globl _send_byte
	.globl _send_bit
	.globl _send_stop
	.globl _send_start
	.globl _seeprom_wait_until_idle
	.globl _print
	.globl _I2C_STATE
	.globl _RAW_I2C_SDA
	.globl _RAW_I2C_SCL
	.globl _CHAROUT
	.globl _DEBUG
	.globl _POWEROFF
	.globl _I2C_DATA
	.globl _I2C_ERROR_CODE
	.globl _I2C_RW_MASK
	.globl _I2C_LENGTH
	.globl _I2C_ADDR
	.globl _FLAG
;--------------------------------------------------------
; special function registers
;--------------------------------------------------------
	.area RSEG    (ABS,DATA)
	.org 0x0000
_POWEROFF	=	0x00ff
_DEBUG	=	0x00fe
_CHAROUT	=	0x00fd
_RAW_I2C_SCL	=	0x00fa
_RAW_I2C_SDA	=	0x00fb
_I2C_STATE	=	0x00fc
;--------------------------------------------------------
; special function bits
;--------------------------------------------------------
	.area RSEG    (ABS,DATA)
	.org 0x0000
;--------------------------------------------------------
; overlayable register banks
;--------------------------------------------------------
	.area REG_BANK_0	(REL,OVR,DATA)
	.ds 8
;--------------------------------------------------------
; internal ram data
;--------------------------------------------------------
	.area DSEG    (DATA)
;--------------------------------------------------------
; overlayable items in internal ram 
;--------------------------------------------------------
	.area	OSEG    (OVR,DATA)
	.area	OSEG    (OVR,DATA)
	.area	OSEG    (OVR,DATA)
	.area	OSEG    (OVR,DATA)
;--------------------------------------------------------
; Stack segment in internal ram 
;--------------------------------------------------------
	.area	SSEG
__start__stack:
	.ds	1

;--------------------------------------------------------
; indirectly addressable internal ram data
;--------------------------------------------------------
	.area ISEG    (DATA)
;--------------------------------------------------------
; absolute internal ram data
;--------------------------------------------------------
	.area IABS    (ABS,DATA)
	.area IABS    (ABS,DATA)
;--------------------------------------------------------
; bit data
;--------------------------------------------------------
	.area BSEG    (BIT)
;--------------------------------------------------------
; paged external ram data
;--------------------------------------------------------
	.area PSEG    (PAG,XDATA)
;--------------------------------------------------------
; external ram data
;--------------------------------------------------------
	.area XSEG    (XDATA)
_FLAG	=	0xff00
_I2C_ADDR	=	0xfe00
_I2C_LENGTH	=	0xfe01
_I2C_RW_MASK	=	0xfe02
_I2C_ERROR_CODE	=	0xfe03
_I2C_DATA	=	0xfe08
;--------------------------------------------------------
; absolute external ram data
;--------------------------------------------------------
	.area XABS    (ABS,XDATA)
;--------------------------------------------------------
; external initialized ram data
;--------------------------------------------------------
	.area XISEG   (XDATA)
	.area HOME    (CODE)
	.area GSINIT0 (CODE)
	.area GSINIT1 (CODE)
	.area GSINIT2 (CODE)
	.area GSINIT3 (CODE)
	.area GSINIT4 (CODE)
	.area GSINIT5 (CODE)
	.area GSINIT  (CODE)
	.area GSFINAL (CODE)
	.area CSEG    (CODE)
;--------------------------------------------------------
; interrupt vector 
;--------------------------------------------------------
	.area HOME    (CODE)
__interrupt_vect:
	ljmp	__sdcc_gsinit_startup
;--------------------------------------------------------
; global & static initialisations
;--------------------------------------------------------
	.area HOME    (CODE)
	.area GSINIT  (CODE)
	.area GSFINAL (CODE)
	.area GSINIT  (CODE)
	.globl __sdcc_gsinit_startup
	.globl __sdcc_program_startup
	.globl __start__stack
	.globl __mcs51_genXINIT
	.globl __mcs51_genXRAMCLEAR
	.globl __mcs51_genRAMCLEAR
	.area GSFINAL (CODE)
	ljmp	__sdcc_program_startup
;--------------------------------------------------------
; Home
;--------------------------------------------------------
	.area HOME    (CODE)
	.area HOME    (CODE)
__sdcc_program_startup:
	ljmp	_main
;	return from main will return to caller
;--------------------------------------------------------
; code
;--------------------------------------------------------
	.area CSEG    (CODE)
;------------------------------------------------------------
;Allocation info for local variables in function 'print'
;------------------------------------------------------------
;str                       Allocated to registers 
;------------------------------------------------------------
;	user.c:22: void print(const char *str) {
;	-----------------------------------------
;	 function print
;	-----------------------------------------
_print:
	ar7 = 0x07
	ar6 = 0x06
	ar5 = 0x05
	ar4 = 0x04
	ar3 = 0x03
	ar2 = 0x02
	ar1 = 0x01
	ar0 = 0x00
	mov	r5,dpl
	mov	r6,dph
	mov	r7,b
;	user.c:23: while (*str) {
00101$:
	mov	dpl,r5
	mov	dph,r6
	mov	b,r7
	lcall	__gptrget
	mov	r4,a
	jz	00104$
;	user.c:24: CHAROUT = *str++;
	mov	_CHAROUT,r4
	inc	r5
	cjne	r5,#0x00,00101$
	inc	r6
	sjmp	00101$
00104$:
	ret
;------------------------------------------------------------
;Allocation info for local variables in function 'seeprom_wait_until_idle'
;------------------------------------------------------------
;	user.c:28: void seeprom_wait_until_idle() {
;	-----------------------------------------
;	 function seeprom_wait_until_idle
;	-----------------------------------------
_seeprom_wait_until_idle:
;	user.c:29: while (I2C_STATE != 0) {}
00101$:
	mov	a,_I2C_STATE
	jnz	00101$
	ret
;------------------------------------------------------------
;Allocation info for local variables in function 'send_start'
;------------------------------------------------------------
;	user.c:33: void send_start() {
;	-----------------------------------------
;	 function send_start
;	-----------------------------------------
_send_start:
;	user.c:34: RAW_I2C_SCL = 0;
	mov	_RAW_I2C_SCL,#0x00
;	user.c:35: RAW_I2C_SDA = 1;
	mov	_RAW_I2C_SDA,#0x01
;	user.c:36: RAW_I2C_SCL = 1;
	mov	_RAW_I2C_SCL,#0x01
;	user.c:37: RAW_I2C_SDA = 0;
	mov	_RAW_I2C_SDA,#0x00
	ret
;------------------------------------------------------------
;Allocation info for local variables in function 'send_stop'
;------------------------------------------------------------
;	user.c:40: void send_stop() {
;	-----------------------------------------
;	 function send_stop
;	-----------------------------------------
_send_stop:
;	user.c:41: RAW_I2C_SCL = 0;
	mov	_RAW_I2C_SCL,#0x00
;	user.c:42: RAW_I2C_SDA = 0;
	mov	_RAW_I2C_SDA,#0x00
;	user.c:43: RAW_I2C_SCL = 1;
	mov	_RAW_I2C_SCL,#0x01
;	user.c:44: RAW_I2C_SDA = 1;
	mov	_RAW_I2C_SDA,#0x01
	ret
;------------------------------------------------------------
;Allocation info for local variables in function 'send_bit'
;------------------------------------------------------------
;a2                        Allocated to registers r7 
;------------------------------------------------------------
;	user.c:47: void send_bit(unsigned char a2) {
;	-----------------------------------------
;	 function send_bit
;	-----------------------------------------
_send_bit:
	mov	r7,dpl
;	user.c:48: RAW_I2C_SCL = 0;
	mov	_RAW_I2C_SCL,#0x00
;	user.c:49: RAW_I2C_SDA = (a2 & 1) != 0;
	anl	ar7,#0x01
	clr	a
	cjne	r7,#0x00,00103$
	inc	a
00103$:
	mov	r7,a
	cjne	a,#0x01,00105$
00105$:
	clr	a
	rlc	a
	mov	_RAW_I2C_SDA,a
;	user.c:50: RAW_I2C_SCL = 1;
	mov	_RAW_I2C_SCL,#0x01
	ret
;------------------------------------------------------------
;Allocation info for local variables in function 'send_byte'
;------------------------------------------------------------
;a2                        Allocated to registers r7 
;i                         Allocated to registers r5 r6 
;------------------------------------------------------------
;	user.c:53: void send_byte(unsigned char a2) {
;	-----------------------------------------
;	 function send_byte
;	-----------------------------------------
_send_byte:
	mov	r7,dpl
;	user.c:56: for ( i = 0; i <= 7; ++i ) {
	mov	r5,#0x00
	mov	r6,#0x00
00102$:
;	user.c:57: RAW_I2C_SCL = 0;
	mov	_RAW_I2C_SCL,#0x00
;	user.c:58: RAW_I2C_SDA = ((a2 >> (7 - i)) & 1) != 0;
	mov	a,#0x07
	clr	c
	subb	a,r5
	mov	r3,a
	clr	a
	subb	a,r6
	mov	r4,a
	mov	b,r3
	inc	b
	mov	a,r7
	sjmp	00111$
00110$:
	clr	c
	rrc	a
00111$:
	djnz	b,00110$
	anl	a,#0x01
	mov	r4,a
	clr	a
	cjne	r4,#0x00,00112$
	inc	a
00112$:
	mov	r4,a
	cjne	a,#0x01,00114$
00114$:
	clr	a
	rlc	a
	mov	_RAW_I2C_SDA,a
;	user.c:59: RAW_I2C_SCL = 1;
	mov	_RAW_I2C_SCL,#0x01
;	user.c:56: for ( i = 0; i <= 7; ++i ) {
	inc	r5
	cjne	r5,#0x00,00115$
	inc	r6
00115$:
	clr	c
	mov	a,#0x07
	subb	a,r5
	mov	a,#(0x00 ^ 0x80)
	mov	b,r6
	xrl	b,#0x80
	subb	a,b
	jnc	00102$
	ret
;------------------------------------------------------------
;Allocation info for local variables in function 'recv_byte'
;------------------------------------------------------------
;i                         Allocated to registers r5 r6 
;v3                        Allocated to registers r7 
;------------------------------------------------------------
;	user.c:63: unsigned char recv_byte() {
;	-----------------------------------------
;	 function recv_byte
;	-----------------------------------------
_recv_byte:
;	user.c:67: v3 = 0;
	mov	r7,#0x00
;	user.c:68: for ( i = 0; i <= 7; ++i ) {
	mov	r5,#0x00
	mov	r6,#0x00
00102$:
;	user.c:69: RAW_I2C_SCL = 0;
	mov	_RAW_I2C_SCL,#0x00
;	user.c:70: RAW_I2C_SCL = 1;
	mov	_RAW_I2C_SCL,#0x01
;	user.c:71: v3 = (v3 << 1) | ((RAW_I2C_SDA & 1) != 0);
	mov	a,r7
	add	a,r7
	mov	r4,a
	mov	a,#0x01
	anl	a,_RAW_I2C_SDA
	mov	r3,a
	clr	a
	cjne	r3,#0x00,00113$
	inc	a
00113$:
	mov	r3,a
	cjne	a,#0x01,00115$
00115$:
	clr	a
	rlc	a
	mov	r3,a
	orl	a,r4
	mov	r7,a
;	user.c:68: for ( i = 0; i <= 7; ++i ) {
	inc	r5
	cjne	r5,#0x00,00116$
	inc	r6
00116$:
	clr	c
	mov	a,#0x07
	subb	a,r5
	mov	a,#(0x00 ^ 0x80)
	mov	b,r6
	xrl	b,#0x80
	subb	a,b
	jnc	00102$
;	user.c:73: return v3;
	mov	dpl,r7
	ret
;------------------------------------------------------------
;Allocation info for local variables in function 'recv_ack'
;------------------------------------------------------------
;	user.c:76: unsigned char recv_ack() {
;	-----------------------------------------
;	 function recv_ack
;	-----------------------------------------
_recv_ack:
;	user.c:77: RAW_I2C_SCL = 0;
	mov	_RAW_I2C_SCL,#0x00
;	user.c:78: RAW_I2C_SCL = 1;
;	user.c:79: return (((unsigned char)RAW_I2C_SDA) & 1 != 0) ^ 1;
	mov	a,#0x01
	mov	_RAW_I2C_SCL,a
	anl	a,_RAW_I2C_SDA
	xrl	a,#0x01
	mov	dpl,a
	ret
;------------------------------------------------------------
;Allocation info for local variables in function 'main'
;------------------------------------------------------------
;i                         Allocated to registers r6 r7 
;c                         Allocated to registers r5 
;------------------------------------------------------------
;	user.c:82: void main(void) {
;	-----------------------------------------
;	 function main
;	-----------------------------------------
_main:
;	user.c:85: print("Hello World\n");
	mov	dptr,#___str_0
	mov	b,#0x80
	lcall	_print
;	user.c:86: seeprom_wait_until_idle();
	lcall	_seeprom_wait_until_idle
;	user.c:88: print("start\n");
	mov	dptr,#___str_1
	mov	b,#0x80
	lcall	_print
;	user.c:89: send_start();
	lcall	_send_start
;	user.c:91: print("op load_address\n");
	mov	dptr,#___str_2
	mov	b,#0x80
	lcall	_print
;	user.c:92: send_byte(SEEPROM_I2C_ADDR_WRITE);
	mov	dptr,#_SEEPROM_I2C_ADDR_WRITE
	clr	a
	movc	a,@a+dptr
	mov	r6,a
	mov	a,#0x01
	movc	a,@a+dptr
	mov	dpl,r6
	lcall	_send_byte
;	user.c:93: if (!recv_ack()) { print("failed 0\n"); goto end; }
	lcall	_recv_ack
	mov	a,dpl
	jnz	00102$
	mov	dptr,#___str_3
	mov	b,#0x80
	lcall	_print
	ljmp	00112$
00102$:
;	user.c:95: print("addr 0\n");
	mov	dptr,#___str_4
	mov	b,#0x80
	lcall	_print
;	user.c:96: send_byte(0);
	mov	dpl,#0x00
	lcall	_send_byte
;	user.c:97: if (!recv_ack()) { print("failed 1\n"); goto end; }
	lcall	_recv_ack
	mov	a,dpl
	jnz	00104$
	mov	dptr,#___str_5
	mov	b,#0x80
	lcall	_print
	ljmp	00112$
00104$:
;	user.c:99: print("restart\n");
	mov	dptr,#___str_6
	mov	b,#0x80
	lcall	_print
;	user.c:100: send_start();
	lcall	_send_start
;	user.c:101: print("op secure\n");
	mov	dptr,#___str_7
	mov	b,#0x80
	lcall	_print
;	user.c:102: send_byte(SEEPROM_I2C_ADDR_SECURE | 0b1111);
	mov	dptr,#_SEEPROM_I2C_ADDR_SECURE
	clr	a
	movc	a,@a+dptr
	mov	r6,a
	mov	a,#0x01
	movc	a,@a+dptr
	orl	ar6,#0x0F
	mov	dpl,r6
	lcall	_send_byte
;	user.c:103: if (!recv_ack()) { print("failed 2\n"); goto end; }
	lcall	_recv_ack
	mov	a,dpl
	jnz	00106$
	mov	dptr,#___str_8
	mov	b,#0x80
	lcall	_print
	sjmp	00112$
00106$:
;	user.c:105: print("restart 2\n");
	mov	dptr,#___str_9
	mov	b,#0x80
	lcall	_print
;	user.c:106: send_start();
	lcall	_send_start
;	user.c:108: print("op read\n");
	mov	dptr,#___str_10
	mov	b,#0x80
	lcall	_print
;	user.c:109: send_byte(SEEPROM_I2C_ADDR_READ);
	mov	dptr,#_SEEPROM_I2C_ADDR_READ
	clr	a
	movc	a,@a+dptr
	mov	r6,a
	mov	a,#0x01
	movc	a,@a+dptr
	mov	dpl,r6
	lcall	_send_byte
;	user.c:110: if (!recv_ack()) { print("failed 3\n"); goto end; }
	lcall	_recv_ack
	mov	a,dpl
	jnz	00122$
	mov	dptr,#___str_11
	mov	b,#0x80
	lcall	_print
;	user.c:112: for (i=0; i<256; i++) {
	sjmp	00112$
00122$:
	mov	r6,#0x00
	mov	r7,#0x00
00113$:
;	user.c:113: c = recv_byte();
	push	ar7
	push	ar6
	lcall	_recv_byte
	mov	r5,dpl
;	user.c:114: if (!recv_ack()) { print("failed read\n"); goto end; }
	push	ar5
	lcall	_recv_ack
	mov	a,dpl
	pop	ar5
	pop	ar6
	pop	ar7
	jnz	00110$
	mov	dptr,#___str_12
	mov	b,#0x80
	lcall	_print
	sjmp	00112$
00110$:
;	user.c:115: CHAROUT = c;
	mov	_CHAROUT,r5
;	user.c:112: for (i=0; i<256; i++) {
	inc	r6
	cjne	r6,#0x00,00143$
	inc	r7
00143$:
	clr	c
	mov	a,r7
	xrl	a,#0x80
	subb	a,#0x81
	jc	00113$
;	user.c:117: print("\n");
	mov	dptr,#___str_13
	mov	b,#0x80
	lcall	_print
;	user.c:119: end:
00112$:
;	user.c:120: POWEROFF = 1;
	mov	_POWEROFF,#0x01
	ret
	.area CSEG    (CODE)
	.area CONST   (CODE)
_SEEPROM_I2C_ADDR_MEMORY:
	.byte #0xA0,#0x00	;  160
_SEEPROM_I2C_ADDR_READ:
	.byte #0xA1,#0x00	;  161
_SEEPROM_I2C_ADDR_WRITE:
	.byte #0xA0,#0x00	;  160
_SEEPROM_I2C_ADDR_SECURE:
	.byte #0x50,#0x00	;  80
___str_0:
	.ascii "Hello World"
	.db 0x0A
	.db 0x00
___str_1:
	.ascii "start"
	.db 0x0A
	.db 0x00
___str_2:
	.ascii "op load_address"
	.db 0x0A
	.db 0x00
___str_3:
	.ascii "failed 0"
	.db 0x0A
	.db 0x00
___str_4:
	.ascii "addr 0"
	.db 0x0A
	.db 0x00
___str_5:
	.ascii "failed 1"
	.db 0x0A
	.db 0x00
___str_6:
	.ascii "restart"
	.db 0x0A
	.db 0x00
___str_7:
	.ascii "op secure"
	.db 0x0A
	.db 0x00
___str_8:
	.ascii "failed 2"
	.db 0x0A
	.db 0x00
___str_9:
	.ascii "restart 2"
	.db 0x0A
	.db 0x00
___str_10:
	.ascii "op read"
	.db 0x0A
	.db 0x00
___str_11:
	.ascii "failed 3"
	.db 0x0A
	.db 0x00
___str_12:
	.ascii "failed read"
	.db 0x0A
	.db 0x00
___str_13:
	.db 0x0A
	.db 0x00
	.area XINIT   (CODE)
	.area CABS    (ABS,CODE)
