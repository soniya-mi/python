list = [4,3,2,1]
max = 0 
sec_max = 0
for item in list : 
    if item > max:
        sec_max = max
        max = item
    elif item > sec_max : 
        sec_max = item
        

print sec_max