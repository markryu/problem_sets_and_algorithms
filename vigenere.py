
def main():
    """
    Implements the vigenere cipher, which uses keywords for the secret key. The secret key is a word in which represented as index numbers
    The secret key is a word, then transposed as index numbers into an array, adds the index number everytime it iterates through the plain text to produce the cipher text.
    """

    from string import ascii_lowercase as lowercase, ascii_uppercase as uppercase
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("secret_keyword", help="Enter string of text for the secret_keyword")
    args = parser.parse_args()
    try:
        try:
            secret_keyword = int(args.secret_keyword)
            print ("Secret keyword must not contain integers.")
        except:
            secret_keyword = float(args.secret_keyword)
            print ("Secret keyword must not contain floats.")
    except:
        secret_keyword = str(args.secret_keyword)
        key_indices = list()
        for key_char in secret_keyword:
            if key_char in lowercase:
                index_number = 0
                for lower_chars in lowercase:
                    if key_char == lower_chars:
                        key_index = index_number
                        break
                    index_number += 1
            elif key_char in uppercase:
                index_number = 0
                for upper_chars in uppercase:
                    if key_char == upper_chars:
                        key_index = index_number
                        break
                    index_number += 1
            else:
                print ("The key contains unsupported characters. Only use alphabet characters.")
            key_indices.append(key_index)
        plain_text = str(input("plain_text: "))
        print (key_indices)


if __name__=='__main__':
    main()
