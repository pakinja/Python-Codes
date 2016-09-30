def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    for i in range(1,a):
        if a < b:
            if b%a==0 and a%a==0:
                return a
            else:
                div = a-i
                if b % div == 0 and a % div == 0:
                    return div
        else:
            if a%b==0 and b%b==0:
                return b
            else:
                div = b-i
                if a%div == 0 and b%div == 0:
                    return div
