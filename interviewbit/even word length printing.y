s = "This is a python a a sin language"

input=s.split()

#method 1 with inbuilt
for i in input:
    if len(i) % 2 == 0 :
        print i


#method 2
for i in input:
    count = 0
    for char in i:
        count = count + 1
    if count % 2 == 0:
        print i
