def check_upper(list):
    for item in list:
        if item.isupper() == True:
            return True
        else:
            return False
list = ['A' , 'b' , 'C' , 'd']
a = filter(check_upper , list)
print a