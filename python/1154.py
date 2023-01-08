# Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

 

# Example 1:

# Input: date = "2019-01-09"
# Output: 9
# Explanation: Given date is the 9th day of the year in 2019.
# Example 2:

# Input: date = "2019-02-10"
# Output: 41
# Example 3:

# Input: date = "2003-03-01"
# Output: 60
# Example 4:

# Input: date = "2004-03-01"
# Output: 61
 

# Constraints:

# date.length == 10
# date[4] == date[7] == '-', and all other date[i]'s are digits
# date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.


import datetime
class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        date=date.split('-')
        year=int(date[0])
        month=int(date[1])
        day=int(date[2])
        res=datetime.date(year,month,day)
        f=datetime.date(year-1,12,31)
        
        # return res.timetuple().tm_yday
        r=(res-f)
        return (r.days)
        
