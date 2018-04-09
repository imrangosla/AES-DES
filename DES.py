from Crypto.Cipher import DES

class DESinterface:
    @staticmethod
    def setKey(key):
        global des
        des = DES.new(key, DES.MODE_ECB)

    @staticmethod
    def encrypt(plainText):
        plainText = plainText.rstrip()
        while (len(plainText) % 8) != 0:
            plainText += '*'
        return des.encrypt(plainText)

    @staticmethod
    def decrypt(cipherText):
        return des.decrypt(cipherText)
