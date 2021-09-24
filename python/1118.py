# Given a year year and a month month, return the number of days of that month.

 

# Example 1:

# Input: year = 1992, month = 7
# Output: 31
# Example 2:

# Input: year = 2000, month = 2
# Output: 29
# Example 3:

# Input: year = 1900, month = 2
# Output: 28


from calendar import monthrange
class Solution(object):
    def numberOfDays(self, Y, M):
        """
        :type Y: int
        :type M: int
        :rtype: int
        """
        
        return monthrange(Y,M)[1]
