#!/usr/bin/python

import socket 
from threading import Thread 
from SocketServer import ThreadingMixIn 
from datetime import datetime
import md5
import numpy as np
import hashlib, binascii
import re

def square(x):
	try:
	    sum_so_far = 0
	    for _ in range(x):
	        sum_so_far += x
		return sum_so_far
	except Exception(e):
		print e
	finally:
		return sum_so_far

def get_key(x):
	nr = 1337
	try:
		for value in range(1,x):
			nr = nr * value
		return nr
	except Exception(e):
		print e
	finally:
		return nr

def hash(inp):
	return hashlib.sha256(str(inp) + "DCTF2018_BUCHAREST").hexdigest()

# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread): 
 
	def __init__(self,ip,port): 
		Thread.__init__(self) 
		self.ip = ip 
		self.port = port 
		print "[+] New server socket thread started for " + ip + ":" + str(port) 
 
	def run(self): 
		while True: 
			data = conn.recv(4096)

			print "Server received data:", data
			data = data.split(" ")

			if len(data) != 11:
				print "Tried until #1", self.ip
				conn.send("Try harder!\n")
				return conn.close()
			try:
				#validate date
				dinp = [int(x) for x in data[:5]]
				if (dinp[0] > 9999 or dinp[0] < 1 or dinp[1] < 1 or dinp[1] > 12 or 
					dinp[2] < 1 or dinp[2] > 31 or dinp[3] < 0 or dinp[3] > 23 or 
					dinp[4] < 0 or dinp[4] > 59):
					return conn.close()

				date = datetime(dinp[0], dinp[1], dinp[2], dinp[3], dinp[4]).time()
				if date: 
					print "Tried until #2", self.ip
					conn.send("Try harder!\n")
					return conn.close()
			except:
				print "Tried until #3", self.ip
				conn.send("Try harder!\n")
				return conn.close()
				pass

			if int(data[5]) != square(get_key(data[0])):
				print "Tried until #4", self.ip
				conn.send("Try harder!\n")
				return conn.close()

			inp    = (np.array([float(data[6]), float(data[7]), float(data[8]), float(data[9])])*PRIV)%int(data[5])
			test   = np.array([float(559), float(661), float(661), float(522)])
			solved = np.empty([], dtype=np.float)
			 
			for i in range(len(inp)):
				if inp[i] == test[i]: 
					solved = np.append(solved, test[i])
			
			if len(solved) != 4:
				print "Tried until #5", self.ip
				conn.send("Try harder!\n")
				return conn.close()

			if hash(np.sum(solved)*PRIV) != 'fe79a0ee1fc2a52fc9af8592d8c0570a73d9542ec1d4ec2ae6e9d03991cb0459':
				print "Tried until #6", self.ip
				conn.send("Try harder!\n")
				return conn.close()

			val = re.sub(r"[^a-z|\(|\)|<|\-|,|=]", '', data[10])
			if len(val) > 2000:
				print "Tried until #7", self.ip
				conn.send("Try harder!\n")
				return conn.close()
			try:
				exec('cmd='+val)
				print cmd
				exec(cmd)
				conn.send(a)
				a=None
				cmd=None
				print "Success", self.ip
				return conn.close()
			except:
				print "Failed", self.ip
				return conn.close()

# Multithreaded Python server : TCP Server Socket Program Stub
TCP_IP = '0.0.0.0' 
TCP_PORT = 13022 
BUFFER_SIZE = 20  # Usually 1024, but we need quick response 

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcpServer.bind((TCP_IP, TCP_PORT)) 
threads = [] 

PRIV = 1198041294


while True: 
	tcpServer.listen(4)  
	(conn, (ip,port)) = tcpServer.accept() 
	newthread = ClientThread(ip,port) 
	newthread.start() 
	threads.append(newthread) 
 
for t in threads: 
	t.join() 

