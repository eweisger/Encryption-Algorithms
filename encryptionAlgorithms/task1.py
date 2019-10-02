#Emma Weisgerber
#CSCI 373: Intro to Cyber Security - Dr. Brian Drawert
#Homework 2: Cryptography - 2/18/19
#-----------------------------------------------------
#Program that implements the Caesarian Shift substitution cypher
#Uses the character set of ASCII code 32 through 126 for a total of 95 characters, and ignores the new line character
#Using an offset of 19 it reads in the task1 encrypted message and writes out the decrypted message
#Stack overflow and man pages were referenced

import string

def caesarian_shift():
    offset = 19

    with open("task1_encrypted_message.txt", "r") as input_message:
        encrypted_message = input_message.read()
        decrypted_message = decrypt(encrypted_message, offset)

    with open("task1_decrypted_message.txt", "w") as output_message:
        output_message.write(decrypted_message)

    #Used to test encryption
    #with open("test_encryption.txt", "w") as test:
        #test.write(encrypt(decrypted_message, offset))


def decrypt(cyphertext, offset):
    key = decryption_key(offset)
    character_set = [chr(i) for i in range(32, 127)]

    #For each character in the cyphertext, check to make sure it's a valid character
    for i in range(len(cyphertext)):
        if cyphertext[i] not in '\n'.join(character_set):
            print("Invalid character: {}".format(cyphertext[i]))
            return

    #For each character in the cyphertext, decrypt the character using the key and replace it with the unencrypted character, ignoring the new line character
    plaintext = ''
    for i in range(len(cyphertext)):
        if cyphertext[i] == '\n':
            plaintext += "\n"
        else:
            plaintext += key[cyphertext[i]]
    return plaintext


def decryption_key(offset):
    character_set = [chr(i) for i in range(32, 127)]

    #Create key for each encrypted character with its corresponding unencrypted character within the character set
    key = {}
    for i in range(len(character_set)):
        j = (i + offset) % len(character_set)
        key[character_set[j]] = character_set[i]
    return key


def encrypt(plaintext, offset):
    key = encryption_key(offset)
    character_set = [chr(i) for i in range(32, 127)]

    #For each character in the plaintext, check to make sure it's a valid character
    for i in range(len(plaintext)):
        if plaintext[i] not in '\n'.join(character_set):
            print("Invalid character: {}".format(plaintext[i]))
            return

    #For each character in the plaintext, encrypt the character using the key and replace it with the encrypted character, ignoring the new line character
    cyphertext = ''
    for i in range(len(plaintext)):
        if plaintext[i] == '\n':
            cyphertext += "\n"
        else:
            cyphertext += key[plaintext[i]]
    return cyphertext


def encryption_key(offset):
    character_set = [chr(i) for i in range(32, 127)]

    #Create key for each character with its corresponding encrypted character within the character set
    key = {}
    for i in range(len(character_set)):
        j = (i + offset) % len(character_set)
        key[character_set[i]] = character_set[j]
    return key


if __name__ == "__main__":
   caesarian_shift()
