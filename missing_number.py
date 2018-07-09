def missing_num(input):
    sum = 0
    expected_sum = 0
    for number in range(1,9):
        expected_sum = expected_sum + number
    for index in range(0,len(input)):
        sum = sum + input[index]

    missing_num = expected_sum-sum
    return missing_num

#input = [1,2,7,4,3,6,8]
input =  [1,2,3,4,6,7,8]
print missing_num(input)