# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secret_dict = {'keys': str()}
    count = 0
    for c in secretWord:
        if c not in secret_dict['keys']:
            secret_dict['keys'] += c
    for each_letter in lettersGuessed:
        if each_letter in secret_dict['keys']:
            count += 1
    return True if count == len(secret_dict['keys']) else False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    indice_tbr = list()
    for idx, each_letter in enumerate(lettersGuessed):
        if each_letter in secretWord:
            indice_tbr.append(each_letter)
    for c in secretWord:
        if c not in indice_tbr:
            secretWord = secretWord.replace(c, '_')
    return secretWord


# print (getGuessedWord('secret', [ 'c', 'r', 't']))


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    from string import ascii_lowercase as lowercase
    for e in lettersGuessed:
        if e in lowercase:
            lowercase = lowercase.replace(e, '')
    return lowercase


# print (getAvailableLetters(['a', 'z']))

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...

    import sys
    print ("Welcome to the game, Hangman!")
    print (f"I am thinking of a word that is {len(secretWord)} letters long.")
    print ('-----')
    max_guesses = 9
    lettersGuessed = list()
    flag = isWordGuessed(secretWord, lettersGuessed)
    while not flag:
        print (f"You have {max_guesses} left.")
        print(f"Available letters: {getAvailableLetters(lettersGuessed)}")
        remaining = getAvailableLetters(lettersGuessed)
        newGuess = str()
        input_flags = bool()
        while input_flags != True:
            newGuess = input("Enter a new guess: ")
            if newGuess.isalpha() != True:
                print("Only use alphabet letters")
            elif len(newGuess) != 1:
                print ("Only use 1 character")
            else:
                newGuess = newGuess.lower()
                input_flags = True
        lettersGuessed.append(newGuess)
        guessed = getGuessedWord(secretWord, lettersGuessed)
        if newGuess in secretWord:
            if newGuess in remaining:
                print (f"Good guess: {guessed}")
                max_guesses -= 1
            else:
                print (f"Oops, You've already guessed that letter: {guessed}")
        else:
            max_guesses -= 1
            print (f"Oops, that letter is not in my word: {guessed}")

        print ("---------\n")
        if max_guesses == 0:
            print (f"\nThe secretWord is {secretWord}")
            try_again = input(
                "You have lost, try again? (press y/n and enter): ")
            flag = True
            if try_again == 'y':
                secretWord = chooseWord(wordlist).lower()
                hangman(secretWord)

            else:
                sys.exit("Goodbye :(")
    print ("Congratulations! you won!")


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
