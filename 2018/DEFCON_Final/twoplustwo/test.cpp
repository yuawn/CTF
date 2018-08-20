//g++ -otest test.cpp src/duktape.c -Isrc -lm
#include <stdio.h>
#include "duktape.h"

int main(int argc, char *argv[]) {
  duk_context *ctx = duk_create_heap_default();
  //duk_eval_string(ctx, "1+2");
  //printf("1+2=%d\n", (int) duk_get_int(ctx, -1));
  duk_eval_string(ctx, "(function a() { print( getname() , getname() , getname() ); print(getname()); print(getname()); })");
  duk_dump_function(ctx);
  void *ptr;
  duk_size_t sz;

  ptr = duk_get_buffer(ctx, -1, &sz);
  printf("buf=%p, size=%lu\n", ptr, (unsigned long) sz);
  for(int i=0;i<sz;i++)
    printf("\\x%02x",*((unsigned char*)ptr + i));
  puts("");

  duk_destroy_heap(ctx);
  return 0;
}