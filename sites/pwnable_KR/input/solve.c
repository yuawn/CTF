#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

//2016.11.17
//ln -s /home/input2/flag flag
//python -c "print '\xde\xad\xbe\xef'" | nc 127.0.0.1 1337
//flag->Mommy! I learned how to pass various input in Linux :)

int main() {
  char* argc[101] = {[0 ... 99] = "\x00"};
  argc['B'] = "\x20\x0a\x0d";
  argc['C'] = "1337";

  char* env[2] = {"\xde\xad\xbe\xef=\xca\xfe\xba\xbe"};

  FILE* fp = fopen("\x0a", w"r");
  fwrite("\x00\x00\x00\x00" , 4 , 1 , fp);
  fclose(fp);

  int pipe1[2] , pipe2[2] , pipe3[2];
  pipe(pipe1);
  pipe(pipe2);
  pipe(pipe3);

  if( fork() == 0 ){
    puts("Im parent.");
    dup2(pipe1[0],0);
    dup2(pipe2[0],2);
    close(pipe1[1]);
    close(pipe2[1]);
    close(pipe1[0]);
    close(pipe2[0]);
    dup2(pipe3[1],1);
    close(pipe3[0]);
    close(pipe3[1]);
    execve("/home/input2/input",argc,env);
  }
  else{
    write(pipe1[1] , "\x00\x0a\x00\xff" , 4);
    write(pipe2[1] , "\x00\x0a\x02\xff" , 4);

    char buf[250];
    read(pipe3[0],buf,250);
    printf("read -> %s\n",buf);
  }


  return 0;
}
