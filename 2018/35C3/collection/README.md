# 35C3 CTF 2018
## collection
* We found the way to control vtable function pointer.
* We tried to find gadget or control rbp, but this way was uncompleted in the end.
```asm
call [r11+0x58]
```
* Final solution was completed by sasdf.