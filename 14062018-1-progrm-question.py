def find_prefix(elem1 , elem2):
    prefix=""
    length=0
    if len(elem1) > len(elem2):
        length = len(elem2)
    else:
        length=len(elem1)
    for index in range(0,length):
        if elem1[index] == elem2[index]:
            prefix=prefix+elem1[index]
        else:
            continue
        
    return prefix
    
list = [ "ethans" , "ethan" , "ethansmumbai" , "ethansludhiana" , "ethanschandigarh" ]

longest_prefix = find_prefix(list[0] , list[1])
for index in range(2,len(list)):
    longest_prefix = find_prefix(longest_prefix,list[index])

print longest_prefix


