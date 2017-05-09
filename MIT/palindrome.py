# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 20:07:40 2016

@author: Francisco
"""

def isPalindrome(s):
    print(1)  
    def toChars(s):
        print(2)        
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        #print(ans)
        #print(type(ans))
        return ans
        
    def isPal(s):
        print(3)
        if len(s) <=1:
            return True
        else:
            print(s[1:-1])
            return s[0]==s[-1] and isPal(s[1:-1])
            
    return isPal(toChars(s))