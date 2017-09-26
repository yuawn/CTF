#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

char shellcode[120];

char *memstr(char *haystack, char *needle, int size) {
	char *p;
	char needlesize = strlen(needle);

	for (p = haystack; p <= (haystack-needlesize+size); p++)
	{
		if (memcmp(p, needle, needlesize) == 0)
			return p; /* found */
	}
	return NULL;
}

void welcome() {
	puts("=======================================");
	puts("      shellcode challenge, again!      ");
	puts("=======================================");
	puts("Rule :                                ");
	puts(" 1. limited number of syscalls        ");
	puts(" 2. Filter \"flag\" in your shellcode ");
	puts(" 3. read or write up to 120 bytes     ");
	puts("=======================================");
	puts("Hint: What did you see in misc1?");
}

int main() {
	setvbuf(stdin,  NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);

	alarm(10);
	welcome();

	printf("Show me your shellcode (max = %zi bytes): ", sizeof(shellcode));
	read(0, shellcode, sizeof(shellcode));
	if(memstr(shellcode, "flag", sizeof(shellcode))){
		puts("Oops!");
		exit(0);
	}

	(*(void(*)())shellcode)();

	return 0;
}

