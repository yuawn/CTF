#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(){
	char buf[0x20];
	setvbuf(stdout,0,_IONBF,0);
	printf("Read your input:");
	read(0,buf,0x30);
	return 0 ;
}
