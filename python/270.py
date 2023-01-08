# Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.

 

# Example 1:


# Input: root = [4,2,5,1,3], target = 3.714286
# Output: 4
# Example 2:

# Input: root = [1], target = 4.428571
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# 0 <= Node.val <= 109
# -109 <= target <= 109


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def scan(self,node):
        if node==None:
            return
        temp=abs(node.val-self.t)
        if temp<self.min:
            self.min=temp
            self.res=node.val
        self.scan(node.left)
        self.scan(node.right)
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.t=target
        self.min=9999999
        self.res=0
        self.scan(root)
        return self.res
