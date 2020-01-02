str1 = 'abcdef'
str2 = 'defghia'

count =0

for char in str1:
    if char in str2:
        count = count +1

print count
