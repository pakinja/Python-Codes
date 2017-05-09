# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 23:24:23 2016

@author: Francisco
"""

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