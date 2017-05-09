# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 14:20:33 2016

@author: Francisco
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    for k in aDict.keys():   # The order of the k's is not defined
        lens = len(aDict[k]))

    ks = list(aDict.keys())
    return(ks)