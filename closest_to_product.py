list = [4,3,1,2]
new_list = []
prod = 1
k = 5


for index in range(0,len(list)):
    for i in range ( 0, len(list)):
        if i != index : 
            prod = list[i] * list[index]
            diff = abs(k - prod)
            new_list.append(diff)
 
least = new_list[0]   
closest = 0

for item in range(1,len(new_list)):
    if new_list[item] < least :  
        #print   new_list[item] , least
        least = new_list[item]

print least
            
            

    