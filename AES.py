from Crypto.Cipher import AES
import sys

class AESinterface:
    @staticmethod
    def setKey(key):
        if (all(ord(c) < 128 for c in key)) and (len(key) == 16):
            global aes
            aes = AES.new(key, AES.MODE_ECB)
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
