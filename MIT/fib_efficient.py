# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 17:25:25 2016

@author: Francisco
"""

def fib_efficient(n,d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans
        
d = {1:1, 2:2}
print(fib_efficient(6, d))