#!/usr/bin/python

list = [ 1, "a" , 2 , "b"]
new_list=[]
for item in range(len(list),0,-1):
    new_list.append(list[item-1])
        
print new_list