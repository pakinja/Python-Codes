# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 15:39:20 2016

@author: Francisco
"""

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
    
    
    us_num_int = int(us_num)
    us_num_l = list(us_num)
    
    if us_num_int in range(0, 11):
        return trans[us_num]
        
    elif 10 < us_num_int < 20:
        return str(trans['10']) + ' ' + str(trans[us_num_l[-1]])
        
    else:
        if us_num_l[-1] == '0':
            return str(trans[us_num_l[0]]) + ' ' + str(trans['10'])
        else:
            return (str(trans[us_num_l[0]]) + ' ' + str(trans['10']) +
                ' ' + str(trans[us_num_l[-1]]))