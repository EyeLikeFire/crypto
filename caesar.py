# #case insensitive caesars cypher using user input for rotation
# def caesar_encode(scrt, rot):
    
#     encoded_list = []
#     secret_list = []
#     alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
#      'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
#       'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     #convert the string into a list
#     for i in range(len(scrt)):
#         secret_list.append(scrt[i])

#     #letter.isalpha() == Bool
#     #if .isupper() == True, letter.lower(), if True letter.upper
#     #letter.index() == int
#     for i in secret_list:
#         if i.isalpha():
#             up_down = False
#             #do cypher stuff here
#             if i.isupper():
#                 up_down = True
#                 i = i.lower()
#             letter_index = alphabet.index(i)
#             scramble = (rot + letter_index) % 26

#             if up_down:
#                 up = (alphabet[scramble]).upper()
#                 encoded_list.append(up)
#             else:
#                 encoded_list.append(alphabet[scramble]) 

#         else:
#             #add all non alpha numbers as is 
#             encoded_list.append(i)
#     string_encoded = ''.join(encoded_list)
#     return(string_encoded)

from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    letter_list = []
    crypto_string = ""
    for letter in range(len(text)):
        char = text[letter]
        char = rotate_character(char, rot)
        letter_list.append(char)
    for i in letter_list:
        crypto_string += i
    return crypto_string


def main():
    from sys import argv, exit
    if not(argv[1].isdigit()):
        print("usage: python caesar.py n")
        exit()
    #do stuff
    message = input("Type a message:")
    #print(message)
    #rotation = int(input("Rotate by:"))
    rotation = int(argv[1])
    print(encrypt(message, rotation))


if __name__ == "__main__":
    main()

#def main():
    #get user input
    #secret = "Aa Bb Cc Dd Ee Ff Gg Hh Ii Jj Kk Ll Mm Nn Oo Pp..."
    #rot = 2
    #secret = input("Enter your secret message!")
    #rot = int(input("enter a secret number"))

    #caesar_encode(secret, rot)

#if __name__ == "__main__":
#    main()
