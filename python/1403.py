class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # if len(nums)==1:
        #     return nums
        res=[]
        while sum(res)<sum(nums)+1:
            m= nums.pop(nums.index(max(nums)))
            res.append(m)
        return res
            
            
