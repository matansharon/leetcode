# Given an integer array nums, return 0 if the sum of the digits of the minimum integer in nums is odd, or 1 otherwise.

 

# Example 1:

# Input: nums = [34,23,1,24,75,33,54,8]
# Output: 0
# Explanation: The minimal element is 1, and the sum of those digits is 1 which is odd, so the answer is 0.
# Example 2:

# Input: nums = [99,77,33,66,55]
# Output: 1
# Explanation: The minimal element is 33, and the sum of those digits is 3 + 3 = 6 which is even, so the answer is 1.


class Solution(object):
    def sumOfDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp=min(nums)
        res=0
        while temp>0:
            
            res+= temp%10
            temp/=10
        if res%2==0:
            return 1
        return 0
