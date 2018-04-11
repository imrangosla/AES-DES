from Crypto.Cipher import DES
import sys

class DESinterface:
    @staticmethod
    def setKey(key):
        if (all(ord(c) < 128 for c in key)) and (len(key) == 16):
            key = key.decode("hex")
            global des
            des = DES.new(key, DES.MODE_ECB)
        else:
            print "Wrong Key"
            sys.exit()

    @staticmethod
    def encrypt(plainText):
        cipherText = ""
        plainText = plainText.rstrip()
        blocks=[plainText[x:x+8] for x in range(0,len(plainText),8)]
        for elements in range(len(blocks)):
            while (len(blocks[elements]) % 8) != 0:
                blocks[elements] += '*'
            cipherText += des.encrypt(blocks[elements])
        return cipherText.rstrip()

    @staticmethod
    def decrypt(cipherText):
        plainText = ""
        cipherText = cipherText.rstrip()
        blocks=[cipherText[x:x+8] for x in range(0,len(cipherText),8)]
        for elements in range(len(blocks)):
            plainText += des.decrypt(blocks[elements])
        return plainText.rstrip()
