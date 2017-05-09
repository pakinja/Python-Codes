# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 16:34:26 2016

@author: Francisco
"""

def polysum(n,s):
    import math #import math module
        
    pi = math.pi # pi constant
    factor = 0.25 #formula factor
    area = (factor)*(n*s**2)/math.tan(pi/n) # formula for area
    
    per = (n*s)*(n*s) #perimeter squared
    
    return round(area + per, 4) # return result rounded up to 4 places