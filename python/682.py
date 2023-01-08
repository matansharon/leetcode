class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        res=[]
        for i in ops:
            if i[0]=='-' or i.isdigit():
                res.append(int(i))
            
            elif i=='C':
                    res.pop()
            elif i=='D':
                res.append(res[-1]*2)
            elif i =='+':
                res.append(res[-1]+res[-2])
           
        return sum(res)
        
