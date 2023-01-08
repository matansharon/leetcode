# Given a date, return the corresponding day of the week for that date.

# The input is given as three integers representing the day, month and year respectively.

# Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

 

# Example 1:

# Input: day = 31, month = 8, year = 2019
# Output: "Saturday"
# Example 2:

# Input: day = 18, month = 7, year = 1999
# Output: "Sunday"
# Example 3:

# Input: day = 15, month = 8, year = 1993
# Output: "Sunday"

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        res=[] 
        res.append(0)
        curr=0
        max_al=0
        for i in range(0,len(gain)):
            curr+=gain[i]
            if curr>max_al:
                max_al=curr
        return max_al
            
