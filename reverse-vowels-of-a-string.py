s = "leetcode"
vowel = [ "a" , "e" , "i" , "o" , "u"]

new_list=""
for elem in s:
    if elem in vowel:
        new_list=new_list+elem

length=len(new_list)
new_str=""
for elem in s:
    if elem not in vowel:
        new_str=new_str+elem
    else:
        new_str=new_str+new_list[length-1]
        length=length-1
        
print(new_str)
        

'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
'''
