class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=[0,1]
        if n==0:
            return 0
        if n==1:
            return 1
        for i in range(2,n+1):
            res.append(res[i-2]+res[i-1])
        # return res[n-1]
        return res[n]
