s ="eesoeesauo"

flag =0
for i in s :
    if i in "a|e|i|o|u":
        flag =1
    else:
        flag =0

if flag == 1:
    print "Accepted"
else:
    print "NON accepted"
