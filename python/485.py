# Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=[]
        cnt=0
        con=False
        for i in nums:
            if i==1 and not con:
                con=True
                cnt+=1
            elif i==1 and con:
                cnt+=1
            elif i==0 and con:
                con=False
                res.append(cnt)
                cnt=0
        res.append(cnt)
        return max(res)
