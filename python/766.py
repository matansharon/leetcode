# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

 

# Example 1:


# Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# Output: true
# Explanation:
# In the above grid, the diagonals are:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
# In each diagonal all elements are the same, so the answer is True.
# Example 2:


# Input: matrix = [[1,2],[2,2]]
# Output: false
# Explanation:
# The diagonal "[1, 2]" has different elements.



class Solution(object):
    def creat_digonal(self,row,col,matrix):
        res=[]
        while row>-1 and col>-1:
            try:
                res.append(matrix[row][col])
            except:
                pass
            row-=1
            col-=1
        return res
    def check_diagonal(self,digonal):
        if len(digonal)==0:
            return True
        num=digonal[0]
        for i in digonal:
            if i!= num:
                return False
        return True
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        row=len(matrix)-1
        col=0
        while  col<len(matrix[0]):
            d=self.creat_digonal(row,col,matrix)
            if self.check_diagonal(d)==False:
                return False
            col+=1
        row=len(matrix)-1
        col=len(matrix[0])
        while row>-1:
            d=self.creat_digonal(row,col,matrix)
            if self.check_diagonal(d)==False:
                return False
            row-=1
        return True
      
# 
