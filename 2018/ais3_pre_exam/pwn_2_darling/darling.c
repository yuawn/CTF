#include"stdio.h"
#include"stdlib.h"
#include"unistd.h"

void debug(){
  system("/bin/sh");
}

int main(){
  setvbuf(stdout, 0, 2, 0);
  setvbuf(stdin, 0, 2, 0);

  char parasite[8][16] = {"Hiro", "Zero Two", "Ichigo", "Goro", "Miku", "Zorome", "Kokoro", "Futoshi"};
  long long int code[8] = {16, 2, 15, 56, 390, 666, 556, 214};
  long long int pair[2] = {0, 0};
  long long int permission_code = 1602;
  char franxx[5][16] = {"Strelitzia", "Delphinium", "Argentea", "Genista", "Chlorophytum"};

  printf("Gutenberg drangon is near.\n");
  printf("Here is all parasites of the 13th plantation:\n");
  printf("+-----------------------+\n");
  printf("|  code  |   parasite   |\n");
  printf("+-----------------------+\n");
  for(int i=0; i<8; i++){
    printf("|   %3lld%16s |\n", code[i], parasite[i]);
  }
  printf("+-----------------------+\n");
  
  printf("Commander, please choose two parasites to defense plantation.\n");
  int idx;
  int sure;
  while(1){
    printf("Index: ");
    scanf("%d", &idx);
    if(idx > 2){
      printf("Error: index error\n");
      continue;
    }
    printf("Code: ");
    scanf("%lld", &pair[idx]);
    for(int i=0; i<8; i++){
      if(code[i] == pair[idx]){
        printf(">> %3lld %16s\n", code[i], parasite[i]);
        break;
      }
    }
    printf("Are you sure ? (yes:1 / no:0) ");
    scanf("%d", &sure);
    if(sure == 1)break;
  }
  
  if(permission_code == 6666){
    printf("FRANXX list:\n");
    for(int i=0; i<5; i++){
      printf("%d: %16s\n", i, franxx[i]);
    }
    printf("Which FRANXX do you wnat to use ? ");
    scanf("%d", &idx);
    if(idx > 5){
      printf("Error: index error\n");
      exit(0);
    }
    printf("New name for this FRANXX: ");
    read(0, franxx[idx], 16);

    if(idx == 0 && pair[0] == 2 && pair[1] == 16){
      printf("Win OUO\n");
    }else{
      printf("Failed QQ\n");
    }
  }else{
    printf("Error: permission denied.\n");
  }

  return 0;
}
