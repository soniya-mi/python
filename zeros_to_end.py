def push_zero(list):
    count = 0
    new_list = []
    for item in list:
        if item == 0 :
            count = count +1
        else:
            new_list.append(item)
    for number in range(0,count):
        new_list.append(0)

    print new_list
list = [0,2,3,0,4,6,0,7,10]
push_zero(list)


