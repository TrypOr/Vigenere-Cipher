from collections import Counter
from math import *


alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ."
#Function that repeats key until its the same size of string
def generateKey(string, key): 
        key = list(key)
        #If key length equals string length just return key 
        if len(string) == len(key): 
            return(key) 
        else:
            #Repeat key characters for the difference of string to key
            for i in range(len(string) -len(key)): 
                key.append(key[i % len(key)]) 
        return("" . join(key))
    

#Function that returns all possible key lengths
def possible_keylen(factor_lists):
    #Create list with factors
    all_factors = [factor_lists[lst][fac] for lst in range(len(factor_lists)) for fac in range(len(factor_lists[lst]))]
    #Filter factors smaller than 2 and bigger than 8
    possible_length = list(filter(lambda x:  2 < x <= 8, all_factors))
    #Sort list
    result = sorted(set(possible_length), key=lambda x: all_factors.count(x), reverse=True)
    
    return result

#Function that factorises an integer
def factorise(num):
    return [n for n in range(1, num + 1) if num % n == 0] 

#Function that computes distances between sequences
def compute_distances(distance):
    return [distance[i+1] - distance[i] for i in range(len(distance)-1)]

#Function that splits a string in n parts
def split_string(tmp, n):
    
    for i in range(0, len(tmp), n):
        yield tmp[i:i + n]

#Function that calculates the index of coincidence in the ciphertext
def calculate_IOC(ciphertext):
    common = Counter(ciphertext)
    ioc = 0

    for index in list(alphabet):
      ioc = ioc + (common[index] * (common[index] - 1))
      
    ioc = ioc * 1/len(ciphertext) * 1/(len(ciphertext) - 1)
    return ioc


 
def break_cipher(file_content,key_length):
    temp=[]
    temp.append(list(split_string(file_content,int(len(file_content)/key_length))))
    dict_reader = open("../dictionary_1000.txt", "r")
    dictionary=dict_reader.read().splitlines()
    decrypted_text=""
    for i in range(key_length):
        print("UNIMPLEMENTED")
        exit()
        #print(temp[i])
        #for shift in alphabet:
        
#Function that finds sequences of length in a string(file_content)
def find_seq(file_content,length):
    position = {}  
    for i,garbage in enumerate(file_content):
        next = file_content[i:i+length]
        if next in position.keys():
            position[next].append(i)
        else:
            position[next] = [i]
    repeated = list(filter(lambda x: len(position[x]) >= 2, position))
    rep_position = [(seq, position[seq]) for seq in repeated]
    #If empty return 0
    if not rep_position:
        return 0
    else:    
        return rep_position 