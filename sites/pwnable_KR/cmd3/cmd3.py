#!/usr/bin/python
import base64, random, math
import os, sys, time, string
from threading import Timer

def rstring(N):
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

password = rstring(32)
filename = rstring(32)

TIME = 60
class MyTimer():
	global filename
        timer=None
        def __init__(self):
                self.timer = Timer(TIME, self.dispatch, args=[])
                self.timer.start()
        def dispatch(self):
                print 'time expired! bye!'
		sys.stdout.flush()
		os.system('rm flagbox/'+filename)
                os._exit(0)

def filter(cmd):
	blacklist = '` !&|"\'*'
	for c in cmd:
		if ord(c)>0x7f or ord(c)<0x20: return False
		if c.isalnum(): return False
		if c in blacklist: return False
	return True

if __name__ == '__main__':
	MyTimer()
	print 'your password is in flagbox/{0}'.format(filename)
	os.system("ls -al")
	os.system("ls -al jail")
	open('flagbox/'+filename, 'w').write(password)
	try:
		while True:
			sys.stdout.write('cmd3$ ')
			sys.stdout.flush()
			cmd = raw_input()
			if cmd==password:
				os.system('./flagbox/print_flag')
				raise 1
			if filter(cmd) is False:
				print 'caught by filter!'
				sys.stdout.flush()
				raise 1

			os.system('echo "{0}" | base64 -d - | env -i PATH=jail /bin/rbash'.format(cmd.encode('base64')))
			sys.stdout.flush()
	except:
		os.system('rm flagbox/'+filename)
		os._exit(0)