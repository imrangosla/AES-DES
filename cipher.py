import sys
from DES import DESinterface
from AES import AESinterface

cipherName = sys.argv[1]
key = sys.argv[2]
encDec = sys.argv[3]
input = sys.argv[4]
output = sys.argv[5]

input = open(input, 'r')
output = open(output, 'r+')

print len(sys.argv)

#learn dictionaries
def Main():
    if cipherName == "DES":
        cipher = DESinterface()
        plainText = input.read()
        cipher.setKey(key)
        if encDec == "ENC":
            output.write(cipher.encrypt(plainText))
        elif encDec == "DEC":
            output.write(cipher.decrypt(plainText))
        else:
            print "Choose ENC or DEC"
    elif cipherName == "AES":
        cipher = AESinterface()
        plainText = input.read()
        cipher.setKey(key)
        if encDec == "ENC":
            output.write(cipher.encrypt(plainText))
        elif encDec == "DEC":
            output.write(cipher.decrypt(plainText))
        else:
            print "Choose ENC or DEC"
    else:
        print "Incorrect Cipher"



if __name__ == "__main__":
    Main()
