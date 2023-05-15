def selectionSort(data,size):
    
    for i in range(0,size):
        min = i
        print ("min" , min)
        for j in range(i,size):
            print ( data[min] , data[j])
            if ( data[min] > data[j]):
                min=j
        data[i],data[min]=data[min],data[i]    
    
    print (data)
# Driver code
data = [ 7, 2, 1, 6 ]
size = len(data)
selectionSort(data, size)


'''
min 0
7 7
7 2
2 1
1 6
min 1
2 2
2 7
2 6
min 2
7 7
7 6
min 3
7 7
[1, 2, 6, 7]
> 
'''
