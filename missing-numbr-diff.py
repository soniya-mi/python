def missing_num(input):
    sum = 0
    for index in range(0,len(input)-1):
        diff = input[index+1] - input[index]
        if diff > 1 :
            missing_nm = input[index] + 1

    return missing_nm

input =  [1,3,4,5,6,7,8]
print missing_num(input)