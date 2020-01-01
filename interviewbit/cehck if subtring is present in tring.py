test="Geeks For Geeks"
str="Geeks"
flag =0

inout_str=test.split()

for item in inout_str:
    if str == item:
        flag = 1
    else:
        flag = 0

if flag != 0 :
    print "sub string present "
else:
    print "substr not present"
