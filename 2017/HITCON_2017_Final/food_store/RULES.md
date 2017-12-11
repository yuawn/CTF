Food Store
====

Where Is The Service
--------------------
`nc 10.0.<TN>.1 56746`

Which File Should Be Patched
----------------------------
`food_store`

Where Is The Flag
-----------------
`/home/food_store/flag`

How We Run This Service
-----------------------
We will run `food_store` in the nsjail. The nsjail config is `food_store.cfg`. The service is 

Wrapper
-



```
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
int main(int argc,char *argv[],char *envp[]){
    int fd = open("/dev/null",O_RDWR);
    dup2(fd,2);
    execve("/home/food_store/binary",argv,envp);
}
```