import re

fname = raw_input("Enter file name: ")
fh = open(fname)

nums = list()

for line in fh:
    line = line.rstrip()
    enums = re.findall('[0-9]+', line)
    if len(enums) == 0 : continue
    for n in range(len(enums)):
        num = int(enums[n])
        nums.append(num)
    #print(num)
    #print(enums)

#print (len(nums))
#print(nums)
print(sum(nums))
