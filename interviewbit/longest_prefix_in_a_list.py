list = [ "abc" , "abcd" , "abcde" , "abcdef"]
prefix=""
for index in range(0,len(list[0])):
    match = True
    for word in list:
        if index >= len(word):
            match= False
            break
        if word[index] == list[0][index]:
            match = True
        else:
            match  = False
            break
    if match == True:
        prefix=prefix+word[index]
    else:
        break

print prefix
            
    

