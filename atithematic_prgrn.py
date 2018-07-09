def progression_check(list):
    if len(list) < 2:
        print "it is a progression list"
        return
    is_prgren = True
    diff = list[1] - list[0]
    prev_diff = 0
    for index in range(0,len(list)-1):
        prev_diff = diff
        diff = list[index+1] - list[index]
        if diff != prev_diff:
            is_prgren = False

    if is_prgren == True:
        print "List is in progression"

list = [5, 7, 8, 11]

progression_check(list)