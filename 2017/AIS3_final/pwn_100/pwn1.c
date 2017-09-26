#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include "mysandbox.h"


char *memstr(char *haystack, char *needle, int size)
{
	char *p;
	char needlesize = strlen(needle);

	for (p = haystack; p <= (haystack-needlesize+size); p++)
	{
		if (memcmp(p, needle, needlesize) == 0)
			return p; /* found */
	}
	return NULL;
}

void description(){
	puts("========================================");
	puts("       Shellcode challenge Revenge     ");
	puts("========================================");
	puts("Rule :                                ");
	puts(" 1. Only allow open/read/write/exit   ");
	puts(" 2. Filter \"flag\" in your shellcode ");
	puts(" 3. arg3 of read < 42 when running\n    shellcode");
	puts("========================================");
	puts("Do you remember the shellcode challenge in ais3 pre-exam this year ?");
	puts("Can you read the flag again ?");
}

int main(){
	char *shellcode ;
	setvbuf(stdin,0,2,0);
	setvbuf(stdout,0,2,0);
	alarm(10);
	description();
	shellcode = (char*)malloc(0x100);
	printf("Give me your shellcode (max = 87 bytes):");
	read(0,shellcode,87);
	mprotect((long int)shellcode & 0xfffffffffffff000,0x1000,5);
	my_sandbox(); //only allow open/read/write/exit 
	if(memstr(shellcode,"flag",87)){
		puts("Oops !");
		exit(0);
	}
	(*(void(*)())shellcode)();
}
