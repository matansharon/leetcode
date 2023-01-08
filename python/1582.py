# Given a rows x cols matrix mat, where mat[i][j] is either 0 or 1, return the number of special positions in mat.

# A position (i,j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

 

# Example 1:

# Input: mat = [[1,0,0],
#               [0,0,1],
#               [1,0,0]]
# Output: 1
# Explanation: (1,2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
# Example 2:

# Input: mat = [[1,0,0],
#               [0,1,0],
#               [0,0,1]]
# Output: 3
# Explanation: (0,0), (1,1) and (2,2) are special positions. 
# Example 3:

# Input: mat = [[0,0,0,1],
#               [1,0,0,0],
#               [0,1,1,0],
#               [0,0,0,0]]
# Output: 2
# Example 4:

# Input: mat = [[0,0,0,0,0],
#               [1,0,0,0,0],
#               [0,1,0,0,0],
#               [0,0,1,0,0],
#               [0,0,0,1,1]]
# Output: 3



class Solution(object):
    def get_col(self,pos,mat):
        res=[]
        for row in mat:
            res.append(row[pos])
        return res
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        
        res=0
        for i in range(len(mat)):
            
            for j in range(len(mat[0])):
                row=mat[i]
                col=self.get_col(j,mat)
                r=row.count(1)
                c=col.count(1)
                
                if r==c==1 and i==col.index(1):
                    res+=1
        
        return res
