class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        mat=[]
        temp=[]
        for i in range(0,n):
            temp.append(0)
        for i in range(0,m):
            mat.append(list(temp))
            
        for i in indices:
            row=i[0]
            col=i[1]
            for j in range(0,n):
                mat[row][j]+=1
            for j in range(0,m):
                mat[j][col]+=1
        res=0
        for i in range(0,m):
            for j in range(0,n):
                
                if mat[i][j]%2==1:
                    res+=1
        return res
