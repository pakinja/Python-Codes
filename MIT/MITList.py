# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 14:37:57 2016

@author: Francisco
"""
class MITPerson(Person):
    
    nextIdNum = 0 # next ID number to assign
    
    def __init__(self, name):
        Person.__init__(self, name) # initialize Person attributes
        self.idNum = MITPerson.nextIdNum # MITPerson attribute: unique ID
        MITPerson.nextIdNum += 1
        
    def getIdNum(self):
        return self.idNum
        
    # sorting MIT people uses their ID number, not name!
    def __lt__(self, other):
        return self.idNum < other.idNum
        
    def speak(self, utterance):
        return (self.getLastName() + "says:" + utterance)


m3 = MITPerson('Mark Zuckerberg')
Person.setBirthay(m3,5,14,84)
m2 = MITPerson('Drew Houston')
Person.setBirthay(m2,3,4,83)
m1 = MITPerson('Bill Gates')
Person.setBirthay(m1, 10, 28, 55)

MITPersonList = [m1, m2, m3]

#
#for e in MITPersonList:
#   print(e)

#MITPersonList.sort()
#print()

#for e in MITPersonList:
#print(e)

p1 = MITPerson('Eric')
p2 = MITPerson('John')
p3 = MITPerson('John')
p4 = MITPerson('John')