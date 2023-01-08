# Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

# You may assume the input array always has a valid answer.

 

# Example 1:

# Input: nums = [3,5,2,1,6,4]
# Output: [3,5,1,6,2,4]
# Explanation: [1,6,2,5,3,4] is also accepted.
# Example 2:

# Input: nums = [6,6,5,6,3,8]
# Output: [6,6,5,6,3,8]
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# 0 <= nums[i] <= 104
# It is guaranteed that there will be an answer for the given input nums.
 

# Follow up: Could you solve the problem in O(n) time complexity?


from collections import deque

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Init
        queue = deque(sorted(nums))
        nums.clear()
        flag = True
        
        # Wiggle sort
        while queue:
            nums.append(queue.popleft() if flag else queue.pop())
            flag = False if flag else True
        
        return
