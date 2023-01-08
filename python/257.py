
# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.

 

# Example 1:


# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
# Example 2:

# Input: root = [1]
# Output: ["1"]
  
  
  
  
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def is_leaf(self,node):
        if node.right==None and node.left==None:
            return True
        return False
    def path(self,node,st):
        st+=str(node.val)+'->'
        if self.is_leaf(node):
            st=st[:-2]
            self.res.append(st)
        if node.left:
            self.path(node.left,st)
        if node.right:
            self.path(node.right,st)
            
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.res=[]
        st=''
        self.path(root,st)
        return self.res
        
