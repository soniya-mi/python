list = [12, 35, 9, 56, 24]

length=len(list)
temp=list[0]
list[0]=list[-1]
list[-1]=temp

print list
