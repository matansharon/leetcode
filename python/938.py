# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        stack=[root]
        res=0
        while stack:
            node=stack.pop()
            if node:
                if low<=node.val<=high:
                    res+=node.val
                if node.val<high:
                    stack.append(node.right)
                if node.val>low:
                    stack.append(node.left)
        return res
        
