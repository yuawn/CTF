#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

void read_input(char *buf,unsigned int size){
    int ret ;
    ret = __read_chk(0,buf,size,size);
    if(ret <= 0){
        puts("read error");
        _exit(1);
    }
    if(buf[ret-1] == '\n')
        buf[ret-1] = '\x00';
}

char buf[0x10];


int main(){
	setvbuf(stdin,0,_IONBF,0);
	setvbuf(stdout,0,_IONBF,0);
	setvbuf(stderr,0,_IONBF,0);
	for(unsigned int i = 4 ; i >= 0 ; i--){
		printf("Input:");
		read_input(buf,0x10);
		printf(buf);
		puts("");
		close(i);
	}
}
