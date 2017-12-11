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

char *heap = NULL ;

void allocate_heap(){
	size_t size ;
	printf("Size :") ;
	size = read_long();
	heap = malloc(size);
	if(heap){
		printf("Data :");
		read_input(heap,size+8);
		puts("Done !");
	}else{
		puts("Error !");
		_exit(0);
	}
	

}


void show_heap(){
	if(heap){
		puts(heap);
	}
}

void menu(){
    puts("$$$$$$$$$$$$$$$$$$$$$$$$$$$");
    puts("👼    Baby heap revenge   👼");
    puts("$$$$$$$$$$$$$$$$$$$$$$$$$$$");
    puts("$   1. Allocate heap      $");
    puts("$   2. Show heap          $ ");
    puts("$   3. Exit               $ ");
    puts("$$$$$$$$$$$$$$$$$$$$$$$$$$$");
    printf("Your choice: ");
}

int main(void){
    unsigned long long choice;
    init_proc();
    while(1){
        menu();
        choice = read_long();
        switch(choice){
            case 1:
                allocate_heap();
                break;
            case 2:
                show_heap();
                break;
            case 3:
                _exit(0);
                break ;
            default:
                puts("Invalid Choice");
                break;
        }
    }
}
