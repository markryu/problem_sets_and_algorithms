
def main():
    '''gets the fibonacci sequence whose values do not exceed four million, find 
    the sum of the even-valued terms.
    This function assumes it started at 0'''
    preceeding_number = 0
    current_number = 1
    even_list = list()
    while current_number < 4000000:
        sum_of_two = preceeding_number + current_number
        preceeding_number = current_number
        current_number = sum_of_two
        if current_number % 2 == 0:
            even_list.append(current_number)
    print (f"The total sum of all even numbers from the fibonacci sequence less than 4 million is {sum(even_list)}")
    return sum(even_list)
        

if __name__ == '__main__':
    main()
