class Solution(object):
    def remove(self,s,pos):
        return s[:pos]+s[pos+2:]
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        _s=s
        len1=len(s)
        i=0
        while i<len1-1:
            
            if _s[i]==_s[i+1]:
                _s=self.remove(_s,i)
                
                len1-=2
                i-=2
                if i<0:
                    i=0
            else:
                i+=1
        return _s
            
