class Solution(object):
    def get_col(self,mat,pos):
        col=[]
        for row in mat:
            col.append(row[pos])
        
        return col
        
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res=[]
        mins=[]
        maxs=[]
        for i in range(len(matrix[0])):
            maxs.append(max(self.get_col(matrix,i)))
        for row in matrix:
            mins.append(min(row))
        for i in mins:
            if i in maxs:
                res.append(i)
        return res
        
