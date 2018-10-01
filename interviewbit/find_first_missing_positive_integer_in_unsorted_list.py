def missing_no(orig_list):
    for index in range(1,len(orig_list)+2):
        if index in orig_list:
            continue
        else:
            return index

orig_list=[-1,3,6,1]
print missing_no(orig_list)