# Given an integer n, return any array containing n unique integers such that they add up to 0.

 

# Example 1:

# Input: n = 5
# Output: [-7,-1,1,3,4]
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
# Example 2:

# Input: n = 3
# Output: [-1,0,1]
# Example 3:

# Input: n = 1
# Output: [0]

class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res=[]
        temp=1
        for i in range(0,n):
            if i%2==0:
                res.append(temp)
            else:
                res.append(-temp)
                temp+=1
        if n%2==1:
            res[-1]=0
        return res
            
