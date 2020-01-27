n = 3
sum=0
final_list=[]
for i in range(3):
    for j in range(3):
        for k in range(3):
            inter_list = []
            sum = i+j+k
            if sum < n:
                inter_list.append(i)
                inter_list.append(j)
                inter_list.append(k)
                final_list.append(tuple(inter_list))
            else:
                next






print final_list
