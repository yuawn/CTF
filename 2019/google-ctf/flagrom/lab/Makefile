all:
	sdcc user.c
	packihx user.ihx > user.hex
	objcopy -I ihex -O binary user.hex user.bin