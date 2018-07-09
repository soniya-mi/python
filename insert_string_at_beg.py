def add_string(Sample_list,string):
    #new_list = []
    #for item in Sample_list:
    #    item = str(item)
    #    new_list.append(string+item)
    #return new_list
    for index in range(0,len(Sample_list)):
        Sample_list[index] = string+str(Sample_list[index])
    return Sample_list
Sample_list = [1,2,3,4]
string = "emp"

print add_string(Sample_list,string)