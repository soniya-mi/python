list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

occur ={}
new_list=[]
for item in list:
    count = 1
    if item in occur.keys():
        count=occur[item]
        occur[item]=count +1
    else:
        occur[item] = count

for key in occur.keys():
    if occur[key] > 1:
        new_list.append(key)

print new_list

