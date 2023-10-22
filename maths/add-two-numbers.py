l1 = [4,5,5]
l2 = [5,5,5]
cf = 0
#Output: [7,0,8]
l1=l1[::-1]
l2=l2[::-1]
max_length = len(max(l1,l2))

output = []
for index in range(0,max_length):
    if index < len(l1):
        first = l1[index] 
    else:
        first = 0
    if index < len(l2):
        sec = l2[index] 
    else:
        sec = 0
    sum = first + sec + cf
    num = sum % 10 
    cf = int(sum / 10)
    output.append(num)
    
if cf != 0:
    output.append(cf)
print (output[::-1])
