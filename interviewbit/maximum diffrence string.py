string="12349232"
diff =0
max=0
for index in range(0,len(string)-1):
    diff=int(string[index+1]) - int(string[index])
    if diff > max:
        list=[]
        max=diff
        list.append(string[index])
        list.append(string[index+1])
        #print max

print list
print max
