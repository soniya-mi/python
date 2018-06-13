mylist = [2,2,2,3,3,3,1,1]
myset = set(mylist)
sum = 0
sum_of_list = 0 

k = 3
for item in myset:
    sum = sum + item
    
mult = sum * k
for item in mylist:
    sum_of_list = sum_of_list + item
    
number_missing = mult - sum_of_list
print number_missing