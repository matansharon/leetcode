class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp=sorted(nums)
        return (temp[-1]-1)*(temp[-2]-1)
        
