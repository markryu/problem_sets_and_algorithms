
def main():
    '''gets the sum of all muultiples of 3 or 5 below 1000'''
    sum_of_multiples = list()
    for each_number in range(1000):
        if each_number % 3 == 0 or each_number % 5 == 0:
            sum_of_multiples.append(each_number)
    print (sum(sum_of_multiples))
    return sum(sum_of_multiples) 

if __name__ =='__main__':
    main()
