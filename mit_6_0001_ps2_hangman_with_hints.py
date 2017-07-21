# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 10:58:27 2017

@author: Пользователь
"""

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
#    """
#    Returns a list of valid words. Words are strings of lowercase letters.
#    
#    Depending on the size of the word list, this function may
#    take a while to finish.
#    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    return wordlist

def load_words_a():
#    """
#    Returns a list of valid words. Words are strings of lowercase letters.
#    
#    Depending on the size of the word list, this function may
#    take a while to finish.
#    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist_a = line.split()
    return wordlist_a

def choose_word(wordlist):
#    """
#    wordlist (list): list of words (strings)
#    
#    Returns a word from wordlist at random
#    """
    return random.choice(wordlist)


def hangman_with_hints(secret_word):
    
    def match_with_gaps(my_word, other_word):
        '''
        my_word: string with _ characters, current guess of secret word
        other_word: string, regular English word
        returns: boolean, True if all the actual letters of my_word match the 
            corresponding letters of other_word, or the letter is the special symbol
            _ , and my_word and other_word are of the same length;
            False otherwise: 
        '''
        temp_word = ''
        c = -1
        if len(my_word) == len(other_word):
            for char in other_word:
                c += 1
                if char == my_word[c]: temp_word += char
                else: temp_word += '_'
        return temp_word == my_word
    
    def show_possible_matches(my_word):
        '''
        my_word: string with _ characters, current guess of secret word
        returns: nothing, but should print out every word in wordlist that matches my_word
                 Keep in mind that in hangman when a letter is guessed, all the positions
                 at which that letter occurs in the secret word are revealed.
                 Therefore, the hidden letter(_ ) cannot be one of the letters in the word
                 that has already been revealed.
    
        '''
        temp_l = ''
        wl = load_words_a()
        for other_word in wl:
            if match_with_gaps(my_word, other_word): temp_l = temp_l + other_word +' '
        print('Possible words are:')
        return temp_l


    def hangman(secret_word):
    #    '''
    #    secret_word: string, the secret word to guess.
    #    
    #    Starts up an interactive game of Hangman.
    #    
    #    * At the start of the game, let the user know how many 
    #      letters the secret_word contains and how many guesses s/he starts with.
    #      
    #    * The user should start with 6 guesses
    #
    #    * Before each round, you should display to the user how many guesses
    #      s/he has left and the letters that the user has not yet guessed.
    #    
    #    * Ask the user to supply one guess per round. Remember to make
    #      sure that the user puts in a letter!
    #    
    #    * The user should receive feedback immediately after each guess 
    #      about whether their guess appears in the computer's word.
    #
    #    * After each guess, you should display to the user the 
    #      partially guessed word so far.
    #    
    #    Follows the other limitations detailed in the problem write-up.
    #    '''
    ##########################################################################
        letters_guessed = []
        guess_count = 6
        warn_count = 3
        available_letters = None
    ##########################################################################
    
        def get_available_letters(letters_guessed):
        
        #letters_guessed: list (of letters), which letters have been guessed so far
        #returns: string (of letters), comprised of letters that represents which letters have not
        #yet been guessed.
        
            temp_available_letters = list(string.ascii_lowercase)
            for let in letters_guessed:
                if let in temp_available_letters:
                    temp_available_letters.remove(let)
            return temp_available_letters
    
    ###########################################################################
        
        def info_screen():
            print('\nAvailable letters:',' '.join(get_available_letters(letters_guessed)))
            print('\nGuesses:', guess_count)
            print('\n',get_guessed_word(secret_word, letters_guessed),'\n')
            
    ##############################################################################
            
            
        def is_word_guessed(secret_word, letters_guessed): #READY
    #    '''
    #    secret_word: string, the word the user is guessing; assumes all letters are
    #      lowercase
    #    letters_guessed: list (of letters), which letters have been guessed so far;
    #      assumes that all letters are lowercase
    #    returns: boolean, True if all the letters of secret_word are in letters_guessed;
    #      False otherwise
    #    '''
            templist_a = []
            templist_b = list(secret_word)
            
            for char in secret_word:
                if char in letters_guessed:
                    templist_a += char
            return templist_a == templist_b
    
    
    ###############################################################################
    
        def get_guessed_word(secret_word, letters_guessed): #READY
    #    '''
    #    secret_word: string, the word the user is guessing
    #    letters_guessed: list (of letters), which letters have been guessed so far
    #    returns: string, comprised of letters, underscores (_), and spaces that represents
    #      which letters in secret_word have been guessed so far.
    #    '''   
            temp_guessed_word = []
            for char in secret_word:
                temp_guessed_word.append(' _ ')
            sw_to_list = list(secret_word)
            sw_a_to_list = list(secret_word)
            for let in letters_guessed:
                if let in secret_word and sw_to_list.count(let)>1: 
                    for char in secret_word:
                        if char == let:
                            ind = sw_a_to_list.index(let)
                            sw_a_to_list[ind] = ''
                            temp_guessed_word[ind] = let
                elif let in secret_word : 
                    ind = sw_to_list.index(let)
                    temp_guessed_word[ind] = let
            temp_guessed_word = ''.join(temp_guessed_word)
            return temp_guessed_word
    
    #####################################################################################
    
        print('\n***Welcome to Hangman!***\n\nI am thinking of a word that is',len(secret_word),'letters long.')
        print(get_guessed_word(secret_word, letters_guessed))
        print('\nFor hint press *')
        print('--------------------------------------')
        print('Available letters:',string.ascii_lowercase)

    
        while not is_word_guessed(secret_word,letters_guessed) and guess_count > 0:
    
            available_letters = ' '.join(get_available_letters(letters_guessed))
            
            print('--------------------------------------')
            
            user_letter = input('Enter one lowercase letter: ')
            user_letter = user_letter.lower()
            print(get_guessed_word(secret_word, letters_guessed))
            
            if user_letter == '*':
                my_word = get_guessed_word(secret_word, letters_guessed).replace(' ','')
                print(show_possible_matches(my_word))
                continue
            
            if user_letter.isalpha() and user_letter not in letters_guessed:
                if user_letter in secret_word and user_letter in available_letters:
                    letters_guessed += user_letter
                    print('\nEst takaya bukva!')
                    info_screen()
                    if is_word_guessed(secret_word,letters_guessed): break
                    continue
                elif user_letter in 'aeiouy' and user_letter in available_letters :
                    letters_guessed += user_letter
                    guess_count -= 2
                    if guess_count <= 0: break
                    print('\nWrong letter! Try again!')
                    info_screen()
                    continue
                elif user_letter in available_letters:
                    letters_guessed += user_letter
                    guess_count -= 1
                    if guess_count <= 0: break
                    print('\nWrong letter! Try again!')
                    info_screen()
                    continue
            else:
                if warn_count != 0:
                    if user_letter in letters_guessed:
                        warn_count -= 1
                        print('\nYou entered this letter before!\n\nYou lost a warning. Warnings left:', warn_count)
                        info_screen()
                        continue
                    warn_count -= 1
                    print('\nOnly letters allowed!\n\nYou lost a warning. Warnings left:', warn_count)
                    info_screen()
                    continue
                else:
                    if user_letter in letters_guessed:
                        guess_count -= 1
                        if guess_count <= 0: break
                        warn_count = 3
                        print('\nYou entered this letter before!\nYou lost a guess! Warnings left:', warn_count)
                        info_screen()
                        continue
                    guess_count -= 1
                    if guess_count <= 0: break
                    warn_count = 3
                    print('\nYou lost a guess! Warnings left:', warn_count)
                    info_screen()
                    continue
    
    
        if is_word_guessed(secret_word,letters_guessed): 
            print('\nYou win!') 
            score = guess_count * len(secret_word)
            print('\nYour Score is:', score )
        else: print('\nYou lose!\nSecret word was', secret_word)
    
    hangman(secret_word)
    ########################################################################################

if __name__ == "__main__":
    wordlist = load_words()
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)