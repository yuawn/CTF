// by sasdf
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

const SEEPROM_I2C_ADDR_MEMORY = 0b10100000;
const SEEPROM_I2C_ADDR_READ =   0b10100001;
const SEEPROM_I2C_ADDR_WRITE =  0b10100000;
const SEEPROM_I2C_ADDR_SECURE = 0b01010000;

void print(const char *str) {
  while (*str) {
    CHAROUT = *str++;
  }
}

void seeprom_wait_until_idle() {
  while (I2C_STATE != 0) {}
}

/* Raw i2c protocol */
void send_start() {
  RAW_I2C_SCL = 0;
  RAW_I2C_SDA = 1;
  RAW_I2C_SCL = 1;
  RAW_I2C_SDA = 0;
}

void send_stop() {
  RAW_I2C_SCL = 0;
  RAW_I2C_SDA = 0;
  RAW_I2C_SCL = 1;
  RAW_I2C_SDA = 1;
}

void send_bit(unsigned char a2) {
  RAW_I2C_SCL = 0;
  RAW_I2C_SDA = (a2 & 1) != 0;
  RAW_I2C_SCL = 1;
}

void send_byte(unsigned char a2) {
  signed int i; // [rsp+1Ch] [rbp-4h]

  for ( i = 0; i <= 7; ++i ) {
    RAW_I2C_SCL = 0;
    RAW_I2C_SDA = ((a2 >> (7 - i)) & 1) != 0;
    RAW_I2C_SCL = 1;
  }
}

unsigned char recv_byte() {
  signed int i; // [rsp+18h] [rbp-18h]
  unsigned char v3; // [rsp+1Fh] [rbp-11h]

  v3 = 0;
  for ( i = 0; i <= 7; ++i ) {
    RAW_I2C_SCL = 0;
    RAW_I2C_SCL = 1;
    v3 = (v3 << 1) | ((RAW_I2C_SDA & 1) != 0);
  }
  return v3;
}

unsigned char recv_ack() {
  RAW_I2C_SCL = 0;
  RAW_I2C_SCL = 1;
  return (((unsigned char)RAW_I2C_SDA) & 1 != 0) ^ 1;
}

void main(void) {
    int i;
    unsigned char c;
    print("Hello World\n");
    seeprom_wait_until_idle();

    print("start\n");
    send_start();

    print("op load_address\n");
    send_byte(SEEPROM_I2C_ADDR_WRITE);
    if (!recv_ack()) { print("failed 0\n"); goto end; }

    print("addr 0\n");
    send_byte(0);
    if (!recv_ack()) { print("failed 1\n"); goto end; }

    print("restart\n");
    send_start();
    print("op secure\n");
    send_byte(SEEPROM_I2C_ADDR_SECURE | 0b1111);
    if (!recv_ack()) { print("failed 2\n"); goto end; }

    print("restart 2\n");
    send_start();

    print("op read\n");
    send_byte(SEEPROM_I2C_ADDR_READ);
    if (!recv_ack()) { print("failed 3\n"); goto end; }

    for (i=0; i<256; i++) {
        c = recv_byte();
        if (!recv_ack()) { print("failed read\n"); goto end; }
        CHAROUT = c;
    }
    print("\n");

end:
    POWEROFF = 1;
}