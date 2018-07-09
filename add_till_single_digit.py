def digit_sum(number):
    sum = 0
    while number > 0:
        rem = number % 10
        number = number / 10
        sum = sum + rem
    return sum

def add_list(number):
    while number > 9:
        number = digit_sum(number)
    return number

number = 9850
print add_list(number)
