##https://www.youtube.com/watch?v=-zSxTJkcdAo&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=3&pp=iAQB
# longest substring with no repeating characters brute force 

s = "abcabcbb"
dict = {}
maxcount = count = 0
for i in range(0,len(s)):
    dict={}
    count = 0
    for j in range(i,len(s)):
        if s[j] in dict:
            break
        else:
            dict[s[j]] = 1
            count = count + 1
            maxcount = max(maxcount,count)
        #print(dict , maxcount) 
print(maxcount) 


