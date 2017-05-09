# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 11:57:05 2016

@author: Francisco
"""

def genPrimes():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            print(p)
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last