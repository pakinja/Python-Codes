#Read a string, detect and count a pattern

s = 'azcbobobegghaklbob'
ls = len(s)
dect_str = "bob"
lds = len(dect_str)

#print(ls)
count = 0
for i in range(0,ls-(lds-1)):
    if s[i:i+lds] == dect_str:   
        count +=1
print("Number of times bob occurs is: " + str(count))
