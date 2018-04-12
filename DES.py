from Crypto.Cipher import DES
import sys

class DESinterface:
    @staticmethod
    #NEED TO FIX THIS
    def setKey(key):
        if (all(ord(c) < 128 for c in key)) and (len(key) == 16):
            key = key.decode("hex")
            print key
            global des
            des = DES.new(key, DES.MODE_ECB)
        else:
            print "Wrong Key"
            sys.exit()

    @staticmethod
    def encrypt(plainText):
        cipherText = ""
        plainText = plainText.rstrip()
        #takes the plaintext and forevery 8 bits creates an element in the blocks array
        blocks=[plainText[x:x+8] for x in range(0,len(plainText),8)]
        for elements in range(len(blocks)):
            while (len(blocks[elements]) % 8) != 0:
                #pad the block every 8 bits with an * for the remainder of characters not divisible
                #by 8
                blocks[elements] += '*'
            #we instantianted the des object in the setKey function call, and
            #here we are encrypting it from the blocks of 8 bit chunks of the plaintext
            #and appending to the string ciphertext
            cipherText += des.encrypt(blocks[elements])
        return cipherText

    @staticmethod
    def decrypt(cipherText):
        plainText = ""
        cipherText = cipherText.rstrip()
        blocks=[cipherText[x:x+8] for x in range(0,len(cipherText),8)]
        for elements in range(len(blocks)):
            plainText += des.decrypt(blocks[elements])
        return plainText
