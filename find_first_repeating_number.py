arr = [10, 5, 3, 4, 3, 5, 6]
dict = {}
count = 0
for elem in arr:
    if elem in dict:
        count = dict[elem]
        count = count + 1
        dict[elem] = count
    else:
        dict[elem] = 1
print (dict)


for seq in arr:
    if dict[seq] > 1:
        print ("hi" , seq)
        break
    else:
        print ("hello", seq)
        
'''Input: arr[] = {10, 5, 3, 4, 3, 5, 6}
Output: 5 
Explanation: 5 is the first element that repeats

Input: arr[] = {6, 10, 5, 4, 9, 120, 4, 6, 10}
Output: 6 
Explanation: 6 is the first element that repeats'''
