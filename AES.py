from Crypto.Cipher import AES

class AESinterface:
    @staticmethod
    def setKey(key):
        global aes
        aes = AES.new(key, AES.MODE_ECB)

    @staticmethod
    def encrypt(plainText):
        plainText = plainText.rstrip()
        while (len(plainText) % 16) != 0:
            plainText += '*'
        return aes.encrypt(plainText)

    @staticmethod
    def decrypt(cipherText):
        return aes.decrypt(cipherText)
