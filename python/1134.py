class Solution(object):
    def isArmstrong(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s=str(n)
        
        res=0
        for i in s:
            res+=math.pow(int(i),len(s))
        
        return res==n
    
