char = "*"

n = 5

for r_index in range(0,n): #0,1
	for c_index in range(0,r_index+1): #001
	    print ("*" , end="")
	print ("")

#with single looop
for index in range(0,n):
	string = string + "*"
	print (string)
#print (string)
print ()
'''
*
**
***
****
*****
'''
