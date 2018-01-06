#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdbool.h>
#include <stdlib.h>
#include <signal.h>
#include <time.h>
#define TIMEOUT 60

void handler(int signum){
	puts("Timeout");
	_exit(1);
} 

void init_proc(){
	setvbuf(stdin,0,2,0);
	setvbuf(stdout,0,2,0);
	setvbuf(stderr,0,2,0);
	signal(SIGALRM,handler);
	alarm(TIMEOUT);
} 

long long read_long(){
	char buf[24];
	long long choice ;
	__read_chk(0,buf,23,24);
	choice = atoll(buf);
	return choice;
}
 
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

void menu(){
	puts("###################");
	puts("     Baby Fast 	 ");
	puts("###################");
	puts(" 1. Allocate       ");
	puts(" 2. Free           ");
	puts(" 3. Exit           ");
	puts("###################");
	printf("Your choice :");
}

char *heap[10];

void magic(){
	system("echo 'hello'");
}

void allocate(){
	size_t size = 0 ;
	for(int i = 0 ; i < 10; i++){
		if(!heap[i]){
			printf("Size:");
			size = read_long();
			heap[i] = malloc(size);
			if(!heap[i]){
				puts("ERROR");
				exit(-1);
			}
			printf("Data:");
			read_input(heap[i],size);
			puts("Done!");
			return ;
		}
	}
}

void dfree(){
	unsigned int idx = 0;
	printf("Index:");
	idx = read_long();
	if(idx < 10){
		free(heap[idx]);
	}else{
		puts("Too large");
	}
}

int main(){
	init_proc();
	magic();
	while(1){
		menu();
		switch(read_long()){
			case 1 :
				allocate();
				break ;
			case 2 :
				dfree();
				break ;
			case 3 :
				exit(0);
				break ;
			default :
				puts("Invalid choice");
				break;
		}
	}
}

