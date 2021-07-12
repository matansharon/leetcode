class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr=[]
        r=''
        for i in reversed(s):
            r+=i
        if r==s:
            return 1
        return 2
        
