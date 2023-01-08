# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

# Example 1:


# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:


# Input: p = [1,2], q = [1,null,2]
# Output: false
# Example 3:


# Input: p = [1,2,1], q = [1,1,2]
# Output: false
 

# Constraints:

# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree_to_str(self,node,s):
        s.append(node.val)
        if node.left:
            self.tree_to_str(node.left,s)
        else:
            if node.right:
                s.append(None)
        if node.right:
            
            self.tree_to_str(node.right,s)
        else:
            s.append(None)
        return s
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (not (p) and q) or (q and not (p)):
            return False
        if not p and not q:
            return True
        s1=[]
        if p:
            s1=self.tree_to_str(p,s1)
        s2=[]
        if q:
            s2=self.tree_to_str(q,s2)
        return s1==s2
