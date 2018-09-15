def sum_the_list(list):
    prev_sum =0
    new_list = []
    for l in list:
        sum = 0 
        for item in l:
            sum = sum + item
        if sum > prev_sum:
            prev_sum = sum
            new_list = l
    print new_list, prev_sum
        
Sample_lists =  [[111,112,11], [14,15,61], [10,11,12], [7,8,9]]
sum_the_list(Sample_lists)