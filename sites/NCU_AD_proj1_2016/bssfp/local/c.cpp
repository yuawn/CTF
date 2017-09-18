#include <stdio.h>
#include <stdlib.h>
#include <bits/stdc++.h> 
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#define BUF_SIZE 50

int fp = 0;
char name[BUF_SIZE] = {'0'};

int main()
{
	char buffer[BUF_SIZE];
	fp = open("./pass", 'r');

	puts("User name:");

	scanf("%s", name);
	printf("\n");
	read(fp, buffer, BUF_SIZE);
	printf("name: %p\nfp: %d\npass: %p\n",name,fp,buffer);
	printf("%s\n",buffer);
	if (!strncmp(buffer, name, BUF_SIZE))
	{
		printf("Good!\n");
		system("cat ./flag");
	}

	else
	{	printf("User does not exist.\n");
	}

	return 0;
}
