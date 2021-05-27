class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        res=0
        for word in words:
            flag=True
            for w in word:
                pos=allowed.find(w)
                if pos==-1:
                    flag=False
                    break
            if flag:
                res+=1
        return res
      
