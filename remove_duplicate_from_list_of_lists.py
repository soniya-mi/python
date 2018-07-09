def identify_duplicates(Sample_list):
    dict = {}
    count = 1
    new_list = []
    for list in Sample_list:
        for item in list :
            if item in dict.keys():
                count = dict[item]
                dict[item] = count + 1
                continue
            else:
                dict[item] = count
                new_list.append(item)
    print new_list



Sample_list = [[10, 20], [40], [30, 56, 25], [10, 20 , 30], [33], [40]]
identify_duplicates(Sample_list)