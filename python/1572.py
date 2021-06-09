class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        pos=0
        res=0
        for arr in mat:
            if pos!=len(arr)-1-pos:
                res+=arr[pos]+arr[len(arr)-1-pos]
            else:
                res+=arr[pos]
            pos+=1
        return res
            
