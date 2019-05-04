def main():
    hash = "#"
    space = ' '
    endFlag = False
    while endFlag == False:
        try:
            number = int(input("Enter Number: "))
            if number >= 1 and number <= 8:
                endFlag = True
        except:
            endFlag = False
    for each in range(number):
        hashes = each + 1
        print(f"{(number-1)*space}{hashes*hash}  {hashes*hash}")
        number -= 1




if __name__=='__main__':
    main()
