#!/usr/bin/env python

a=[1,2,3]
print("a: ", a)
b=a
print("b=a: ", b)
#the assignment b=a creates a reference to a
b[0]=0
#changing b also changes a
print("b has changed: ", b)
print("What about a? ",a)
c=list(a)
print("c=list(a): ",c)
#list(a) creates a 'shallow' copy of a
c[0]=4
#changing c seems not to affect a
print("c has changed: " ,c)
print("What about a? " , a)
print("-"*25)

print("What about a list that contains a list?")
a=[[0,1],2,3]
print("a: ", a)
c=list(a)
print("c=list(a): ",c)
#list(a) creates a 'shallow' copy of a
c[0][0]=4
#list(a) only copies a reference to each entries of a
print("c has changed: " ,c)
print("What about a? " , a)

import copy
d=copy.deepcopy(a)
#copy.deepcopy recursively copies everything
print("d=copy.deepcopy(a): ", d)
d[0][1]=5
print("d has changed: ", d)
print("What about a?", a)
print("-"*25)
