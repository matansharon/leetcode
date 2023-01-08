class Solution(object):
    
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        res=0
        for i in range(len(strs[0])):
            arr=[]
            for s in strs:
                arr.append(s[i])
            if arr !=sorted(arr):
                res+=1
        return res
        
