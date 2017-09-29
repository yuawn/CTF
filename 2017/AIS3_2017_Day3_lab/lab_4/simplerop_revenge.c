#include <stdio.h>
#include <unistd.h>
//gcc -fno-stack-protector -static simplerop_revenge.c -o simplerop_revenge
int main(){
	char buf[20];
	puts("ROP is easy is'nt it ?");
	printf("Your input :");
	fflush(stdout);
	read(0,buf,160);
}
