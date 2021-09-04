# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

 

# Example 1:

# Input: nums = [2,1,2]
# Output: 5
# Example 2:

# Input: nums = [1,2,1]
# Output: 0
# Example 3:

# Input: nums = [3,2,3,4]
# Output: 10
# Example 4:

# Input: nums = [3,6,2,3]
# Output: 8

class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        a=b=c=0
        while   len(nums)>0:
            try:
                c=nums.pop(nums.index(max(nums)))
                a=nums.pop(nums.index(max(nums)))
                b=nums.pop(nums.index(max(nums)))
            except:
                return 0
            if b+a>c:
                return a+b+c
            else:
                nums.append(b)
                nums.append(a)
