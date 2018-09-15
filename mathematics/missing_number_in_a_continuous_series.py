def missing_num(n,gvn_list):
    sum =0
    act_sum=0
    for item in gvn_list:
        sum = sum + item
    
    for item in range(1,11):
        act_sum = act_sum + item

    missing_n = act_sum - sum
    return missing_n
    
gvn_list = [1,2,3,4,5,7,8,9,10]
n = 10
print missing_num(n,gvn_list)



##################################################33
#parallel way
##################################################33
def missing_num(n,gvn_list):
    sum =0
    act_sum=(n*(n+1))/2
    
    for item in gvn_list:
        sum = sum + item
    missing_n = act_sum - sum
    return missing_n
    
gvn_list = [1,2,3,4,5,7,8,9,10]
n = 10
print missing_num(n,gvn_list)
