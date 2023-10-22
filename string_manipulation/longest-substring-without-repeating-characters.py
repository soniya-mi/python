s= "pwwkew"
#Output: 3
myset=set()
prev_max=0

for char in s:
    if char not in myset:
        myset.add(char)
    else:
        if len(myset) > prev_max:
            prev_max=len(myset)
        myset = set()
        myset.add(char)
if len(myset) > prev_max:
    prev_max=len(myset)
print (prev_max)

#does not work for input : 
#s = "pwwkew"
