class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        alist=[]
        res=0
        for i in nums:
            res+=i
            alist.append(res)
        return alist
