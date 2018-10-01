number = [9,9,9]

carry_fwd =1

result = []
for index in range(len(number)-1,-1,-1):
    add=number[index] + carry_fwd
    if add == 10:
        result.insert(0,0)
        carry_fwd = 1
    else:
        result.insert(0,add)
        carry_fwd = 0
        
if carry_fwd ==1:
    result.insert(0,1)
    
print result
        
    