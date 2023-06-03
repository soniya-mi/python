class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        position = 0
        for index in range(0,len(nums)):
            if nums[index] == 0 :
                count = count+1
            else:
                nums[position] = nums[index]
                position = position + 1

        for index in range(position,len(nums)):
            nums[index] = 0
    
        

    
'''
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
'''
      
        
