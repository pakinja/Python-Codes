def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    
    elif exp == 1:
        return base
    
    else:
        prod = 1
        for i in range(1,exp+1):
            prod *= base
            i += 1
    return prod
