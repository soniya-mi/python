def sum_the_list (Sample_lists):
    new_list = []
    max = 0
    for list in Sample_lists:
        sum = 0
        for item in list:
            sum = sum + item
        if sum > max :
            max = sum
            new_list = list
    print new_list


Sample_lists =  [[111,112,11], [14,15,61], [10,11,12], [7,8,9]]
sum_the_list(Sample_lists)
