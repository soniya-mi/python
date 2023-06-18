n= 5

for row in range(0, n+1):
	# space
	for col in range(0, n+1 - row):
		print(" ", end="")
		
	# *
	for col in range(0, row*2):
		print("*", end="")
	

	print("")

'''
     **
    ****
   ******
  ********
 **********
'''
