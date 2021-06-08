class Solution(object):
    def my_fac(self,val):
        res=0
        for i in range(0,val+1):
            res+=1
        return res

    def countLetters(self, s):
        """
        :type s: str
        :rtype: int
        """
        row=1
        total=1
        for i in range(0,len(s)-1):
            if s[i]==s[i+1]:
                row+=1
            else:
                row=1
            total+=row
        
        return total
        
