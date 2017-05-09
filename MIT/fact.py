# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 12:04:56 2016

@author: Francisco
"""

def fact_iter(n):
    """assumes n an int >=0 """
    answer = 1
    while n > 1:
        answer *= n
        n -= 1
    return answer