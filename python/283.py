# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:
            return nums
        out=True
        ptr1=0
        while ptr1<len(nums):
            if nums[ptr1]==0:
                ptr2=ptr1
                while nums[ptr2]==0 and ptr2<len(nums)-1:
                    ptr2+=1
                temp=nums[ptr1]
                nums[ptr1]=nums[ptr2]
                nums[ptr2]=temp
            ptr1+=1
            
        
        
