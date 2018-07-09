def missing_num(input):
    missing_nm = []
    for index in range(0,len(input)-1):
        diff = input[index+1] - input[index]
        if diff > 1 :
            for index_inner in range(1,diff):
                missing_nm.append(input[index] + index_inner)

    return missing_nm

input = [1,3,4,6,7,20]
print missing_num(input)