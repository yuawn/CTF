import rsa

n = 66473473500165594946611690873482355823120606837537154371392262259669981906291
e = 65537
PUBKEY = rsa.PublicKey(n, e)

def encrypt(s, pubkey):
	return rsa.encrypt( s, pubkey )

if __name__ == '__main__':
	with open('flag.txt', 'r') as fp:
		flag = fp.read()
	
	with open('flag.enc', 'w') as fp:
		fp.write( encrypt(flag, PUBKEY) )