from Crypto.Cipher import DES
import sys

class DESinterface:
    @staticmethod
    def setKey(key):
        asciiRange = (range(48,58) + range(97,103))
        if (all(ord(c) in asciiRange for c in key)) and (len(key) == 16):
            key = key.decode("hex")
            global des
            des = DES.new(key, DES.MODE_ECB)
        else:
            print "Wrong Key"
            sys.exit()

    @staticmethod
    def encrypt(plainText):
        cipherText = ""
        pad = 0
        padBlock = ""
        plainText = plainText.rstrip()
        blocks=[plainText[x:x+8] for x in range(0,len(plainText),8)]
        for elements in range(len(blocks)):
            while (len(blocks[elements]) % 8) != 0:
                blocks[elements] += '*'
                pad += 1
            cipherText += des.encrypt(blocks[elements])
        cipherText += des.encrypt(str(pad).zfill(8))
        return cipherText.rstrip()

    @staticmethod
    def decrypt(cipherText):
        plainText = ""
        pad = 0
        cipherText = cipherText.rstrip()
        blocks=[cipherText[x:x+8] for x in range(0,len(cipherText),8)]
        for elements in range(len(blocks)):
            if elements == (len(blocks) - 1):
                pad = des.decrypt(blocks[elements])
            else:
                plainText += des.decrypt(blocks[elements])
        return plainText[:-int(pad)].rstrip()
