#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <fcntl.h>

char asdf[1024];

int main()
{
	long long index = 0;

	read(0, &index, 1024);
	read(0, asdf+index, 8);
	read(0, &index, 1024);
}
