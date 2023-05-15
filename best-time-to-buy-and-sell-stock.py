input = [9,2,4,3,8,5]

maxprofit=0
for i in range ( 0 , len(input)):
    for j in range (i+1,len(input)):
        diff = input[j] - input[i]
        #print (input[i],input[j], diff , maxprofit)
        if diff > 0 and diff > maxprofit:
            maxprofit = diff
            day = j
            buying = i
            
            
            
print (maxprofit ,day ,  buying)

#https://levelup.gitconnected.com/coding-interview-question-best-time-to-buy-and-sell-stock-351314bfa37

'''
Sample Input and Output
Example 1:

Input: [9,2,4,3,8,5]
Output: 6
Explanation: Buy on day 1 (price = 2) and sell on day 4 (price = 8), profit = 8-2 = 6.
Example 2:

Input: [9,8,7,6,5]
Output: 0
Explanation: Since all pricing are decreasing, we would never buy, so max profit = 0.
'''
            
            
