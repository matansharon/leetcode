# Numbers can be regarded as the product of their factors.

# For example, 8 = 2 x 2 x 2 = 2 x 4.
# Given an integer n, return all possible combinations of its factors. You may return the answer in any order.

# Note that the factors should be in the range [2, n - 1].

 

# Example 1:

# Input: n = 1
# Output: []
# Example 2:

# Input: n = 12
# Output: [[2,6],[3,4],[2,2,3]]
# Example 3:

# Input: n = 37
# Output: []
 

# Constraints:

# 1 <= n <= 107


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res, level = [], []
        for d in range(2, int(sqrt(n))+1):
            if n % d == 0:
                level.append( [d, n//d] )
        while level:
            new = []
            for chain in level:
                res.append( chain[:] )
                cur = chain.pop()
                start, end = chain[-1], int(sqrt(cur))
                for d in range(start, end+1): # key: gurantee monotonous increase
                    if (cur % d == 0):
                        new.append( chain + [d, cur//d] )
            level = new
        return res
