#!/usr/bin/python

def add(list):
    sum = 0 
    for item in list:
        sum = sum + item
    return sum
list = [1,2,3,4,5]
total = add(list)
print "infunction"
print total