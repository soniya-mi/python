list = [9,9,1]
index = len(list)-1
cf = 1
output = []

while (index >= 0 ):
	add = list[index] + cf
	cf = 0
	if add > 9:
		output.append(0)
		cf = 1
	else:
		output.append(add)
	index = index - 1 

if cf > 0:
    output.append(cf)
print (output[::-1])

'''
n = 123
so array become list = [1,2,3]
add +1 to the the list and output should be ==> [1,2,4]
'''
