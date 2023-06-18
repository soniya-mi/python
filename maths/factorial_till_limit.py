limits = 5
#fact=1

for n in range(1,limits+1):
    fact = 1
    while (n > 1):
        fact = fact * n
        n = n - 1
    print (fact)

'''
1
2
6
24
120
'''
    
