class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        res=[]
        for i in range(0,len(mat)):
            try:
                res.append([mat[i].index(0),i])
            except:
                res.append([len(mat[i]),i])
        res.sort()
        arr=[]
        for i in range(0,k):
            arr.append(res[i][1])
        return arr
        
        
