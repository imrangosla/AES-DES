from Crypto.Cipher import DES
import sys

class DESinterface:
    @staticmethod
    def setKey(key):
        if (all(ord(c) < 128 for c in key)) and (len(key) == 8):
            global des
            des = DES.new(key, DES.MODE_ECB)
        else:
            print "Wrong Key"
            sys.exit()

    @staticmethod
    def encrypt(plainText):
        plainText = plainText.rstrip()
        while (len(plainText) % 8) != 0:
            plainText += '*'
        return des.encrypt(plainText)

    @staticmethod
    def decrypt(cipherText):
        return des.decrypt(cipherText)
