# Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

# Two nodes of a binary tree are cousins if they have the same depth with different parents.

# Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

 

# Example 1:


# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
# Example 2:


# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true
# Example 3:


# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false
 

# Constraints:

# The number of nodes in the tree is in the range [2, 100].
# 1 <= Node.val <= 100
# Each node has a unique value.
# x != y
# x and y are exist in the tree.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def scan(self,prev,node,depth):
        if node==None:
            return
        if node.val==self.x:
            self.x_p=prev
            self.x_depth=depth
        if node.val==self.y:
            self.y_p=prev
            self.y_depth=depth
        self.scan(node,node.left,depth+1)
        self.scan(node,node.right,depth+1)
        
            
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if x==root.val or y==root.val:
            return False
        self.x=x
        self.y=y
        self.x_p=None
        self.y_p=None
        self.x_depth=0
        self.y_depth=0
        self.scan(root,root.left,0)
        self.scan(root,root.right,0)
        if self.x_depth!=self.y_depth:
            return False
        if self.x_p ==self.y_p:
            return False
        return True
        
