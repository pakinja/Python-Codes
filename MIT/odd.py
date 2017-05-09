# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 19:04:08 2016

@author: Francisco
"""
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    i = 0
    j = 0
    
    if b==0:
        return a
    elif a==0:
        return b
    elif a < b:
        if b%a==0:
            return a
        else:
            while True:
                i += 1
                if (b%(a-i))== 0 and (a%(a-i))== 0:
                    return a - i
            
            
    elif b < a:
        if a%b==0:
            return b
        else:
            while True:
                j += 1
                if (a%(b-j))== 0 and (b%(b-j))== 0:
                    return b - j   