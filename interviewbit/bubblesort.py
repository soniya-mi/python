def bubbleSort(arr):
    length=len(arr)
    for i in range(0,length):
        for j in range (0,length-1-i):
            print (i,j , j+1)
            if (arr[j] > arr [j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    
    print(arr)
    
    
arr = [1, 2, 10, 23]
 
bubbleSort(arr)

'''
0 0 1
0 1 2
0 2 3
1 0 1
1 1 2
2 0 1
[1, 2, 10, 23]
> 

'''
