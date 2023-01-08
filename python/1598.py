# The Leetcode file system keeps a log each time some user performs a change folder operation.

# The operations are described below:

# "../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
# "./" : Remain in the same folder.
# "x/" : Move to the child folder named x (This folder is guaranteed to always exist).
# You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.

# The file system starts in the main folder, then the operations in logs are performed.

# Return the minimum number of operations needed to go back to the main folder after the change folder operations.

 

# Example 1:



# Input: logs = ["d1/","d2/","../","d21/","./"]
# Output: 2
# Explanation: Use this change folder operation "../" 2 times and go back to the main folder.
# Example 2:



# Input: logs = ["d1/","d2/","./","d3/","../","d31/"]
# Output: 3
# Example 3:

# Input: logs = ["d1/","../","../","../"]
# Output: 0


class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        alpha='abcdefghijklmnopqrstuvwxyz'
        res=0
        for i in logs:
            if i[0]in alpha or i[0].isdigit():
                res+=1
            elif i[0]=='.' and i[1]=='.' and res>0:
                res-=1
        if res<0:
            return 0
        return res
