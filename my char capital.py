string="my name is minal"
list = string.split()
expected_str=""

for itm in range(len(list),0,-1):
    expected_str = expected_str +  " " + list[itm-1] 
    
print expected_str