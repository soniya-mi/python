def sum_of_n_dig(N):
    sum = 0
    while N >= 1:
        digit = N % 10
        N = N / 10
        sum = sum + digit
    return sum

def find_x(N):
    orig_n = N
    while N > 9:
        N = sum_of_n_dig(N)
    x =2
    while x <= orig_n:
         y = x
         if orig_n % x == 0 :
             while x > 9 :
                 x  = sum_of_n_dig(x)
                 if x == N :
                     print x
    x=y + 1

N = 190
find_x(N)