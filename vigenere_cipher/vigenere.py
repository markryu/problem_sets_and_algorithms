
def main():
    """
    Implements the vigenere cipher, which uses keywords for the secret key. The secret key is a word in which represented as index numbers
    The secret key is a word, then transposed as index numbers into an array, adds the index number everytime it iterates through the plain text to produce the cipher text.
    It's a one way cipher.
    """

    import sys
    argv = sys.argv

    if len(argv) != 2 or argv[1].isalpha() != True:
        sys.exit("Usage: python vigenere.py cipher")
    secret_keyword = str(argv[1])

    secret_key = list()
    for key_char in secret_keyword:
        secret_key.append(ord(key_char.lower()) - 97)

    plain_text = input('plain_text: ')
    plain_text_mapping = list()
    for char in plain_text:
        plain_text_mapping.append(ord(char))
    key_index = 0
    all_cipher = str()
    max_length = len(secret_key)
    for ascii_number in plain_text_mapping:
        if key_index >= max_length:
            key_index = 0 
        if chr(ascii_number).isalpha():
            if chr(ascii_number).islower():
                cipher_char = chr(((((ascii_number - 97) + secret_key[key_index]) % 26) + 97))
            else:
                cipher_char = chr(((((ascii_number - 65) + secret_key[key_index]) % 26) + 65))
            key_index += 1
        else:
            cipher_char = (chr(ascii_number))

        all_cipher += cipher_char
        
    print (f"ciphertext: {all_cipher}\n")


if __name__=='__main__':
    main()
