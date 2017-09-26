#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <io.h>
int count = 0;

void echo() {
	char buf[16];
	if (!count) {
		printf("What do you want to say : ");
		read(0, buf, 15);
		printf("You say : ");
		printf(buf);
		count++;
	}else {
		puts("Hello world !");
	}
}

int bof() {
	int size;
	char buf[20];
	puts("Do you know stack overflow ?");
	printf("Try your best : ");
	size = read(0,buf,100);
	puts("Boom !!!");
	return size;
}

void menu() {
	puts("***************************");
	puts("     AIS 3 BOF Testing     ");
	puts("***************************");
	puts(" 1. Echo ");
	puts(" 2. Try your overflow");
	puts(" 3. Exit");
	puts("***************************");
	printf("Your choice: ");
}

int main()
{
	char buf[8];
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
	while (1) {
		menu();
		read(0, buf, 7);
		switch (atoi(buf)) {
			case 1:
				echo();
				break;
			case 2:
				bof();
				break;
			case 3:
				system("echo Bye");
				exit(0);
				break;
			default:
				puts("Invalid choice");
				break;
		}

	}
	    return 0;
}