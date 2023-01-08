# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]



class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==1:
            return [[1]]
        res=[[1],[1,1]]
        for i in range(3,numRows+1):
            res.append([0]*(i))
        for i in range(1,len(res)-1):
            prev=res[i]
            curr=res[i+1]
            for j in range(0,len(curr)):
                if j==0 or j==len(curr)-1:
                    curr[j]=1
                else:
                    curr[j]=prev[j-1]+prev[j]
        return res
