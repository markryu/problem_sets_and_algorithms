def main():
    """Given an array of integers, return indices of the two numbers such that they add up to a specific target.  
    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    example:  Given nums = [2, 7, 11, 15], target = 9,  Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].
    """

    print (bruteForce([3,2,4], 6))
    print (bruteForce([2, 7, 11, 15], 9))

    print (dictMethod([3,2,4], 6))
    print (dictMethod([2, 7, 11, 15], 9))

def bruteForce(given_list, target):
    """ran through leetcode, and obviously exceeded time limit as it's a brute force function
    """
    test_list = given_list
    for idx, each_number in enumerate(given_list):
        #print( idx, each_number)
        for idx_test, each_test in enumerate(test_list):
            #print ("test")
            #print ( idx_test, each_test)
            main_test = each_test + each_number
            if idx == idx_test:
                pass
            elif main_test == target:
                return [idx, idx_test]
            else:
                pass

def dictMethod(given_list, target):
    """ if target answer - givenlist at index i, then save it to dictionary,
    if not then return an answer"""
    dict = {}       
    listLen = len(given_list)
    for i in range(listLen):             
        if target - given_list[i] not in dict:                 
            dict[given_list[i]] = i             
        else:                 
            return [dict[target-given_list[i]],i]


if __name__ == '__main__':
    main()
