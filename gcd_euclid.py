def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a == 0:
       return b
    elif b == 0:
       return a
    elif a >= b:
        if a%b==0:
            return b
        else: 
            return gcdRecur(b,a%b)
    elif b >= a:
        if b%a==0:
            return a
        else:
            return gcdRecur(a,b%a)
