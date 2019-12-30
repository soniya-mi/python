list = [100, 10, 5, 25, 35, 14]
n=11

mult=1
for i in range(0,len(list)):
    mult=mult*list[i]

output = mult % n
print output


'''Input : arr[] = {100, 10, 5, 25, 35, 14}, 
            n = 11
Output : 9
100 x 10 x 5 x 25 x 35 x 14 = 61250000 % 11 = 9'''
