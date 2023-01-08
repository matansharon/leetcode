# Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

 

# Example 1:

# Input: nums = [-2,0,1,3], target = 2
# Output: 2
# Explanation: Because there are two triplets which sums are less than 2:
# [-2,0,1]
# [-2,0,3]
# Example 2:

# Input: nums = [], target = 0
# Output: 0
# Example 3:

# Input: nums = [0], target = 0
# Output: 0
 

# Constraints:

# n == nums.length
# 0 <= n <= 3500
# -100 <= nums[i] <= 100
# -100 <= target <= 100


class Solution:
    #https://leetcode.com/problems/valid-triangle-number/discuss/1512630/Python-solution-with-explanation
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
        res = 0
        nums.sort()
        N = len(nums)
        
        for i in range(N-1):
            left, right = i+1, N-1
            while (left < right):
                totSum = nums[i] + nums[left] + nums[right]
                if totSum < target:
                    res += (right - left)
                    left += 1
                else:
                    right -= 1
        
        return res
