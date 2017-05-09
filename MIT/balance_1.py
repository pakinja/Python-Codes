# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 00:04:00 2016

@author: Francisco
"""
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
i = 0
for i in range(12):
    balance = ((balance - balance*monthlyPaymentRate )+
        (annualInterestRate/12)*(balance - balance*monthlyPaymentRate))
    i += 1
print(round(balance,2))