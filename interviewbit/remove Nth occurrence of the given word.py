list = ["geeks" , "for" , "geeks" ]
n = 2

new_list=[]
for i in range(0,len(list)):
    if i != n:

        new_list.append(list[i])

print new_list
