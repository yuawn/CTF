#include <stdio.h>
#include <unistd.h>
#include <time.h>
#include <stdlib.h>

char flag[40] ;

int main(){
	setvbuf(stdout,0,2,0);
	char buf[100];
	int fd ;
	fd = open("/home/cr4ck/flag",0);
	if(fd == -1){
		puts("Error");
		exit(-1);
	}
	read(fd,flag,32);
	printf("What your name ? ");
	read(0,buf,99);
	printf("Hello ,");
	printf(buf);
	puts("Goodbye !");	
}
