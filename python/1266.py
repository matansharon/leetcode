import math
class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res=0
        for p in range(0,len(points)-1):
            curr=points[p]
            nextp=points[p+1]
            xdiff=abs(nextp[0]-curr[0])
            ydiff=abs(nextp[1]-curr[1])
            print(xdiff,ydiff)
            res+=min(xdiff,ydiff)+abs(xdiff-ydiff)
        return res
