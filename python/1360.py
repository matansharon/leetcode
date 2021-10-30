# Write a program to count the number of days between two dates.

# The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

 

# Example 1:

# Input: date1 = "2019-06-29", date2 = "2019-06-30"
# Output: 1
# Example 2:

# Input: date1 = "2020-01-15", date2 = "2019-12-31"
# Output: 15
 

# Constraints:

# The given dates are valid dates between the years 1971 and 2100.


import datetime
class Solution(object):
    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """
        date1=date1.split('-')
        date2=date2.split('-')
        date1=datetime.datetime(int(date1[0]),int(date1[1]),int(date1[2]))
        date2=datetime.datetime(int(date2[0]),int(date2[1]),int(date2[2]))
        temp=date2-date1
        return abs(temp.days)
