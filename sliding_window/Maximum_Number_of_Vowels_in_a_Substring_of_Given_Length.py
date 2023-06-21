s = "leetcode"
k = 3
max = 0
for char_index in range(0,len(s)-k):
    count = 0 
    for index in range(char_index , char_index+k):
        if s[index] in ["a","e","i","o","u"]:
            count = count + 1
    if count == k:
        print ("k found")
        break
    elif count > max:
        max = count
print (max)

'''
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?envType=study-plan-v2&envId=leetcode-75
Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
'''
