def alphabet_position(letter):
    lower_string = 'abcdefghijklmnopqrstuvwxyz'
    upper_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if letter in lower_string:
        return lower_string.find(letter)
    elif letter in upper_string:
        return upper_string.find(letter)

def rotate_character(char, rot):
    lower_string = 'abcdefghijklmnopqrstuvwxyz'
    upper_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if char in lower_string:
        new_pos = alphabet_position(char) + (rot % 26)
        return lower_string[new_pos % 26]
    elif char in upper_string:
        new_pos = alphabet_position(char) + (rot % 26)
        return upper_string[new_pos % 26]
    else:
        return char
        
def encrypt(string, rot):
    encrypted_string = ''
    for char in string:
        result = rotate_character(char, rot)
        encrypted_string = encrypted_string + result
    return encrypted_string

def main():
    string = input("Please enter a phrase you want to encrypt.")
    rot = int(input("Please enter a number (in integer form) of letters you want to rotate by."))
    print(encrypt(string, rot))

if __name__ == '__main__':
    main()