string = "my name is minal her name is soniya"
list = string.split(" ")
occur= {}
for item in list:
    count = 1 
    if item in occur.keys():
        count = occur[item]
        occur[item] = count + 1
    else:
        occur[item] = count
print occur