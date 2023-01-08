# Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.

 

# Example 1:


# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2.00000
# Explanation: The five points are shown in the above figure. The red triangle is the largest.
# Example 2:

# Input: points = [[1,0],[0,0],[0,1]]
# Output: 0.50000


import math
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        res=0.0
        for i in range(len(points)):
            for j in range(len(points)):
                for k in range(len(points)):
                    a=points[i][0]
                    b=points[i][1]
                    c=points[j][0]
                    d=points[j][1]
                    e=points[k][0]
                    f=points[k][1]
                    d1=math.sqrt((a-c)**2+(b-d)**2)
                    d2=math.sqrt((a-e)**2+(b-f)**2)
                    d3=math.sqrt((c-e)**2+(d-f)**2)
                    s=(d1+d2+d3)/2
                    temp=(s*(s-d1)*(s-d2)*(s-d3))
                    if temp>0:
                        area=math.sqrt(temp)
                        res=max(res,area)
                        
                    
        return res
