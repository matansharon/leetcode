# Given a string num which represents an integer, return true if num is a strobogrammatic number.

# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

 

# Example 1:

# Input: num = "69"
# Output: true
# Example 2:

# Input: num = "88"
# Output: true
# Example 3:

# Input: num = "962"
# Output: false
# Example 4:

# Input: num = "1"
# Output: true
 

# Constraints:

# 1 <= num.length <= 50
# num consists of only digits.
# num does not contain any leading zeros except for zero itself.


class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        copy=[]
        for i in reversed(num):
            if i in '23457':
                return False
            if i=='9':
                copy.append('6')
            elif i=='6':
                copy.append('9')
            else:
                copy.append(i)
        num=list(num)
        print num
        print copy
        return num==copy
