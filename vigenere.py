from math import *
from queue import Empty
import sys
import argparse
from vigenere_functions import*
    
def main(arguments):

    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-e", "--encrypt", help="Encrypt text file", type=argparse.FileType('r'))
    parser.add_argument("-d", "--decrypt", help="Decrypt ciphertext file", type=argparse.FileType('r'))
    parser.add_argument("-k", "--keyword", help="Keyword used for encryption/decryption", default="keyword")
    parser.add_argument("-c", "--cryptanalysis", help="Perform cryptanalysis on the given ciphertext", type=argparse.FileType('r'))
    parser.add_argument("-m", "--method", help="What method should be used for finding the length of the key", default="KASISKI")

    args = parser.parse_args(arguments)

    

    if args.encrypt:
        keyword = args.keyword
        file_content = args.encrypt.read()
        #Change file_content to wanted format uppercase in a single line
        file_content= file_content.upper().replace(" ", "").replace("\n"," ")
        #Generate key to the same size as file_content
        keyword=generateKey(file_content,keyword)
        #Change to uppercase
        keyword=keyword.upper()
        key_as_int = [ord(i) for i in keyword]
        encrypted_text=[]
        for i in range(len(file_content)):
            #If character is not in alphabet do not replace
            if(ord(file_content[i]) in range(0,64) or ord(file_content[i])>123 or ord(file_content[i]) in range(91,96)):
                x=file_content[i]
                encrypted_text.append(x)
            else:
                #Encrypt each letter of the file_content       
                x = (ord(file_content[i]) + key_as_int[i % len(keyword)]) % 26
                x += ord('A')
                encrypted_text.append(chr(x))  
        #Print encrypted result    
        print("" . join(encrypted_text))
    if args.decrypt:
        keyword = args.keyword
        file_content = args.decrypt.read()
        #Change file_content to uppercase
        file_content.upper()
        #Generate key to the same size as file_content#
        keyword=generateKey(file_content,keyword)
        keyword=keyword.upper()
        key_as_int = [ord(i) for i in keyword]
        decrypted_text=[]
        for i in range(len(file_content)):
            #If character is not in alphabet do not replace
            if(ord(file_content[i]) in range(0,64) or ord(file_content[i])>123 or ord(file_content[i]) in range(91,96)):
                x=file_content[i]
                decrypted_text.append(x)
            else:    
                #Decrypt each letter of the file_content       
                x = (ord(file_content[i]) - key_as_int[i % len(keyword)]) % 26
                x += ord('A')
                decrypted_text.append(chr(x))
        #Print decrypted result      
        print("" . join(decrypted_text))
    if args.cryptanalysis:
        file_content = args.cryptanalysis.read()
        #Change file_content to wanted format without spaces in a single line
        file_content= file_content.replace(" ", "").replace("\n"," ")     
        if args.method == "IOC":
            temp=[]
            newlist=[]
            result=[]
            i=0
            #For all possible key lengths
            for key_length in range(2,9):
                newlist.clear()
                #Split file_content in key_length columns
                temp.append(list(split_string(file_content,int(len(file_content)/key_length))))
                #Calculate index of coincidence for each column
                for j in range(key_length):
                    newlist.append(str(calculate_IOC(temp[i][j])))
                i += 1
                #Sort list to save the largest IOC and append to other list
                newlist.sort(reverse=True)
                result.append([key_length,newlist[0]])
            #Sort result to find largest IOC from all key lengths
            result=sorted(result,key=lambda x: (x[1]),reverse=True)
            key_length=result[0][0]
            print("IOC: All posible key lengths are",result[0][0] ,result[1][0],result[2][0],result[3][0],
            "\nThe most possible key length is ",key_length,"with index",result[0][1])
                             
        else:
            factors=[]
            #Find all repeated strings for length 3
            temp = find_seq(file_content, 3)
            i=3
             #Find all repeated strings for all lengths
            while(True):
                i = i + 1
                if find_seq(file_content,i) == 0:
                    break
                else:
                    temp += find_seq(file_content,i)                   
            distances=[]
            for i in range(len(temp)):
                #Calculate distances from each repeated string
                distances.append(compute_distances(temp[i][1])) 
                #Factorise distances   
                for j in distances[i]:
                    factors.append(factorise(j))
            #Key_length is the most possible length        
            key_length=possible_keylen(factors)[0]        
            print("KASISKI: All posible key lengths are",possible_keylen(factors),
            "\nThe most possible key length is ",key_length)
        break_cipher(file_content,key_length)
if __name__ == '__main__':
    main(sys.argv[1:])

