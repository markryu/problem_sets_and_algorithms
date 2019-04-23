
def main():
    """
    get a valid credit card number
    multiply each other digit by 2 from 2nd to the last digit
    add the products and the unmultiplied digits 
    check the sum if the last digit is zero 
    sum modulo 10 must be zero
    
    american express uses 15 digit numbers starts with 34 or 37
    mastercard uses 16 starts with 51, 52,53, 54, 55
    visa uses 13 or 16 starts with 4
    """

    number = getInput()[0]
    allSum = sumSeconds(number) + sumOthers(number)
    checkSum(allSum, number)
    print ("Press <Enter> to exit")
    input()
    
def getInput():
    flag = False
    while flag == False:
        try:
            number_input = int(input("Number: "))
            number = str(number_input)
            if number[:2] == '34' or number[:3] == '37' and len(number) == 15:
                brand = "AMEX"
                flag = True
            elif number[:2] == '51' or number[:3] == '52'  or number[:3] == '53' or number[:3] == '54' or number[:3] == '55' and len(number) == 16:
                flag = True
                brand = "MASTERCARD"
            elif number[0] == '4' and (len(number) == 16 or len(number) == 13):
                flag = True
                brand = "VISA" 
            else:
                flag = False
        except:
            None
    return number, brand

def sumOthers(number):
    length =  (len(number) + 1) * -1
 False   indices = list()
    for index in number[-1:length:-2]:
        index = int(index)
        indices.append(index)
    return sum(indices)


def sumSeconds(number):
    length =  (len(number) + 1) * -1
    all_second_indices = list()
    for second_index in number[-2:length:-2]:
        second_index = int(second_index)
        second_index *= 2
        stringed_index = str(second_index)
        if len(stringed_index) >= 2:
            for each in stringed_index:
                numbered = int(each)
                all_second_indices.append(numbered)
        else:
            all_second_indices.append(second_index)

    return sum(all_second_indices)

def checkSum(allSum, number):
    if allSum % 10 == 0:
        print ("Card Number is Valid")
        print (number[1])

    else:
        print("Checksum mismatch.")
        main()


if __name__=='__main__':
    main()
