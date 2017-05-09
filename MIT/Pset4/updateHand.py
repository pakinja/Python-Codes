# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 10:37:33 2016

@author: Francisco
"""

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
 
    #wd = getFrequencyDict(word)
    #print(wd)
    hand_1 = hand.copy()
    for x in word:
        hand_1[x] = hand_1.get(x,0) - 1
    #print(fq)
    return hand_1
    
        