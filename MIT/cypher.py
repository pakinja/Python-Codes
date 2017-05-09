# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 16:45:37 2016

@author: Francisco
"""

import string

def Coder(shift):
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    
    if 0 <= shift < 26:
        unshifted_letters = upper + lower
        shifted_letters = (upper[shift:] + upper[:shift] + lower[shift:]
                            + lower[:shift])
        #print(shifted_letters)
    return dict(zip(unshifted_letters, shifted_letters))