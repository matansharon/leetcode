class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        nums=[]
        res=start
        
        for i in range(1,n):
            temp=start+i*2
            res^=temp
        return res
