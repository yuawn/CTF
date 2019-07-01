__sfr __at(0xff) POWEROFF;
__sfr __at(0xfe) DEBUG;
__sfr __at(0xfd) CHAROUT;
__xdata __at(0xff00) unsigned char FLAG[0x100];

__sfr __at(0xfa) RAW_I2C_SCL;
__sfr __at(0xfb) RAW_I2C_SDA;

// I2C-M module/chip control data structure.
__xdata __at(0xfe00) unsigned char I2C_ADDR; // 8-bit version.
__xdata __at(0xfe01) unsigned char I2C_LENGTH;  // At most 8 (excluding addr).
__xdata __at(0xfe02) unsigned char I2C_RW_MASK;  // 1 R, 0 W.
__xdata __at(0xfe03) unsigned char I2C_ERROR_CODE;  // 0 - no errors.
__xdata __at(0xfe08) unsigned char I2C_DATA[8];  // Don't repeat addr.
__sfr __at(0xfc) I2C_STATE;  // Read: 0 - idle, 1 - busy; Write: 1 - start

const unsigned char SEEPROM_I2C_ADDR_MEMORY = 0b10100000;
const unsigned char SEEPROM_I2C_ADDR_SECURE = 0b01010000;

void print(const char *str) {
  while (*str) {
    CHAROUT = *str++;
  }
}

void seeprom_wait_until_idle() {
  while (I2C_STATE != 0) {}
}

void seeprom_write_byte(unsigned char addr, unsigned char value) {
  seeprom_wait_until_idle();

  I2C_ADDR = SEEPROM_I2C_ADDR_MEMORY;
  I2C_LENGTH = 2;
  I2C_ERROR_CODE = 0;
  I2C_DATA[0] = addr;
  I2C_DATA[1] = value;
  I2C_RW_MASK = 0b00;  // 2x Write Byte

  I2C_STATE = 1;
  seeprom_wait_until_idle();
}

unsigned char seeprom_read_byte(unsigned char addr) {
  seeprom_wait_until_idle();

  //DEBUG = 1;

  I2C_ADDR = SEEPROM_I2C_ADDR_MEMORY;
  I2C_LENGTH = 2;
  I2C_ERROR_CODE = 0;
  I2C_DATA[0] = addr;
  I2C_RW_MASK = 0b10;  // Write Byte, then Read Byte

  I2C_STATE = 1;
  seeprom_wait_until_idle();

  if (I2C_ERROR_CODE != 0) {
    return 0;
  }

  return I2C_DATA[1];
}

void pwn() {
  I2C_ADDR = SEEPROM_I2C_ADDR_MEMORY;
  I2C_LENGTH = 2;
  I2C_ERROR_CODE = 0;
  I2C_DATA[0] = 0;
  I2C_RW_MASK = 0b10;  // Write Byte, then Read Byte

  I2C_STATE = 1;
  CHAROUT = I2C_DATA[1];

  I2C_DATA[0] = 64;
  I2C_STATE = 4;

  CHAROUT = I2C_DATA[1];
}



unsigned char seeprom_read_byte2(unsigned char addr) {
  seeprom_wait_until_idle();

  I2C_ADDR = SEEPROM_I2C_ADDR_MEMORY;
  I2C_LENGTH = 2;
  I2C_ERROR_CODE = 0;
  I2C_DATA[0] = addr;
  I2C_RW_MASK = 0b10;  // Write Byte, then Read Byte

  //RAW_I2C_SCL = 0b11;
  //RAW_I2C_SDA = 0b01;
  I2C_STATE = 7;
  seeprom_wait_until_idle();

  return I2C_DATA[1];
}

void seeprom_secure_banks(unsigned char mask) {
  seeprom_wait_until_idle();

  I2C_ADDR = SEEPROM_I2C_ADDR_SECURE | (mask & 0b1111);
  I2C_LENGTH = 0;
  I2C_ERROR_CODE = 0;
  

  I2C_STATE = 1;
  seeprom_wait_until_idle();
}


void main( void ){

    int i;
    char buf[100];
    const char *msg = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
    char *ptr;


    /*for( i = 0; msg[i] != '\0' ; i++) {
        seeprom_write_byte( 128 + i, msg[i] );
    }*/
    
    /* for( i = 0 ; i < 0x10 ; i++ ){
        DEBUG = 1;
        CHAROUT = seeprom_read_byte( i );
    }*/

    //seeprom_secure_banks( 0b11112 );

    //ptr = 0xa0;

    //ptr[1] = '\n';

    /*for( i = 0 ; i < 0x1000 ; i++ ){
        __asm
            pop 0xa0
        __endasm;
        CHAROUT = *ptr--;
        //print( ptr );
        //ptr += 8;
    }*/


    /*I2C_ADDR = SEEPROM_I2C_ADDR_MEMORY;
    I2C_LENGTH = 2;
    I2C_ERROR_CODE = 0;
    I2C_RW_MASK = 0b10;
    I2C_DATA[0] = 64;

    I2C_STATE = 1;
    CHAROUT = I2C_DATA[1];
    */

    I2C_ADDR = SEEPROM_I2C_ADDR_MEMORY;
    //I2C_ADDR = 0b10100000;
    //I2C_ADDR = 0b11010000;
    I2C_LENGTH = 2;
    I2C_ERROR_CODE = 0;
    I2C_RW_MASK = 0b10;
    I2C_DATA[0] = 0b01000000;

    //RAW_I2C_SCL = 0b01;

    I2C_STATE = 7;
    CHAROUT = I2C_DATA[1];

    //I2C_STATE = 0;

    /*seeprom_secure_banks( 0b1111 );

    for( i = 0 ; i < 100 ; i++ ){
        buf[i] = seeprom_read_byte( 64 + i );
    }

    print( buf );
    */
    //ptr[0] = 'a';
    //ptr[1] = 'b';  

    //while(1){
    //    CHAROUT = ptr;
        
        //DEBUG = 1;
        //seeprom_read_byte2(0);
    //}


    //print( buf );


    /*while(1){
        I2C_ADDR = SEEPROM_I2C_ADDR_MEMORY;
        I2C_LENGTH = 2;
        I2C_DATA[0] = 0;
        I2C_RW_MASK = 0b10;
        I2C_STATE = 1;
        CHAROUT = I2C_DATA[1];
        //seeprom_wait_until_idle();
        I2C_ADDR = SEEPROM_I2C_ADDR_MEMORY;
        I2C_LENGTH = 2;
        I2C_DATA[0] = 64;
        I2C_RW_MASK = 0b10;
        I2C_STATE = 7;
        CHAROUT = I2C_DATA[1];
        //seeprom_wait_until_idle();
        
    }*/

    while(1){
        //pwn();
    }

    //POWEROFF = 1;

}

// 0x2292C0
// 0x2392C0