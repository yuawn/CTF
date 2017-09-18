#include <stdio.h>
#include <unistd.h>



void get_flag(){
	int fd ;
	int password;
	int magic ;
	char key[] = "Not_real_key";
	char cipher[] = "Not_real_cipher";
	fd = open("/dev/urandom",0);
	read(fd,&password,4);
	printf("Give me maigc :");
	scanf("%d",&magic);
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
