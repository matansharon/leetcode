# Given an array of unique integers preorder, return true if it is the correct preorder traversal sequence of a binary search tree.

 

# Example 1:


# Input: preorder = [5,2,1,3,6]
# Output: true
# Example 2:

# Input: preorder = [5,2,6,1,3]
# Output: false
 

# Constraints:

# 1 <= preorder.length <= 104
# 1 <= preorder[i] <= 104
# All the elements of preorder are unique.
 

# Follow up: Could you do it using only constant space complexity?


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stck, lo, n = [], -float('inf'), len(preorder)
        for i in range(n):
            if preorder[i] < lo:
                return False
            if i > 0 and preorder[i] > preorder[i-1]:  # update min threshold
                while stck and stck[-1] < preorder[i]:
                    lo = stck.pop()
            stck.append(preorder[i])
        return True
