class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        low='abcdefghi'
        up='jklmnopqrstuvwxyz'
        res=''
        result=''
        pos=len(s)-1
        while pos>-1:
            if s[pos]=='#':
                temp_s=s[pos-2]+s[pos-1]
                temp_i=int(temp_s)
               
                res+=up[temp_i-10]
                
                pos-=3
            else:
                temp_i=int(s[pos])
                res+=low[temp_i-1]
                
                pos-=1
        for i in range(len(res)-1,-1,-1):
            result+=res[i]
        return result
