# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 17:26:02 2016

@author: Francisco
"""

import math

s = 'drhfgarixplwxzcarrz'

voc = list(map(chr, range(97, 123)))
#print(voc)
pos = range(0,26)
voc_dict = {}
for i in range(len(voc)):
    voc_dict[voc[i]] = pos[i]

string = list(enumerate(s))
str_s = dict(string)
seq = list()
for j in range(len(s)):
    seq.append(voc_dict.get(s[j]))
    #print "Value : %s" %  voc_dict.get(s[j])

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)
nlist = nCr(len(s)-1,2)

lists = []
for p in range(len(seq)):
    lists.append([])

################################################
#print(seq)
l = 0
k = 0

while l <= len(seq)-1:
   if k == len(seq)-1:
       break
   while k < len(seq)-1:
        if seq[k] <= seq[k+1]:
            #print(seq[k],seq[k+1])
            lists[l].append(seq[k])
            lists[l].append(seq[k+1])
            if k == len(seq)-4:
                lists[l].append(seq[k+1])
            #print(lists[l])            
            #print 'no. lista',',', l
                       
            k += 1
            #print 'k', '=', k
            
                
        else:
            
            l += 1
            seq.remove(seq[k])
            
            #print(seq)
            #print 'k', '=', k           
            #print 'no. lista',',', l
            #print 'not ' , seq[k] , seq[k+1]
            break
####################################################
#print (lists)
l_string = list()
pos_max = list()

for r in range(len(lists)):
    imp = range(1,len(lists[r])-1,2)
    if len(lists[r]) > 3:
        lists[r] = [i for j, i in enumerate(lists[r]) if j not in imp]

#print(lists)

for t in range(len(lists)):
    pos_max.append(len(lists[t]))
#print('posmax',pos_max)
g_max = max(pos_max)
#print('gmax', g_max)

max_p = [i for i,x in enumerate(pos_max) if x == g_max]
#print 'pos', max_p

max_max = lists[max_p[0]]
#print 'maxmax', max_max
for p in max_max:
    l_string.append(voc[p])
#print(l_string)

#lon = len(l_string)
#print(lon)
#imp = range(1,lon-1,2)
#print(imp)

#for w in imp:
#    del l_string[w]
    
#l_string = [i for j, i in enumerate(l_string) if j not in imp]

#print len(s) , len(max_p)

if len(s) == len(max_p):
    l_string = s[0]
    print "Longest substring in alphabetical order is:", l_string
else:
    l_string = "".join(str(e) for e in l_string)
    print "Longest substring in alphabetical order is:", l_string

