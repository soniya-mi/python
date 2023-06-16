nums = [1,2,2,3,1,4,2]
dict = {}
l = {}
r = {}

count = 1
for index in range(0,len(nums)):
    if nums[index] in dict:
        count = dict[nums[index]] + 1
        dict[nums[index]] = count
        r[nums[index]] = index
    else:
        dict[nums[index]] = 1
        l[nums[index]] = index
        r[nums[index]] = index

print (dict)

max_count = max(dict.values())

mini = len(nums)+1

for k,v in dict.items():
    if v == max_count:
        length = r[k] - l[k] + 1
    
        if length < mini:
            mini = length
    
print (mini)
"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:

Input: nums = [1,2,2,3,1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:

Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation: 
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
"""
