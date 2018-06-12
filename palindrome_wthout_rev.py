string = "nitin"
len = len(string)
is_pal = True
for i in range(len/2):
    if string[i] == string[len-i-1]:
        continue
    else:
        is_pal=False
        break

if is_pal == True:
    print "Palindrome"
else:
    print "No Palindrome"