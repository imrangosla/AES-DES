from Crypto.Cipher import AES
import sys
# AES accepts as 128-bit (i.e. 16 byte) plaintext block,
# a 128, 192, or 256-bit key, and produces
# a 128-bit ciphertext block.

class AESinterface:
    @staticmethod
    def setKey(key):
        #each hex character is 4 bits so 4 * 32 = 128 bit key
        #32 characters representing a 128-bit hexadecimal number
        #ord(c)-returns the ASCII value of c
        #all() returns true if all elements of the iterable are true
        #or if iterable is empty
        #the range in ascii of a-f is 97-102
        #the range in ascii of 0-9 is 48 through 57

        #0-9, a-f string key
        asciiRange = (range(48,58) + range(97,103))
        if (all(ord(c) in asciiRange for c in key)) and (len(key) == 32):
        #if (all(ord(c) < 128 for c in key)) and (len(key) == 32):
            # global aes
            #  aes = AES.new(key, AES.MODE_ECB)
            # key = key.decode("hex")
            hexKey=[key[x:x+2] for x in range(0,len(key),2)]

            for i in range(len(hexKey)):
                hexKey[i] = '\\x'+hexKey[i]
            print hexKey
            newKey =''
            for i in range(len(hexKey)):
                newKey += hexKey[i]
            print('newKey: ', newKey)
            global aes
            aes = AES.new(newKey, AES.MODE_ECB)
        else:
            print "Wrong Key"
            sys.exit()

    @staticmethod
    def encrypt(plainText):
        cipherText = ""
        plainText = plainText.rstrip()
        blocks=[plainText[x:x+16] for x in range(0,len(plainText),16)]
        for elements in range(len(blocks)):
            while (len(blocks[elements]) % 16) != 0:
                blocks[elements] += '*'
            cipherText += aes.encrypt(blocks[elements])
        return cipherText

    @staticmethod
    def decrypt(cipherText):
        plainText = ""
        cipherText = cipherText.rstrip()
        blocks=[cipherText[x:x+16] for x in range(0,len(cipherText),16)]
        for elements in range(len(blocks)):
            plainText += aes.decrypt(blocks[elements])
        return plainText
