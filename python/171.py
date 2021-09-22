# Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
 

# Example 1:

# Input: columnTitle = "A"
# Output: 1
# Example 2:

# Input: columnTitle = "AB"
# Output: 28
# Example 3:

# Input: columnTitle = "ZY"
# Output: 701
# Example 4:

# Input: columnTitle = "FXSHRXW"
# Output: 2147483647

class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ct=columnTitle
        res=0
        p=0
        for i in reversed(ct):
            res+= pow(26,p)*(alpha.index(i)+1)
            p+=1
        return res
