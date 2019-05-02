def main():
    take_input = getInput()
    number = take_input[0]
    allSum = sumSeconds(number) + sumOthers(number)
    checkSum(allSum, take_input)
    
def getInput():
    import sys
    flag = False
    invalid = False
    while flag == False:
        try:
            number_input = int(input("Number: "))
            number = str(number_input)
            if number[:2] == '34' or number[:2] == '37' and len(number) == 15:
                brand = "AMEX\n"
                flag = True
            elif number[:2] == '51' or number[:2] == '52'  or number[:2] == '53' or number[:2] == '54' or number[:2] == '55' and len(number) == 16:
                flag = True
                brand = "MASTERCARD\n"
            elif number[0] == '4' and (len(number) == 16 or len(number) == 13):
                flag = True
                brand = "VISA\n" 
            elif len(number) < 13:
                invalid = True
                flag = True
            else:
                flag = False
        except:
            None 
    if invalid == True:
        sys.exit("INVALID")
    else:
        return number, brand


def sumOthers(number):
    length =  (len(number) + 1) * -1
    indices = list()
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

def checkSum(allSum, take_input):
    if allSum % 10 == 0:
        print (take_input[1])

    else:
        print("INVALID\n.")
        main()


if __name__=='__main__':
    main()
