class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res=[]
        temp=1
        for i in range(0,n):
            if i%2==0:
                res.append(temp)
            else:
                res.append(-temp)
                temp+=1
        if n%2==1:
            res[-1]=0
        return res
            
