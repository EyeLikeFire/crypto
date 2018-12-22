def alphabet_position(letter):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                'h', 'i', 'j', 'k', 'l', 'm', 'n', 
                'o', 'p','q', 'r', 's', 't', 'u', 
                'v', 'w', 'x', 'y', 'z']
    letter = letter.lower()
    result = alphabet.index(letter)
    return result

def rotate_character(char, rot):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                'h', 'i', 'j', 'k', 'l', 'm', 'n', 
                'o', 'p','q', 'r', 's', 't', 'u', 
                'v', 'w', 'x', 'y', 'z']

    if char.isalpha():
        index = alphabet_position(char)
        index += rot 
        index = index % 26
        letter = alphabet[index]

        if char.isupper():
            letter = letter.upper()
        return letter
    else:
        return char