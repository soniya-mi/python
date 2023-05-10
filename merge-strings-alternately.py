word1 = "abc"
word2 = "pqrs"
length=0

if len(word1) < len(word2):
    length=len(word1)
    slice1=word2[length:]
elif len(word1) > len(word2):
    length=len(word2)
    slice1=word1[length:]
else:
    length=len(word1)
    slice1=""

new_string=""
for i in range(0,length):
    new_string=new_string+word1[i]+word2[i]

new_string=new_string+slice1
print (new_string)

    

'''
Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
'''

