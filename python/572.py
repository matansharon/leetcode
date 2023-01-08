# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

# Example 1:


# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
# Example 2:


# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false
 

# Constraints:

# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -104 <= root.val <= 104
# -104 <= subRoot.val <= 104


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def get_all_sub_trees(self,root):
        self.all.append(root)
        if root.left:
            self.get_all_sub_trees(root.left)
        if root.right:
            self.get_all_sub_trees(root.right)
    def scan(self,root1,root2):
        
        if root1 and not root2:
            self.flag=False
            return
        if not root1 and root2:
            self.flag=False
            
        if root1 and root2:
            if root1.val != root2.val:
                self.flag=False

            self.scan(root1.left,root2.left)

            self.scan(root1.right,root2.right)
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        self.all=[]
        self.flag=True
        self.get_all_sub_trees(root)
        for i in self.all:
            self.flag=True
            self.scan(subRoot,i)
            if self.flag:
                print i
                return True
        return False
        
