
def main():
    """ pseudocode
    Provide a commandline argument where the program asks a command line argument, preferrably an integer which will then become the secret key
    The program then asks for a plaintext which then the program prints out the ciphertext after entering the plaintext
    The program will only rotate alphabetical letters, and will copy the punctuation marks as is.
    """
    
    from sys import argv

    secret_key = int(argv[1])
    if len(argv) < 2:
        sys.exit("Usage: python caesar.py k")
    try:
        plain_text = input("plaintext: ")
        ciphertext = str()
        uppercase_index = -1
        for idx, plaintext_char in enumerate(plain_text):
            if plaintext_char.isalpha():
                if plaintext_char.isupper():
                    uppercase_index = idx
                iterate_char = plaintext_char.lower()
                for i, letters in enumerate(range(97,123)):
                    if iterate_char == chr(letters):
                        cipher_char = chr(97 +(i+ secret_key) % 26)
                        if uppercase_index == idx:
                            cipher_char = cipher_char.upper()
            else:
                cipher_char = plaintext_char

            ciphertext = ciphertext + cipher_char
        print(f"ciphertext: {ciphertext}")
    except:
        print("Usage: python caesar.py k")




if __name__ == '__main__':
    main()
