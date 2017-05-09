# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 11:48:09 2016

@author: Francisco
"""
balance = 320000
annualInterestRate = 0.2

lower = balance / 12.0
upper = balance*((1 + (annualInterestRate)/12)**12)/12.0
p = (lower + upper)/2
epsilon = 0.01

#print(lower, upper)    
j=0
for j in range(30):
    bal_1 = [balance]               
    for i in range(12):
        bal_1.append((bal_1[i] - p) +
        (annualInterestRate/12)*(bal_1[i] - p))
        #print(bal_1[i], p)
        #print[bal_1[-1]]
                                  
    if bal_1[-1] < 0:
        upper = p
        #print(upper)
    elif bal_1[-1] > 0:
        lower = p
    p = (lower + upper)/2
    j += 1
print(round(p,2))
        
        
        
                                                                                             