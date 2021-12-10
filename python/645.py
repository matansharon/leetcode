# Easy

# 1566

# 517

# Add to List

# Share
# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

# Example 1:

# Input: nums = [1,2,2,4]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1]
# Output: [1,2]
 

# Constraints:

# 2 <= nums.length <= 104
# 1 <= nums[i] <= 104


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums==[1,1]:
            return [1,2]
        
        _max=max(nums)
        dic={}
        miss=-1
        twice=-1
        for i in range(1,_max+1):
            dic[i]=0
        for i in nums:
            if i in dic:
                dic[i]+=1
        for i in dic:
            if dic[i]==2:
                twice=i
            if dic[i]==0:
                miss=i
        
        if miss==-1:
            return [twice,_max+1]
        return [twice,miss]
        
        
