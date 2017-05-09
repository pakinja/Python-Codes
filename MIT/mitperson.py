# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 11:58:17 2016

@author: Francisco
"""

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
        
    def get_age(self):
        return self.age
        
    def get_name(self):
        return self.name
        
    def set_age(self, newage):
        self.age = newage
    
    def set_name(self, newname = ""):
        self.name = newname
        
    def __str__(self):
        return "animal: " + str(self.name) + ":" + str(self.age)
        
class Cat(Animal):
    
    def speak(self):
        print("meow")
    
    def __str__(self):
        return "cat:" + str(self.name) + ":" + str(self.age)
        
        
class Rabbit(Animal):
        
    tag = 1
    
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.patent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1
        
    def get_rid(self):
        return str(self.rid).zfill(3)
        
    def get_parent1(self):
        return self.parent1
        
    def get_parent2(self):
        return self.parent2
        
    def __add__(self, other):
        
        #returning object of same type as this class
        
        return Rabbit(0, self, other)
        
    def __eq__(self, other):
        parents_same = self.parent1.rid == other.parent1.rid \
                        and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent1.rid == other.parent2.rid
        
        return parents_same or parents_opposite

class Person(Animal):
    
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self,name)
        self.friends = []
        
    def get_friends(self):
        return self.friends
        
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
            
    def speak(self):
        print("hello")
            
    def age_diff(self, other):
        # alternative way: diff = self.age - other.age
        diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print(self.name, "is", diff, "years older than", other.name)
        else:
            print(self.name, "is", -diff, "years younger than", other.name)
            
    def __str__(self):
        return "person:" + str(self.name) + ":" + str(self.age)
        
import random
        
class Student(Person):
    
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
    
    def change_major(self, major):
        self = major

    def speak(self):
        r = random.random()
        if r < 0.25:
            print("i have homework")
        elif 0.25 <= r < 0.5:
            print("i need sleep")
        else:
            print("i am watching tv")
            
    def __str__(self):
        return "student:" + str(self.name) + ":" + str(self.age) + ":"+ str(self.major)


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
p4 = Person('John')