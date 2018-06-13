list = [1,2,3,4,5,6,7,8]
k = 8
def add( num1 , num2):
    return num1+num2
for index in range(len(list)):
    for again_index in range(len(list)): 
        #print index , again_index
        if again_index != index:
                #print index , again_index
                sum = add (list[again_index] , list[index])
                #print sum 
                if k == sum : 
                    print  list[again_index] , list[index]
