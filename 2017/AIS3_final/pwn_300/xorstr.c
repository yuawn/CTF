#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <signal.h>
#include <time.h>
#include <unistd.h>

void read_input(char *buf,unsigned int size){
	int ret ;
	ret = read(0,buf,size);
	if(ret <= 0){
		puts("read error");
		exit(1);
	}
}

void handler(int signum){
	puts("Timeout");
	_exit(1);
}
void init(){
	setvbuf(stdout,0,_IONBF,0);
	setvbuf(stdin,0,_IONBF,0);
	setvbuf(stderr,0,_IONBF,0);
	signal(SIGALRM,handler);
	alarm(60);
}

int xorlen = 0 ;
int count = 0 ;
void xorstr(char *str){
	char result[128];
	char key[128];
	printf("What do you want to xor :");
	read_input(key,128);
	xorlen = strlen(key);
	for(count = 0 ; count < xorlen; count++){
		result[count] = str[count] ^ key[count];		
	}
	printf("Result:%s",result);
}

void process(){
	char str[128];
	printf("Your string:");
	read_input(str,128);
	xorstr(str);
	return;
}

int main(){
	init();
	while(1){
		process();
	}
	return 0;	
}
