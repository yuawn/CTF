from blockcipher import *
from rijndael import rijndael

def new(key,mode=MODE_ECB,IV=None,counter=None,segment_size=None,blocksize=None):
    """Create a new cipher object

    Wrapper for pure python implementation rijndael.py

        key = raw string containing the key
            -> supported key size are 16, 24 and 32 bytes
        mode = python_Rijndael.MODE_ECB/CBC/CFB/OFB/CTR/XTS/CMAC, default is ECB
            -> for every mode, except ECB and CTR, it is important to construct a seperate cipher for encryption and decryption
        IV = IV as a raw string, default is "all zero" IV
            -> needed for CBC, CFB and OFB mode
        counter = counter object (CryptoPlus.Util.util.Counter)
            -> only needed for CTR mode
            -> use a seperate counter object for the cipher and decipher: the counter is updated directly, not a copy
                see CTR example further on in the docstring
        segment_size = amount of bits to use from the keystream in each chain part
            -> supported values: multiple of 8 between 8 and the blocksize
               of the cipher (only per byte access possible), default is 8
            -> only needed for CFB mode
        blocksize = blocksize in bytes
            -> supported blocksizes are 16, 24 and 32 bytes, must be 16 if XTS mode.

    EXAMPLES:
    **********
    IMPORTING:
    -----------
    >>> from CryptoPlus.Cipher import python_Rijndael

    EXAMPLE:
    --------
    24 byte block, 32 byte key (http://fp.gladman.plus.com/cryptography_technology/rijndael/)
    >>> key = '2b7e151628aed2a6abf7158809cf4f3c762e7160f38b4da56a784d9045190cfe'.decode('hex')
    >>> plaintext ='3243f6a8885a308d313198a2e03707344a4093822299f31d'.decode('hex')
    >>> cipher = python_Rijndael.new(key,python_Rijndael.MODE_ECB,blocksize=24)
    >>> cipher.encrypt(plaintext).encode('hex')
    '0ebacf199e3315c2e34b24fcc7c46ef4388aa475d66c194c'

    CBC EXAMPLE (plaintext = 3 blocksizes) (AES):
    -----------------------------------------
    >>> key = ('2b7e151628aed2a6abf7158809cf4f3c').decode('hex')
    >>> IV = ('000102030405060708090a0b0c0d0e0f').decode('hex')
    >>> plaintext1 = ('6bc1bee22e409f96e93d7e117393172a').decode('hex')
    >>> plaintext2 = ('ae2d8a571e03ac9c9eb76fac45af8e51').decode('hex')
    >>> plaintext3 = ('30c81c46a35ce411e5fbc1191a0a52ef').decode('hex')
    >>> cipher = python_Rijndael.new(key,python_Rijndael.MODE_CBC,IV,blocksize=16)
    >>> ciphertext = cipher.encrypt(plaintext1 + plaintext2 + plaintext3)
    >>> (ciphertext).encode('hex')
    '7649abac8119b246cee98e9b12e9197d5086cb9b507219ee95db113a917678b273bed6b8e3c1743b7116e69e22229516'
    >>> decipher = python_Rijndael.new(key,python_Rijndael.MODE_CBC,IV,blocksize=16)
    >>> plaintext = decipher.decrypt(ciphertext)
    >>> (plaintext).encode('hex')
    '6bc1bee22e409f96e93d7e117393172aae2d8a571e03ac9c9eb76fac45af8e5130c81c46a35ce411e5fbc1191a0a52ef'

    XTS EXAMPLE:
    ------------
    (Examples for XTS-AES)
    XTS-AES-128 applied for a data unit of 512 bytes
    testvector: http://grouper.ieee.org/groups/1619/email/pdf00086.pdf

    >>> key = ('27182818284590452353602874713526'.decode('hex'),'31415926535897932384626433832795'.decode('hex'))
    >>> plaintext = '000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f202122232425262728292a2b2c2d2e2f303132333435363738393a3b3c3d3e3f404142434445464748494a4b4c4d4e4f505152535455565758595a5b5c5d5e5f606162636465666768696a6b6c6d6e6f707172737475767778797a7b7c7d7e7f808182838485868788898a8b8c8d8e8f909192939495969798999a9b9c9d9e9fa0a1a2a3a4a5a6a7a8a9aaabacadaeafb0b1b2b3b4b5b6b7b8b9babbbcbdbebfc0c1c2c3c4c5c6c7c8c9cacbcccdcecfd0d1d2d3d4d5d6d7d8d9dadbdcdddedfe0e1e2e3e4e5e6e7e8e9eaebecedeeeff0f1f2f3f4f5f6f7f8f9fafbfcfdfeff000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f202122232425262728292a2b2c2d2e2f303132333435363738393a3b3c3d3e3f404142434445464748494a4b4c4d4e4f505152535455565758595a5b5c5d5e5f606162636465666768696a6b6c6d6e6f707172737475767778797a7b7c7d7e7f808182838485868788898a8b8c8d8e8f909192939495969798999a9b9c9d9e9fa0a1a2a3a4a5a6a7a8a9aaabacadaeafb0b1b2b3b4b5b6b7b8b9babbbcbdbebfc0c1c2c3c4c5c6c7c8c9cacbcccdcecfd0d1d2d3d4d5d6d7d8d9dadbdcdddedfe0e1e2e3e4e5e6e7e8e9eaebecedeeeff0f1f2f3f4f5f6f7f8f9fafbfcfdfeff'.decode('hex')
    >>> cipher = python_Rijndael.new(key,python_Rijndael.MODE_XTS,blocksize=16)
    >>> ciphertext = cipher.encrypt(plaintext)
    >>> ciphertext.encode('hex')
    '27a7479befa1d476489f308cd4cfa6e2a96e4bbe3208ff25287dd3819616e89cc78cf7f5e543445f8333d8fa7f56000005279fa5d8b5e4ad40e736ddb4d35412328063fd2aab53e5ea1e0a9f332500a5df9487d07a5c92cc512c8866c7e860ce93fdf166a24912b422976146ae20ce846bb7dc9ba94a767aaef20c0d61ad02655ea92dc4c4e41a8952c651d33174be51a10c421110e6d81588ede82103a252d8a750e8768defffed9122810aaeb99f9172af82b604dc4b8e51bcb08235a6f4341332e4ca60482a4ba1a03b3e65008fc5da76b70bf1690db4eae29c5f1badd03c5ccf2a55d705ddcd86d449511ceb7ec30bf12b1fa35b913f9f747a8afd1b130e94bff94effd01a91735ca1726acd0b197c4e5b03393697e126826fb6bbde8ecc1e08298516e2c9ed03ff3c1b7860f6de76d4cecd94c8119855ef5297ca67e9f3e7ff72b1e99785ca0a7e7720c5b36dc6d72cac9574c8cbbc2f801e23e56fd344b07f22154beba0f08ce8891e643ed995c94d9a69c9f1b5f499027a78572aeebd74d20cc39881c213ee770b1010e4bea718846977ae119f7a023ab58cca0ad752afe656bb3c17256a9f6e9bf19fdd5a38fc82bbe872c5539edb609ef4f79c203ebb140f2e583cb2ad15b4aa5b655016a8449277dbd477ef2c8d6c017db738b18deb4a427d1923ce3ff262735779a418f20a282df920147beabe421ee5319d0568'
    >>> decipher = python_Rijndael.new(key,python_Rijndael.MODE_XTS,blocksize=16)
    >>> decipher.decrypt(ciphertext).encode('hex')
    '000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f202122232425262728292a2b2c2d2e2f303132333435363738393a3b3c3d3e3f404142434445464748494a4b4c4d4e4f505152535455565758595a5b5c5d5e5f606162636465666768696a6b6c6d6e6f707172737475767778797a7b7c7d7e7f808182838485868788898a8b8c8d8e8f909192939495969798999a9b9c9d9e9fa0a1a2a3a4a5a6a7a8a9aaabacadaeafb0b1b2b3b4b5b6b7b8b9babbbcbdbebfc0c1c2c3c4c5c6c7c8c9cacbcccdcecfd0d1d2d3d4d5d6d7d8d9dadbdcdddedfe0e1e2e3e4e5e6e7e8e9eaebecedeeeff0f1f2f3f4f5f6f7f8f9fafbfcfdfeff000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f202122232425262728292a2b2c2d2e2f303132333435363738393a3b3c3d3e3f404142434445464748494a4b4c4d4e4f505152535455565758595a5b5c5d5e5f606162636465666768696a6b6c6d6e6f707172737475767778797a7b7c7d7e7f808182838485868788898a8b8c8d8e8f909192939495969798999a9b9c9d9e9fa0a1a2a3a4a5a6a7a8a9aaabacadaeafb0b1b2b3b4b5b6b7b8b9babbbcbdbebfc0c1c2c3c4c5c6c7c8c9cacbcccdcecfd0d1d2d3d4d5d6d7d8d9dadbdcdddedfe0e1e2e3e4e5e6e7e8e9eaebecedeeeff0f1f2f3f4f5f6f7f8f9fafbfcfdfeff'

    using data sequence number n

    >>> key = ('fffefdfcfbfaf9f8f7f6f5f4f3f2f1f0'.decode('hex'),'22222222222222222222222222222222'.decode('hex'))
    >>> plain ='4444444444444444444444444444444444444444444444444444444444444444'.decode('hex')
    >>> n = '3333333333'.decode('hex')
    >>> cipher = python_Rijndael.new(key,python_Rijndael.MODE_XTS,blocksize=16)
    >>> ciphertext = cipher.encrypt(plain,n)
    >>> ciphertext.encode('hex')
    'af85336b597afc1a900b2eb21ec949d292df4c047e0b21532186a5971a227a89'
    >>> decipher = python_Rijndael.new(key,python_Rijndael.MODE_XTS,blocksize=16)
    >>> decipher.decrypt(ciphertext,n).encode('hex')
    '4444444444444444444444444444444444444444444444444444444444444444'
    """
    return python_Rijndael(key,mode,IV,counter,blocksize,segment_size)

class python_Rijndael(BlockCipher):
    key_error_message = ("Key should be 128, 192 or 256 bits")

    def __init__(self,key,mode,IV,counter,blocksize,segment_size):
        if blocksize not in (16,24,32):
                raise ValueError("Blocksize should be 16, 24 or 32")
        cipher_module = rijndael
        args = {'block_size':blocksize}
        self.blocksize = blocksize
        BlockCipher.__init__(self,key,mode,IV,counter,cipher_module,segment_size,args)

    def keylen_valid(self,key):
        return len(key) in (16,24,32)

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
