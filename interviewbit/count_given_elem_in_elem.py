def count_elem(list,x):
    count =0
    for item in list:
        if (item == x):
            count = count +1
    return count

list = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8

print count_elem(list,x)
print ('{} elemst has appeared {} time').format(x,count_elem(list,x))
