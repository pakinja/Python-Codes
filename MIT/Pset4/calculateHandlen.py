# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 16:47:21 2016

@author: Francisco
"""

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    val = hand.values()
    suma = 0    
    
    for i in val:
        if i > 0:
            suma += i
        
    return suma