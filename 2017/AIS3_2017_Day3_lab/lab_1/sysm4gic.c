#include <stdio.h>
#include <unistd.h>



void get_flag(){
	int fd ;
	unsigned long password;
	unsigned long magic ;
	char key[] = "why_my_teammate_Orange_is_so_angry??";
	char cipher[] = "hahaha";
	fd = open("/dev/urandom",0);
	read(fd,&password,8);
	printf("Give me maigc :");
	scanf("%lu",&magic);
	if(password == magic){
		for(int i = 0 ; i < sizeof(cipher) ; i++){
			printf("%c",cipher[i]^key[i]);
		}
	}
}


int main(){
	setvbuf(stdout,0,2,0);
	get_flag();
	return 0 ;
}
