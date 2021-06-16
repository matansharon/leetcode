class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        num=n
        res=0
        while num>0:
            r=num%k
            res+=r
            num/=k
        return res
        
