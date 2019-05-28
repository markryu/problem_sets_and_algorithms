


def main():
    aTup = ['a', 2, 'c']
    
    print (oddTuples(aTup))

def oddTuples(aTup):
    '''
    aTup: a tuple
    returns: tuple, every other element of aTup
    '''
    return aTup[::2]




if __name__ == '__main__':
    main()