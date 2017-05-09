# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 19:34:54 2016

@author: Francisco
"""
def AnnumBal(balance, annualInterestRate, monthlyPaymentRate):
        
        balance = ((balance - balance*monthlyPaymentRate )+
            (annualInterestRate/12)*(balance - balance*monthlyPaymentRate))
        print(balance)
        return (round(balance, 2) and
            AnnumBal(balance, annualInterestRate, monthlyPaymentRate))