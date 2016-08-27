name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fhand = open(name)

counts = dict()
wdname = list()

for line in fhand:
    if not line.startswith('From '): continue
    words = line.split()
    wdname.append(words[1])
    
#print wdname
#print len(wdname)
    
for word in wdname:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1
                   
print counts
