# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 17:01:55 2016

@author: Francisco
"""
def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """
    # save the current longest length for increasing run
    length_inc = []
    # save the current longest length for decreasing run
    length_dec = []
    # set the initial length to 1
    length_inc.append(1)
    length_dec.append(1)
    # save the result
    result_sum = 0
    # save the longest length
    longest_length = 0

    for i in range(1, len(L)):
        # assume the current longest length to 1
        length_inc.append(1)
        length_dec.append(1)
        # for increasing
        if L[i] >= L[i - 1]:
            length_inc[i] = length_inc[i - 1] + 1
            if length_inc[i] > longest_length:
                # update result
                longest_length = length_inc[i]
                result_sum = sum(L[i - longest_length + 1: i + 1])
        # for decreasing
        if L[i] <= L[i - 1]:
            length_dec[i] = length_dec[i - 1] + 1
            if length_dec[i] > longest_length:
                # update result
                longest_length = length_dec[i]
                result_sum = sum(L[i - longest_length + 1: i + 1])
    return result_sum