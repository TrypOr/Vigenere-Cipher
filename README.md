# Vigenere-Cipher
Vigenere Cipher encryption/decryption and cryptanalysis

You can encrypt a text file by providing the file path with the -e or --encrypt option, and provide the keyword used for encryption with the -k or --keyword option. The 
default keyword is "keyword".

You can decrypt a ciphertext file by providing the file path with the -d or --decrypt option, and provide the keyword used for decryption with the -k or --keyword 
option. The default keyword is "keyword".

You can perform cryptanalysis on a ciphertext file by providing the file path with the -c or --cryptanalysis option. The script will perform cryptanalysis on the 
ciphertext file and try to determine the length of the key used to encrypt it. The method used for finding the length of the key can be specified with the -m or --method 
option. The available methods are "KASISKI" and "IOC".
