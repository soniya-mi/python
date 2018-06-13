#!/usr/bin/python

list = [1, 2, 3, 4, 5, 6]
 
for index in range(len(list)):
    if index % 2 == 0:
        tmp = list[index]
        list[index] = list[index+1]
        list[index+1]=tmp
    else:
        continue
    
print list

        
    