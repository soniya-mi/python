list = [5, -1, -1, 1, 2, 3]
m =7
output = []
for i in range(0,len(list)):
   # print list[i] , (list[i-1+1])+1
    moderation=((list[i-1])+1)%m
    output.append(moderation)
    #print moderation


print output
