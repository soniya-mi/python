def add_till_single(number):
    add = 0
    while number > 0:
        dig = number % 10
        number = number / 10
        add = add + dig 
    
    return add
    
number = 12345
total=add_till_single(number)
print total