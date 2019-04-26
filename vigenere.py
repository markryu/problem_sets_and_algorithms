
def main():
    """
    Implements the vigenere cipher, which uses keywords for the secret key. The secret key is a word in which represented as index numbers
    The secret key is a word, then transposed as index numbers into an array, adds the index number everytime it iterates through the plain text to produce the cipher text.
    It's a one way cipher.
    """

    import sys
    from string import ascii_lowercase as lowercase, ascii_uppercase as uppercase
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("secret_keyword", help="Enter string of text for the secret_keyword")
    args = parser.parse_args()

    secret_keyword = str(args.secret_keyword)
    secret_key = list()
    ascii = lowercase + uppercase
    for key_char in secret_keyword:
        index_number = ascii.find(key_char) if key_char in ascii else sys.exit()
        secret_key.append(index_number)

    plain_text = input('plain_text: ')
    plain_text_mapping = list()
    for each_plain_char in plain_text:
        index_number = ascii.find(each_plain_char) if each_plain_char in ascii else each_plain_char
        plain_text_mapping.append(index_number)
    key_index = 0
    all_cipher = list()
    max_length = len(secret_key) - 1
    for ascii_position in plain_text_mapping:
        if key_index > max_length:
            key_index = 0
        if type(ascii_position) == int:
            if ascii_position >= 26:
                cipher_number = ascii_position + secret_key[key_index] 
                if cipher_number >= 52:
                    cipher_number = (key_index % 52) + 26
                key_index += 1
            else:
                cipher_number = ascii_position + secret_key[key_index]
                if cipher_number >= 26:
                    cipher_number %= 26 
                key_index += 1 
        else:
            cipher_number = ascii_position
        all_cipher.append(cipher_number) 
         
    final_print = str()
    for each_cipher_char in all_cipher:
        printable = ascii[each_cipher_char] if type(each_cipher_char) == int else each_cipher_char
        final_print += printable 
    print (f"cipher_text: {final_print}")


if __name__=='__main__':
    main()
