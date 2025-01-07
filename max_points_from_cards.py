## maximum points we can obtain from deck of cards.
## https://www.youtube.com/watch?v=pBWCOCS636U&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=2&pp=iAQB

k = 4
s = [6,2,3,4,7,2,1,7,1]
lsum = 0 
rsum = 0
maxsum = 0
rindex = len(s) - 1

for i in range ( 0, k ):
    lsum = lsum + s[i] 
    
maxsum = lsum

for i in range(k-1,0,-1):
    lsum = lsum - s[i]
    rsum = rsum + s[rindex]
    sum = rsum+lsum
    rindex = rindex -1
    maxsum = max (maxsum,sum)
print (maxsum)


