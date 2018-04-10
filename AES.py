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
        plainText = plainText.rstrip()
        while (len(plainText) % 16) != 0:
            plainText += '*'
        return aes.encrypt(plainText)

    @staticmethod
    def decrypt(cipherText):
        return aes.decrypt(cipherText)
