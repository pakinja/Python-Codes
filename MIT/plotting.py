# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 12:01:15 2016

@author: Francisco
"""

import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)
    
plt.plot(mySamples, myLinear)
plt.plot(mySamples, myQuadratic)
plt.plot(mySamples, myCubic)
plt.plot(mySamples, myExponential)

plt.figure('lin')
plt.clf()
plt.subplot(211)
plt.title('Linear')
plt.ylim(0,29)
plt.xlabel('Sample Points')
plt.ylabel('Linear Function')
plt.plot(mySamples, myLinear, 'b^', label = 'Linear')
plt.legend(loc = 'upper left')
plt.figure('quad')
plt.plot(mySamples, myQuadratic)
plt.figure('cube')
plt.plot(mySamples, myCubic)
plt.figure('expo')
plt.plot(mySamples, myExponential)
###

plt.figure('lin quad')
plt.clf()
plt.plot(mySamples, myLinear)
plt.plot(mySamples, myQuadratic)