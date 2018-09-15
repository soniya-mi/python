list = [4,3,2,1]
max = list[0]
s_max = list[1]
for item in list:
    
    if item < max:
        s_max=max
        max = item
    elif item < s_max:
        s_max = item
print  s_max