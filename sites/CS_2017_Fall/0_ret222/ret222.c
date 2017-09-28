#include <stdio.h>

void read_input(char *buf,unsigned int size){
    int ret ;
    ret = read(0,buf,size);
    if(ret <= 0){
        puts("read error");
        _exit(1);
    }
    if(buf[ret-1] == '\n')
        buf[ret-1] = '\x00';
}

int read_int(){
	int ret ;
    char buf[16];
    unsigned choice ;
    ret = __read_chk(0,buf,15,16);
    if(ret <= 0){
        puts("read error");
        _exit(1);
    }
    choice = atoi(buf);
    return choice;
}

char name[16];

void init_proc(){
	setvbuf(stdout,0,2,0);
	setvbuf(stdin,0,2,0);
}

void menu(){
	puts("*******************");
	puts(" 1. Set name       ");
	puts(" 2. Show info      ");
	puts(" 3. Save data      ");
	puts(" 4. Exit           ");
	puts("*******************");
	printf("> ");
}

int main(){
	init_proc();
	char data[128];
	memset(data,0,128);
	while(1){
		menu();
		switch(read_int()){
			case 1 :
				printf("Your name:");
				read_input(name,16);
				break;
			case 2 :
				printf("Name:");
				printf(name);
				break;
			case 3 :
				printf("Your data:");
				gets(data);
				break;
			case 4 :
				mprotect(( (unsigned long)name & (~0xfff)),0x1000,7);
				return;
				break ;
			default :
				puts("Invaild choice !");
				break;
		}
	}
	
}