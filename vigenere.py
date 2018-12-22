from helpers import alphabet_position, rotate_character


def encrypt(message, code):
    #1. convert __code__ into numbers ()
    rot_list = []
    message_list = []
    message_string = ""
    for i in code:
        rot_list.append(alphabet_position(i))
    #2. reduce message into individual charactors 
    for i in message:
        message_list.append(i)

    #3. rotate letters
    rot_index = 0 #This will be used to itterate through the 'key'
    for i in message_list:

        if i.isalpha():
            b = rot_list[rot_index]
            a = rotate_character(i, b)
            message_string += a
            rot_index += 1
            rot_index = rot_index % len(rot_list) #Using a modulo function to rotate through the 'key'

        else:
        #4. skip non alpha charactors 
            message_string += i

    return message_string


def main():
    from sys import argv
    #if no key is entered:
    if len(argv) < 2:
        key = input("Encryption key:")
    #if a non-alpha key is entered:
    elif not(argv[1].isalpha()):
        print("usage: python vigenere.py key")
        exit()
    #if a key is entered:
    else:
        key = str(argv[1])

    # Type a message:
    message = input("Type a message:")
    #print encrypted message
    print(encrypt(message, key))

if __name__ == "__main__":
    main()

# encrypt
# Now that you have your helper functions, go ahead and write a new version of the encrypt function which uses the Vigenere cipher rather than Caesar.

# Your first step is to figure out what the function signature should say. How should it be different from the Caesar version, def encrypt(text, rot)?

# As usual, don’t move on until you have tested your function against a lot of different inputs and seen the results you expect.