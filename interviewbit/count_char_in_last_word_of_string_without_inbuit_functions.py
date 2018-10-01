string = "HEllo World soniya   "
length=0
p=0
for char in string:
    if char != " " :
        length = length+1
    elif length > 0:
        p = length
        length=0

if length == 0:
    print p 
else:
    print length
