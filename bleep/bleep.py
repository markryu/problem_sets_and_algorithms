import sys

def main():

    if len(sys.argv) != 2:
        sys.exit("Usage: python bleep.py dictionary")

    s = str(input('What message would you like to censor?\n'))
    s_set = set(s.split())

    with open(sys.argv[1], 'r') as banned_words:
        banned_set = set()
        banned = (banned_words.read().split())
        {banned_set.add(each) for each in banned}
        caught = s_set & banned_set
        print (banned_set)
        for each_word in caught:
            s = (s.replace(each_word, '*' * len(each_word)))
        print (s)



if __name__ == "__main__":
    main()
