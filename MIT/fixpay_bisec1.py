# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 11:48:09 2016

@author: Francisco
"""
#import numpy as np

balance = 320000
annualInterestRate = 0.2

i = 0

for p in ((balance//12.0),
    (balance*(1 + annualInterestRate//12)**12)/12,1):
    bal_1 = [balance]    
    print[p]
    for i in range(13):
        print(bal_1[i])
        bal_1.append((bal_1[i] - p) +
        (annualInterestRate/12)*(bal_1[i] - p))
    if bal_1[i] <= 0:
        #print(p, bal_1)
        print('Lowest Payment: ' + str(round(p,2)))
        break
        i += 1
    p += 0.01
