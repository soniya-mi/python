list = [1,2,3,7,5]

TotalSum=12
flag=0
new_list=[]

for index in range(0,len(list)):
    sum =0
    for ind in range(index,len(list)):
        sum = sum +list[ind]
        if TotalSum == sum:
            flag=1
            new_list.append(index)
            new_list.append(ind)
            break
        elif TotalSum < sum:
            flag = 0
            break

    if flag == 1:
        print new_list
        break

if flag != 1:
    print "-1"


