# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 11:48:09 2016

@author: Francisco
"""
#import numpy as np

balance = 999999
annualInterestRate = 0.18
#plist = range(10,(balance//10)+10,10)
#plist = np.arange((balance//12.0),
#    (balance*(1 + annualInterestRate/12)**12)/12.0,0.01)
#print(plist)

def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step
 

plist = list()

for i in frange((balance//12.0),
    (balance*(1 + annualInterestRate/12)**12)/12.0, 0.01):
    plist.append(round(i,2))
    #print(i)
#print(plist)


i = 0

for p in plist:
    bal_1 = [balance]    
    #print[p]
    for i in range(13):
        #print(bal_1[i])
        bal_1.append((bal_1[i] - p) +
        (annualInterestRate/12)*(bal_1[i] - p))
    if bal_1[i] <= 0:
        #print(p, bal_1)
        print('Lowest Payment: ' + str(round(p,2)))
        break
        i += 1
    p += 1
