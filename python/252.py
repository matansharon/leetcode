# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

 

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false
# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: true

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        inter=sorted(intervals)
        print inter
        for i in range(len(inter)-1):
            t=inter[i]
            q=inter[i+1]
            if t[0] <=q[0] and t[1]>=q[1]:
                
                return False
            if t[0]>=q[0]:
                
                return False
            if t[0]<=q[0] and t[1]>q[0]:
                
                return False
        return True
