#include <string>
#include "CipherInterface.h"
#include "DES.h"
#include "AES.h"
#include <fstream>
#include <iostream>

#ifndef __HP_aCC
using namespace std;
#endif

/* Error handling for cipher creation */
void errorCheck(CipherInterface*);

/* Sets the key, perfroms encryption/decryption and writes to the output file */
void cryptoDriver(CipherInterface*, string, string, string, string);

int main(int argc, char** argv)
{
	if (argc != 6)
		return -1;

	/* Code for parsing the command line parameters */
	string cipherName = argv[1];
	unsigned char* key = reinterpret_cast<unsigned char*> (argv[2]);
	string encDec = argv[3];
	string inputFile = argv[4];
	string outputFile = argv[5];

	/* Code for reading the file */
	fstream stream(inputFile.c_str());
	string content((istreambuf_iterator<char>(stream)),(istreambuf_iterator<char>()));
	stream.close();

	/* An interface class */
	CipherInterface* cipher = NULL;

	if (cipherName == "DES")
	{
		/* Create an instance of the Playfair cipher */
		cipher = new DES();
		errorCheck(cipher);
		cryptoDriver(cipher, key, encDec, outputFile, content);
	}
	else if (cipherName == "AES")
	{
		cipher = new AES();
		errorCheck(cipher);
		cryptoDriver(cipher, key, encDec, outputFile, content);
	}
	else
	{
		cout << "Invalid Cipher" << endl;
		return -1;
	}

	return 0;
}

void errorCheck(CipherInterface * cipher)
{
	/* Error checks */
	if (!cipher)
	{
		fprintf(stderr, "ERROR [%s %s %d]: could not allocate memory\n",
			__FILE__, __FUNCTION__, __LINE__);
		exit(-1);
	}
}

void cryptoDriver(CipherInterface * cipher, unsigned char* key, string encDec, string outputFile, string content)
{
	ofstream outFile;
	outFile.open(outputFile.c_str());

	/* Set the encryption key */
	if (cipher->setKey(key))
	{
		if (encDec == "ENC")
		{
			/* Perform encryption */
			string cipherText = cipher->encrypt(content);
			outFile << cipherText;
			cout << "Encryption Successful" << endl;
		}
		else if (encDec == "DEC")
		{
			/* Perform decryption */
			string plainText = cipher->decrypt(content);
			outFile << plainText;
			cout << "Decryption Successful" << endl;
		}
	}
	else
		cout << "Invalid Key" << endl;

	outFile.close();
}
