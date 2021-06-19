class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in range(1,len(arr)):
            if i!=len(arr):
                m=max(arr[i:len(arr)])
                res.append(m)
            else:
                res.append(arr[i])
        res.append(-1)    
        return res
        
