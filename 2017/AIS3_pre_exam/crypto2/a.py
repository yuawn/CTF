#!/usr/bin/env python3
import signal
import sys
import os
import time
import string

if sys.version_info < (3, 0): # For python2
	from urlparse import parse_qs
else: # For python3
	from urllib.parse import parse_qs

from base64 import b64encode as b64e
from base64 import b64decode as b64d
from Crypto.Cipher import AES

FLAG = 'UNKNOWN_FLAG'
KEY = 'abcdefgdhtjg63fr'
IV = 'UNKNOWN_IV'

blockSize = 16

if sys.version_info < (3, 0): # For python2
	input = raw_input


class AESCryptor:

	def __init__(self, key, iv):

		self.KEY = key
		self.IV = iv
		self.aes = AES.new(self.KEY, AES.MODE_ECB, self.IV)


	def encrypt(self, data):
		return self.aes.encrypt(self.pad(data))


	def decrypt(self, data):
		return self.unpad(self.aes.decrypt(data))

	def pad(self, data):
		num = blockSize - len(data) % blockSize
		return data + chr(num) * num

	def unpad(self, data):

		lastValue = 0

		if type(data[-1]) is int:
			lastValue = data[-1]
		else:
			lastValue = ord(data[-1])

		return data[:len(data)-lastValue]


aes = AESCryptor(KEY, IV)


def bye(s):

	print(s)
	exit(0)


def alarm(time):

	signal.signal(signal.SIGALRM, lambda signum, frame: bye('Too slow!'))
	signal.alarm(time)


def printFlag():

	print(FLAG)


def register(name , pwd):

	#name = input('What is your name? ').strip()

	for c in name:
		if c not in string.ascii_letters:
			bye('Invalid characters.(Only alphabets are permitted)')

	#pwd = input('Give me your password: ').strip()

	for c in pwd:
		if c not in string.ascii_letters:
			bye('Invalid characters. (Only alphabets are permitted)')

	pattern = 'name=' + name + '&role=student' + '&password=' + pwd

	print('This is your token: ' + b64e(aes.encrypt(pattern)).decode())


def login(token , name , pwd ):

	#token = input('Give me your token: ').strip()
	#name = input('Give me your username: ').strip().encode()
	#pwd = input('Give me your password: ').strip().encode()

	#try:
		pt = aes.decrypt(b64d(token))
		data = parse_qs(pt, strict_parsing=True)

		if name != data[b'name'][0] or pwd != data[b'password'][0]:
			print('Authentication failed')
			return

		print('Hello %s %s' % (data[b'name'][0].decode() , data[b'role'][0].decode()) )

		data[b'role'].append( b'admin' )

		if b'admin' in data[b'role']:
			print('Hi admin:')
			printFlag()
	#except Exception:
		#print('Something went wrong!! QAQ')
	


"""
def main():

	alarm(60)
	print('Select your choice: ')
	print('0 : Register')
	print('1 : Login')
	num = int(input().strip())

	if num == 0:
		register()
	elif num == 1:
		login()

if __name__ == '__main__':

	main()
"""
#name=yuawn&role= student&password =a
#######d5578bc3beda9c7a67d4f039bb7c27fa
#d0665c60f094b33720c8679e428db55f
#80db4bb5c63e979635a514f05fc29cfd

#name=aaaaaaaaaaa adminadminadmina &role=student&pa ssword=b
#337055ef878bf77fff6a1b503678a9a6
#######821bf3ca91229d825c9f60c09b9bcfa9
#5fe74ae8f090bbce9f1224a0f6d29f95
#d0a66336f0539bdff06f7f8e117e80a7

#name=aaaaaaaaaaa aaa&role=student &password=yass
#337055ef878bf77fff6a1b503678a9a6
#7a39793526ec42204b664c70a29fb716
#######736eb69f5c98e0459387a04ef5df5b2f

# d5578bc3beda9c7a67d4f039bb7c27fa821bf3ca91229d825c9f60c09b9bcfa9736eb69f5c98e0459387a04ef5df5b2f
# 1VeLw77anHpn1PA5u3wn+oIb88qRIp2CXJ9gwJubz6lzbrafXJjgRZOHoE7131sv

register( 'yuawn' , 'a' ) # 1VeLw77anHpn1PA5u3wn+tBmXGDwlLM3IMhnnkKNtV+A20u1xj6XljWlFPBfwpz9
register( 'aaaaaaaaaaa' + 'adminadminadmina' , 'b' ) # M3BV74eL93//ahsFNnippoIb88qRIp2CXJ8GDJubz6lf50roD5C7zp8SJKD20p+VDaZjNvBTm98Pb3+OEX4Ipw==
register( 'aaaaaaaaaaaaaa' , 'yass' ) # M3BV74eL93//ahsFNnippno5eTUm7EICS2ZMcKKftxZzbrafXJjgRZOHCk7131sv

login( b'1VeLw77anHpn1PA5u3wn+tBmXGDwlLM3IMhnnkKNtV+A20u1xj6XljWlFPBfwpz9' , b'yuawn' , b'a' )
login( b'M3BV74eL93//ahsFNnippoIb88qRIp2CXJ8GDJubz6lf50roD5C7zp8SJKD20p+VDaZjNvBTm98Pb3+OEX4Ipw==' , b'aaaaaaaaaaaadminadminadmina' , b'b' )
login( b'M3BV74eL93//ahsFNnippno5eTUm7EICS2ZMcKKftxZzbrafXJjgRZOHCk7131sv' , b'aaaaaaaaaaaaaa' , b'yass' )

#
ans = b64d('1VeLw77anHpn1PA5u3wn+tBmXGDwlLM3IMhnnkKNtV+A20u1xj6XljWlFPBfwpz9')[:16] + b64d('M3BV74eL93//ahsFNnippoIb88qRIp2CXJ8GDJubz6lf50roD5C7zp8SJKD20p+VDaZjNvBTm98Pb3+OEX4Ipw==')[16:32] + b64d('M3BV74eL93//ahsFNnippno5eTUm7EICS2ZMcKKftxZzbrafXJjgRZOHCk7131sv')[32:48]
ans = b64e( ans )

print( ans )

login( ans , b'yuawn' , b'yass' )