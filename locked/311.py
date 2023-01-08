# Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.

 

# Example 1:


# Input: mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]
# Output: [[7,0,0],[-7,0,3]]
# Example 2:

# Input: mat1 = [[0]], mat2 = [[0]]
# Output: [[0]]
 

# Constraints:

# m == mat1.length
# k == mat1[i].length == mat2.length
# n == mat2[i].length
# 1 <= m, n, k <= 100
# -100 <= mat1[i][j], mat2[i][j] <= 100


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        row1 = len(mat1)
        col1 = len(mat1[0])        
        row2 = len(mat2)
        col2 = len(mat2[0])
        
        ans = [[0]*col2 for _ in range(row1)]
        idict_row = {}
        idict_col = {}
        
        for i in range(row1):
            idict_row[i] = {}
            for j in range(col1):
                if mat1[i][j]!=0:
                    idict_row[i][j] = mat1[i][j]
                    
        for i in range(col2):
            idict_col[i] = {}
            for j in range(row2):
                if mat2[j][i]!=0:
                    idict_col[i][j] = mat2[j][i]
                    
        for i in range(row1):
            cur_row = idict_row[i]
            for j in range(col2):
                cur_res = 0
                cur_col = idict_col[j]
                for key,val in cur_row.items():
                    if key in cur_col:
                        cur_res += val*cur_col[key]
                ans[i][j] = cur_res
                    
        return ans
