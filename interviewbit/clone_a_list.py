list = [1,2,3,4]
copy_list=[]

for index in range(0,len(list)):
    copy_list.append(list[index])

print copy_list


#method2 using extend 

list = [1,2,3,4]
copy_list=[]
copy_list.extend(list)

print copy_list
