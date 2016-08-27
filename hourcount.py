name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fhand = open(name)

counts = dict()
wdname = list()
hour = list()

for line in fhand:
    if not line.startswith('From '): continue
    words = line.split()
    wdname.append(words[5])

    #print wdname

for word in range(len(wdname)):
    hrs = wdname[word][0] + wdname[word][1]
    hour.append(hrs)
    
for word in hour:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1

        
klst = counts.keys()
klst.sort()
for key in klst:
    print key, counts[key]
        
        
#for key in sorted(counts.iterkeys()):                 
#    print key, counts[key]
                   
                   
#print counts
