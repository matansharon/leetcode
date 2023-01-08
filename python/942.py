class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        arr=range(0,len(s)+1)
        res=[]
        
      
        for i in s:
            if i=='I':
                m=min(arr)
            else:
                m=max(arr)
            pos=arr.index(m)
            temp=arr.pop(pos)
            res.append(temp)
        res.append(arr.pop())
        return res
                
