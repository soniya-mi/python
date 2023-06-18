n= 5
	
for row in range(1, n+1):
	# space
	for col in range(1, n+1 - row):
		print(" ", end="")
		
	# *
	for col in range(0, row):
		print("*", end="")
		
	print("")

'''
   *
   **
  ***
 ****
*****
'''
