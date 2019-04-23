def main():
    hash = "#"
    space = ' '
    number = getNumber()
    for each in range(number):
        hashes = each + 1
        print (f"{number*space}{hashes*hash}  {hashes*hash}")
        number -= 1

def getNumber():
    endFlag = False
    while endFlag == False:
        try:
            number = int(input("Enter Number: "))
            if number >= 1 and number <= 8:
                endFlag = True
        except:
            endFlag = False
    return number

if __name__=='__main__':
    main()
