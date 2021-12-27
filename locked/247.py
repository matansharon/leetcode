# Given an integer n, return all the strobogrammatic numbers that are of length n. You may return the answer in any order.

# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

 

# Example 1:

# Input: n = 2
# Output: ["11","69","88","96"]
# Example 2:

# Input: n = 1
# Output: ["0","1","8"]
 

# Constraints:

# 1 <= n <= 14

class Solution:        
    def findStrobogrammatic(self, n: int) -> List[str]:
        if n == 1: return ['0', '1', '8']        
        self.map = {'0':'0', '1':'1', '8':'8', '6':'9',  '9':'6'}                
        self.result = []
        
        def store(s):
            self.result.append(''.join(s[:]))
            return ''.join(s[:])

        def btrack(L, R, curr):
            if curr[0] == '0': return
            if L > R:
                store(curr)
                return
            
            if  L == R:
                for c in '018':
                    curr[L] = c
                    store(curr)
                return 
            
            for k in self.map:
                curr[L] = k
                curr[R] = self.map[k]
                btrack(L + 1, R - 1, curr)        
                                
        btrack(0, n - 1, [None] * n)

        return self.result
