# Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

 

# Example 1:

# Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column
# Example 2:

# Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
# Output: [12]
# Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
# Example 3:

# Input: matrix = [[7,8],[1,2]]
# Output: [7]


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
        
