list = [-2,1,-3,4,-1,0,2,1,-5,4]

max=0
sum=0
expect_list=[]
current_rem=[]

for index in range(0,len(list)):
    sum = sum + list[index]
    if sum > max:
        expect_list.extend(current_rem)
        expect_list.append(list[index])
        current_rem =[]
        max = sum
    elif sum < 0:
        sum =0
        expect_list=[]
        current_rem=[]
    else:
        current_rem.append(list[index])

print max , expect_list




