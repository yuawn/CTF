#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <unistd.h>

uint32_t state = 42;


void dish(uint8_t d)
{
    state = ((state + d) * 3294782) ^ 3159238819;
}

int main()
{
    uint8_t input[32];
    read(0, input, 32);

    for (uint32_t idx = 0; idx < 32; idx++) {
        dish(input[idx]);
    }

    if(state == 0xde11c105) {
        system("/bin/cat flag.txt");
    }
    return 0;
}
