# Paste your code into this box
plist = range(10,(balance//10)+10,10)

#print(plist)

i = 0

for p in plist:
    bal_1 = [balance]    
    #print[p]
    for i in range(13):
        #print(bal_1[i])
        bal_1.append((bal_1[i] - p) +
        (annualInterestRate/12)*(bal_1[i] - p))
    if bal_1[i] <= 0:
        print('Lowest Payment: ' + str(p))
        break
        i += 1
    p += 1
