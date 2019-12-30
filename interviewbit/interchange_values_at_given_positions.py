list = [23, 65, 19, 90]


def swap(list,pos1,pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]


pos1=1
pos2=3
swap(list,pos1-1,pos2-1)

print list
