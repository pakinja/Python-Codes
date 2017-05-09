# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 11:37:01 2016

@author: Francisco
"""

import time

def c_to_f(c):
    return c*9.0/5 + 32
    
t0 = time.clock()
c_to_f(100000)
t1 = time.clock() - t0
print("t=", t1, ":", t1, "s,")