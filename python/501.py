# Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

# If the tree has more than one mode, return them in any order.

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:


# Input: root = [1,null,2,2]
# Output: [2]
# Example 2:

# Input: root = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -105 <= Node.val <= 105
 

# Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).


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
        if node.val in self.dic:
            self.dic[node.val]+=1
        else:
            self.dic[node.val]=1
        self.scan(node.left)
        self.scan(node.right)
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.dic={}
        self.arr=[]
        self.scan(root)
        _max=0
        # print self.dic
        for i in self.dic:
            if self.dic[i]>_max:
                _max=self.dic[i]
        for i in self.dic:
            if self.dic[i]==_max:
                self.arr.append(i)
        return self.arr
