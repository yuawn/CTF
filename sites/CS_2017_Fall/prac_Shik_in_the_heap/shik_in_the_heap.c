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
	buf[ret] = '\x00';
} 

void menu(){
	puts("##########################");
	puts("     Shik in the heap     ");
	puts("##########################");
	puts(" 1.Allocate               ");
	puts(" 2.Free                   ");
	puts(" 3.Add a shik             ");
	puts(" 4.show a shik            ");
	puts(" 5.edit a shik            ");
	puts(" 6.Exit                   ");
	puts("##########################");
	printf("Your choice:");
}

struct shik{
	char *data ;
	int id ;
};

char *heap[10];
struct shik *s = NULL;

void allocate(){
	size_t size ;
	for(int i = 0 ; i < 10 ; i++){
		if(!heap[i]){
			printf("Size:");
			size = read_long();
			heap[i] = malloc(size);
			if(!heap[i]){
				puts("Error!");	
			}
			printf("Content:");
			read_input(heap[i],size);
			return ;
		}
	}
	puts("Too more !");
}

void dfree(){
	unsigned int idx = 0 ;
	printf("Index:");
	idx = read_long();
	if(idx < 10){
		free(heap[idx]);
		heap[idx] = NULL ;	
	}else{
		puts("Too large");
	}
}

void add_shik(){
	if(!s){
		s = malloc(sizeof(struct shik));
		s->data = malloc(32);
		printf("magic :");
		read_input(s->data,32);
		s->id = rand();
	}else{
		puts("shik is our god");
	}
}

void show_shik(){
	if(s){
		printf("Magic: %s",s->data);
	}else{
		puts("shik is not here");
	}
}

void edit_shik(){
	if(s){
		printf("magic:");
		read_input(s->data,32);
	}else{
		puts("shik is not here");
	}
}

int main(){
	init_proc();
	while(1){
		menu();
		switch(read_long()){
			case 1:
				allocate();
				break;
			case 2:
				dfree();
				break;
			case 3:
				add_shik();
				break;
			case 4:
				show_shik();
				break;
			case 5:
				edit_shik();
				break;
			case 6:
				exit(0);
				break ;
			default:
				puts("Invalid choice");
				break;

		}
	}
}
