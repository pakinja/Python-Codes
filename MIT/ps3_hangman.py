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
    bol = list()
    pos = list()
    for i in range(len(secretWord)):
        for j in range(len(lettersGuessed)):
            bol_True = secretWord[i]==lettersGuessed[j]
            if bol_True == True:
                bol.append(secretWord[i]==lettersGuessed[j])
                pos.append(i)
                break
    if len(bol) >= len(secretWord):
        return True, bol
    else:
        return False, bol


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    #bol = list()
    pos = list()
    dicc = dict()
    
    if len(lettersGuessed)== 0:
        for k in range(len(secretWord)):  
            dicc[k] = ' _ '
    else:
            
        for i in range(len(secretWord)):
            for j in range(len(lettersGuessed)):
                
                bol_True = secretWord[i]==lettersGuessed[j]
                if bol_True == True:
                    dicc[i] = secretWord[i]
                    pos.append(i)
                    break
                elif bol_True == False:
                    dicc[i] = ' _ '
    val_string = ''.join(dicc.values())
    return val_string



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    voc = list(map(chr, range(97, 123)))
    diff = list(set(voc) - set(lettersGuessed))
    diff_1 = sorted(diff)
    return ''.join(diff_1)
    

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
    lsw = len(secretWord)
    lettersGuessed = list()
    #mistakeMade = list()
    print('Welcome to the game Hangman!')    
    print('I am thinking of a word that is ' + str(lsw) + ' letters long')
    print('-----------')
    i = 8    
    while i > 0:
        print('You have ' + str(i) + ' guesses left' )
        print('Available letters: ' + 
                str(getAvailableLetters(lettersGuessed)))
        guess = input('Please guess a letter: ')
        guessInLowerCase = guess.lower()
        
        
        if guessInLowerCase not in getAvailableLetters(lettersGuessed):
            print("Oops! You've already guessed that letter: " +
            str(getGuessedWord(secretWord, lettersGuessed)))
            
        

        elif (guessInLowerCase not in secretWord)== True:
            lettersGuessed.append(guessInLowerCase)            
            i -= 1
            print('Oops! That letter is not in my word: ' +
            str(getGuessedWord(secretWord, lettersGuessed)))
            if i==0:
                print('Sorry, you ran out of guesses. The word was '+
                str(secretWord) + '.')

        
        elif (guessInLowerCase in secretWord) == True:
            lettersGuessed.append(guessInLowerCase)            
            print('Good guess: ' + 
            str(getGuessedWord(secretWord, lettersGuessed)))
            
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('Congratulations, you won!')
            break
    
    




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
