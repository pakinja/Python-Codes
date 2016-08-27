def computepay(hours,rate):
    hours = float(hours)
    rate = float(rate)
    
    if hours <= 40 :
       pay = rate*hours
    else :
       pay = rate *40+(rate*1.5*(hours - 40))
    return pay
h = raw_input("Enter Hours: ")
h = float(h)
r = raw_input("Enter Rate: ")
r= float(r)
p = computepay(h,r)
print p
