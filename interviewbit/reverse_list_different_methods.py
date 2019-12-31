list = [1,2,3,4,5]


#Method 1
reverse_list = list[::-1]
print reverse_list

#Method2
list = [1,2,3,4,5]
new_list=[]
for item in range(len(list),0,-1):
    new_list.append(item)

print new_list

