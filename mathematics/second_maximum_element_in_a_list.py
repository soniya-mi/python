list = [4,3,2,1]
max = 0
s_max = 0
for item in list:
    
    if item > max:
        s_max=max
        max = item
    elif item > s_max:
        s_max = item
print  s_max