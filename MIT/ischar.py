# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 19:54:47 2016

@author: Francisco
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:
        return False
    if len(aStr) == 1:
        return char[0] == aStr[0]

        
    elif char[0] == aStr[len(aStr)//2]:
        return True
        
    elif char[0] < aStr[len(aStr)//2]:
        if char[0] == aStr[(len(aStr)//2)]:
            return True
        
        else:
            return isIn(char, aStr[:(len(aStr)//2)])
        
    elif char[0] > aStr[len(aStr)//2]:
        
        if char[0] == aStr[(len(aStr)//2)]:
            return True
        
        else:
            #print(aStr[(len(aStr)/2)+2:])
            return isIn(char, aStr[(len(aStr)//2):])
    else:
        return False
    
    #return middle(aStr)
    
    
    
    