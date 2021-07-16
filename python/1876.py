class Solution(object):
    def check_for_good(self,sub):
        for i in range(len(sub)):
                if sub[i] in sub[i+1:]:
                    print False,sub
                    return False
        print True,sub
        return True
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        if len(s)<3:
            return 0
        if len(s)==3:
            if self.check_for_good(s):
                res+=1
            
        else:
            for i in range(0,len(s)-2):
                sub=s[i:i+3]
                if self.check_for_good(sub):
                    res+=1
        return res
        
