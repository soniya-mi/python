#!/usr/bin/python

list1 = [1,2,3,4,5,6,7,8]
d=2

temp1=[]
temp2=[]

for i in range(0,len(list1)):
    if ( i < d ) :
        temp1.append(list1[i])
    else:
        temp2.append(list1[i])

temp2.extend(temp1)
print temp2

#input : 1 , 2 , 3 , 4 , 5
#output : 3 , 4 , 5 , 1 ,2
