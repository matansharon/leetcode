# Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

 

# Example 1:


# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true
# Example 2:


# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false
# Example 3:

# Input: root = [2,1,3], k = 4
# Output: true
# Example 4:

# Input: root = [2,1,3], k = 1
# Output: false
# Example 5:

# Input: root = [2,1,3], k = 3
# Output: true


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
        if self.k-node.val in self.dic:
            self.flag=True
        self.dic[node.val]=self.k-node.val
        
        self.scan(node.left)
        self.scan(node.right)
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        
        self.flag=False
        self.dic={}
        self.k=k
        self.scan(root)
        if len(self.dic)<2:
            return False
        # print self.dic
        return self.flag
