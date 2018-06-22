docker pull ubuntu:17.10

docker run -i -t ID

gcc version 7.2.0 (Ubuntu 7.2.0-8ubuntu3.2)


```c
#include<stdio.h>
#include<stdlib.h>


int main(){


	srand(0);
	for( int i = 0 ; i < 85 ; ++i ) printf("%d\n" , rand() % 2018);

	return 0;
}
```

