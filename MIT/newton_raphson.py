# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 15:27:19 2016

@author: Francisco
"""

epsilon = 0.01
y = 54.0
guess = y/2.0
numGuesses = 0

while abs(guess*guess - y) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess**2) - y )/(2*guess))
    
print('numGuesses = ' + str(numGuesses))
print('Square root of ' + str(y) + ' is about ' + str(guess))