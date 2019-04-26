""" If initial number is less than 26, then use as is and if over 26, get remainder of 26, if more then 26, then divide it by 26 then add 26"""

def main():
    """

    Implements the vigenere cipher, which uses keywords for the secret key. The secret key is a word in which represented as index numbers
    The secret key is a word, then transposed as index numbers into an array, adds the index number everytime it iterates through the plain text to produce the cipher text.

    """
    import sys

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
        secret_key = list()
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
                sys.exit()
            secret_key.append(key_index)

        max_key_number = len(secret_key)
        plain_text = input('plain_text: ')
        plain_text_mapping = list()
        cipher_number = 0
        for each_plain_char in plain_text:
            if each_plain_char in lowercase:
                index_number = 0 
                for lower_chars in lowercase:
                    if each_plain_char == lower_chars:
                        plain_cipher = index_number
                        break
                    index_number += 1
            elif each_plain_char in uppercase:
                index_number = 26 
                for upper_chars in uppercase:
                    if each_plain_char == upper_chars:
                        plain_cipher = index_number
                        break
                    index_number += 1
            else:
                index_number = each_plain_char
            plain_text_mapping.append(index_number)
        count = 0
        all_cipher = list()
        max_length = len(secret_key) - 1
        for each_index in plain_text_mapping:
            if count > max_length:
                count = 0
            if type(each_index) == int:
                if each_index >= 26:
                    cipher_index = each_index + secret_key[count] 
                    if cipher_index >= 52:
                        cipher_index = cipher_index % 52
                        cipher_index = cipher_index + 26
                    count += 1
                else:
                    cipher_index = each_index + secret_key[count]
                    if cipher_index >= 26:
                        cipher_index = cipher_index % 26
                    count += 1 
            else:
                cipher_index = each_index
            all_cipher.append(cipher_index) 
             
        final_print = str()
        uppercase = lowercase + uppercase
        for each_cipher_char in all_cipher:
            if type(each_cipher_char) == int:
                if each_cipher_char >= 26:
                    printable = uppercase[each_cipher_char]
                else:
                    printable = lowercase[each_cipher_char]
            else:
                printable = each_cipher_char
            final_print += printable 
        print (f"cipher_text: {final_print}")


if __name__=='__main__':
    main()
