def progression(list):
    diff = 0
    is_prg=True
    diff = list[1]-list[0]
    prev_diff=0
    for index in range(0,len(list)-1):
        prev_diff=diff
        diff = list[index+1] - list[index]
        if diff != prev_diff:
            is_prg = False
    if is_prg == True:
        print "list is in progression"
    else:
        print "list is not in progression"
            

list = [5, 7, 8, 11]

progression(list) 