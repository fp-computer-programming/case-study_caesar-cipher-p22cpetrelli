#author CJP (AMDG) 05/19/22
from string import ascii_uppercase

#main function
def cipher_key(shift):
    original_letters = ascii_uppercase
    shifted_letters = ascii_uppercase[int(shift):] + ascii_uppercase[:int(shift)]

    return dict(zip(original_letters, shifted_letters))

def shift_line(line, key):
    new_line = ""
    for letter in line: 
        #will keep the spaces
        if letter == " ":
            new_line = new_line + " "
            continue
        elif letter == "\n":
            new_line = new_line + "\n" 
            #will keep the indentation in file
            continue
        elif letter == "!" or letter == "," or letter == "'":
            new_line = new_line + letter
            continue
        letter = letter.upper()
        
        #returns new encrypted message
        new_line = new_line + key[letter]
    
    return new_line

def encrypt_message(name, key):
    fixed = []
    final = ""
    with open(name) as file:
        for line in file:
            fixed += shift_line(line,key) 
            #uses key to encrypt
        for lines in fixed:
            final = final + lines
        file = open("encrypted_test.txt","w")
        file.write(final) 
        #adds to final code
        file.close()

#main functions
user_file = input("Please enter a file to be encrypted: ")
shift_value = input("Please enter a shift value: ")

key = cipher_key(shift_value)

encrypt_message(user_file, key)