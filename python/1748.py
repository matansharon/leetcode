class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        for i in nums:
            temp=nums.count(i)
            if temp==1:
                res+=i
        return res
        
