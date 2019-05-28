def main():
    flag = False
    while flag == False:
        try:
            number_input = int(input("Number: "))
            number = str(number_input)
            if number[:2] == '34' or number[:2] == '37' and len(number) == 15:
                brand = "AMEX\n"
            elif number[:2] == '51' or number[:2] == '52' or number[:2] == '53' or number[:2] == '54' or number[:2] == '55' and len(number) == 16:
                brand = "MASTERCARD\n"
            elif number[0] == '4' and (len(number) == 16 or len(number) == 13):
                brand = "VISA\n" 
            else:
                brand = "None"
            flag = True
        except:
            flag = False
   
    length =  (len(number) + 1) * -1
    indices = list()
    for index in number[-1:length:-2]:
        index = int(index)
        indices.append(index)

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

    allSum = sum(all_second_indices) + sum(indices)
 
    if len(number) < 13:
        print ("INVALID\n")
    elif allSum % 10 == 0:
        print (brand)
    else:
        print("INVALID\n")


if __name__=='__main__':
    main()
