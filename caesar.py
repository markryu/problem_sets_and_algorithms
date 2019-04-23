
def main():
    """ pseudocode
    Provide a commandline argument where the program asks a command line argument, preferrably an integer which will then become the secret key
    The program then asks for a plaintext which then the program prints out the ciphertext after entering the plaintext
    The program will only rotate alphabetical letters, and will copy as is the punctuation marks
    """
    
    from string import ascii_lowercase as lowercase, ascii_uppercase as uppercase
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("secret_key", help="Provide secret key as an integer.")
    args = parser.parse_args()
    try:
        secret_key = int(args.secret_key) % 26
        plain_text = str(input("plaintext: "))
        ciphertext = str()
        for plaintext_char in plain_text:
            if plaintext_char in lowercase:
                lowercase_index = 0
                for each_index in lowercase:
                    if plaintext_char == each_index:
                        cipher_index = lowercase_index + secret_key 
                        cipher_index = cipher_index % 26
                        cipher_char = lowercase[cipher_index]
                    lowercase_index += 1

            elif plaintext_char in uppercase:
                uppercase_index = 0
                for each_index in uppercase:
                    if plaintext_char == each_index:
                        cipher_index = uppercase_index + secret_key 
                        cipher_index = cipher_index % 26
                        cipher_char = uppercase[cipher_index]
                    uppercase_index += 1
            else:
                cipher_char = plaintext_char

            ciphertext = ciphertext + cipher_char
        print (f"Cipher text is: {ciphertext}")
    except:
        print ("\nArgument secret key must be an integer")


if __name__ == '__main__':
    main()
