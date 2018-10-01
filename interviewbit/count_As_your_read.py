def find_next(string):
    count = 1
    prev_char=""
    new_string=""
    prev_char=string[0]
    char=""
    for index in range(1,len(string)):
        char =string[index]
        if char == prev_char:
            count = count + 1
            
        else:
            new_string=new_string+str(count)+prev_char
            prev_char=char
            count = 1
    new_string=new_string+str(count)+prev_char
    return new_string

n = 4
result=[]
string = "1"
for index in range(1,n+1):
    #print string
    string = find_next(string)
    result.append(string)
print result
