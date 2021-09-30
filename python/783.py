# Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

 

# Example 1:


# Input: root = [4,2,6,1,3]
# Output: 1
# Example 2:


# Input: root = [1,0,48,null,null,12,49]
# Output: 1


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
        self.arr.append(node.val)
        self.scan(node.left)
        self.scan(node.right)
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.arr=[]
        self.scan(root)
        self.arr.sort()
        _min=99999999
        print self.arr
        for i in range(len(self.arr)-1):
            if self.arr[i+1]-self.arr[i]<_min:
                _min=self.arr[i+1]-self.arr[i]
        return _min
