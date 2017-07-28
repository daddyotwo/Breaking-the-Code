# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
n = HAND_SIZE

SCRABBLE_LETTER_VALUES = {
    '*':0, 'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


WORDLIST_FILENAME = "words_ps3.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    comp_a = 0
    for char in word.lower():
        comp_a += SCRABBLE_LETTER_VALUES[char]
    comp_b = 7*len(word) - 3*(n - len(word))
    if comp_b <= 1: comp_b = 1
    score = comp_a*comp_b
    return score

def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    temp = []
    for letter in hand.keys():
        for j in range(hand[letter]):
            temp.append(letter)
    disp = " ".join(temp)
    return disp

def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = int(math.ceil((n) / 3))
    for i in range(num_vowels-1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    for i in range(num_vowels-1, n-1):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    hand['*'] = hand.get('*', 1)
    return hand

def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    temp_hand = []
    for key,val in hand.items():
        for i in range(val):
            temp_hand.append(key)
    temp_word = list(word)
    temp = temp_hand.copy()
    for ind,val in enumerate(temp_hand):
        if val in temp_word: temp[ind] = 0
        else:temp[ind] = val
    temp_cock ={}
    for ind,val in enumerate(temp):
        if val != 0 : temp_cock[val] = temp_cock.get(val,0) + 1
    return temp_cock

def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    temp_word_list = word_list.copy()
    dict_word = {}
    temp_hand = hand.copy()
    for char in word.lower():
        dict_word[char] = dict_word.get(char, 0) + 1
    length = 0
    for key, value in dict_word.items():
        if key in temp_hand.keys() and temp_hand[key] >= value: length += 1
    word_as_list = list(word.lower())
    ast = True
    if '*' in word_as_list:
        for char in VOWELS:
            tempword = word_as_list[:word_as_list.index('*')]+[char] + word_as_list[word_as_list.index('*')+1:]
            if ''.join(tempword) in  temp_word_list:
                ast = True
                in_list = True
                break
            else: 
                ast = False
                in_list = False
    else: 
        in_list = word.lower() in temp_word_list
    return in_list and length == len(dict_word) and ast

def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: int
    """
    return len(hand) 

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    handlen = calculate_handlen(hand)
    hand_score = 0
    while handlen > 0:
        word = input('Enter valid word or !! to indicate you are done: ')
        if word == '!!': break
        else:
            while is_valid_word(word, hand, word_list):
                print('\nThis word earned you',get_word_score(word, n),'points!')
                hand_score += get_word_score(word, n)
                print('\nTotal score is:', hand_score)
                break
            else:
                print('\nThis word is not valid!')
        hand = update_hand(hand, word)
        handlen = calculate_handlen(hand)
        if handlen > 0: 
            print('\nCurrent hand:', display_hand(hand))
        continue
    print('\nTotal score for this hand is:', hand_score)
    return hand_score

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    temp_hand = hand.copy()
    temp_letter = letter
    while letter.lower() in temp_hand.keys():
        if letter in VOWELS: letter = random.choice(VOWELS)
        else: letter = random.choice(CONSONANTS)
    temp_hand[letter] = temp_hand.pop(temp_letter)
    return temp_hand

def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    hand_num = int(input('''
                     
                     Welcom to Wordgame!
                     
                     How many hands you wish to play?
                     
                     '''))
    rep_count = 1
    total_score = 0
    hand_num_c = 1
    while hand_num > 0:
        hand = deal_hand(n)
        print('\nCurrent hand #',hand_num_c,':', display_hand(hand))
        hand_num_c += 1
        ask = input('Would you like to substitute a letter? yes/no ')
        if ask == 'yes': 
            sub_l = input('\nEnter letter: ')
            hand = substitute_hand(hand, sub_l)
            print('\nNew hand:', display_hand(hand))
        hand_score = play_hand(hand, word_list)
        if rep_count == 1: 
            rep = input('\nWould you like to replay this hand? yes/no ')
            if rep == 'yes': 
                hand_num_c -= 1
                print('\nReplaying hand')
                hand = deal_hand(n)
                hand_score = play_hand(hand, word_list)
                rep_count -= 1
        total_score += hand_score
        print('\nYour score for this hand is:', hand_score)
        print('\nYour total score is:', total_score)
        hand_num -= 1
    
    return print('\nYou finished the game! Total score over all hands:', total_score )

if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
