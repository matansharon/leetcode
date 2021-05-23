class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        count=0
        for i in s:
            if i=='R':
                count+=1
            else:
                count-=1
            if count==0:
                res+=1
        return res
            
