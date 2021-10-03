# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:

# Input: rowIndex = 0
# Output: [1]
# Example 3:

# Input: rowIndex = 1
# Output: [1,1]
 

# Constraints:

# 0 <= rowIndex <= 33

class Solution(object):
    def fill_next_row(self,prev):
        
        res=[]
        res.append(1)
        for i in range(0,len(prev)-1):
            res.append(prev[i]+prev[i+1])
        res.append(1)
        return res
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res=[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1]]
        
        
        for row in range(6,34):
            prev=res[row-1]
            
            res.append(self.fill_next_row(prev))
        return res[rowIndex]
        
            
