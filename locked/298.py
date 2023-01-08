# Given the root of a binary tree, return the length of the longest consecutive sequence path.

# The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path needs to be from parent to child (cannot be the reverse).

 

# Example 1:


# Input: root = [1,null,3,2,4,null,null,null,5]
# Output: 3
# Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
# Example 2:


# Input: root = [2,null,3,2,null,1]
# Output: 2
# Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 3 * 104].
# -3 * 104 <= Node.val <= 3 * 104


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
            q = deque()
            longest = 1
            q.append((root, -1000000 ,1))
            while q:
                node, prev_val, length = q.popleft()
                if not node: continue
                if node.val == prev_val + 1: length += 1
                else: length = 1
                longest = max(longest, length)
                q.append((node.left, node.val, length))
                q.append((node.right, node.val, length))
            return longest
