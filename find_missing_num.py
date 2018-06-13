def missing_num(n, gvn_list):
    missing_sum = 0

    actual_sum = (n*(n+1))/2

    for i in gvn_list:
        missing_sum = missing_sum + i
    
    m_num = actual_sum-missing_sum
    return m_num


gvn_list = [1,2,3,4,5,7,8,9,10]
n = 10
num = missing_num(n,gvn_list)
print num