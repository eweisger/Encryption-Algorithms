import string
import os
import pickle
import numpy


def make_enc_key(offset):
    char = []
    for i in range(len(string.ascii_uppercase)):
        char.append(string.ascii_uppercase[i])
    key = {}
    for i in range(len(char)):
        j = (i + offset) % len(char)
        key[ char[i] ] = char[j]
    print(key)
    return key

def encrypt(message, key):
    for i in range(len(message)):
        if message[i] not in string.ascii_letters + ' ':
            raise Exception("{0} is not a valid charcter to encrypt.".format(message[i]))
    message = message.upper()
    cyphertext = ''
    for i in range(len(message)):
        if message[i] == ' ':
            cyphertext += " "
        else:
            cyphertext += key[ message[i] ]

    return cyphertext


def make_dec_key(offset):
    char = []
    for i in range(len(string.ascii_uppercase)):
        char.append(string.ascii_uppercase[i])
    key = {}
    for i in range(len(char)):
        j = (i + offset) % len(char)
        key[ char[j] ] = char[i]
    print(key)
    return key

def get_or_create_dec_key():
    ekey = get_or_create_enc_key()
    print("orig key: {0}".format(ekey))
    key = dict([[v,k] for k,v in ekey.items()])
    return key


def get_or_create_enc_key():
    if os.path.isfile('enc.key'):
        with open('enc.key','rb') as fd:
            return pickle.load(fd)
    else:
        char = []
        for i in range(len(string.ascii_uppercase)):
            char.append(string.ascii_uppercase[i])
        vals = numpy.random.permutation(char)
        key = {}
        for i in range(len(char)):
            key[ char[i] ] = vals[i]
        print(key)
        with open('enc.key','wb') as fd:
            pickle.dump(key,fd)
        return key
        


if __name__ == "__main__":
    en_or_de = input("Encrpyt(1) or decrypt(2)")
    if en_or_de == '1':
        #offset = input("Enter Offset (int):")
        key = get_or_create_enc_key()
        #key = make_enc_key(int(offset))
        cyphertext = encrypt(input("Enter Message:"), key)
        print( cyphertext )
    else:
        #offset = input("Enter Offset (int):")
        key = get_or_create_dec_key()
        #key = make_dec_key(int(offset))
        plaintext = encrypt(input("Enter CypherText:"), key)
        print( plaintext)

