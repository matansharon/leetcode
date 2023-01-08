class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        arr=sorted(nums)
        for i in range(0,len(arr),2):
            res+=arr[i]
        
        return res
