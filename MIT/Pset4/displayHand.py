# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 16:40:15 2016

@author: Francisco
"""

def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,     # print all on the same line
    #print                             # print an empty line