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
