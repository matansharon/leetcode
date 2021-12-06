# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

 

 

# Example 1:



# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true
# Example 2:



# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false
 

# Constraints:

# 2 <= coordinates.length <= 1000
# coordinates[i].length == 2
# -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
# coordinates contains no duplicate point.


class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        x_diff = (coordinates[0][0] - coordinates[1][0]) # grab first coordinates as baseline
        y_diff = coordinates[0][1] - coordinates[1][1] # grab first coordinates as baseline
        if x_diff == 0: # can't divide by zero so if first x_diff is 0, check that they're all 0
            for i in range(len(coordinates)-1):
                x = coordinates[i][0]
                next_x = coordinates[i+1][0]
                if x != next_x:
                    return False
        else: # check if all slopes are the same
            slope = y_diff/x_diff
            for i in range(len(coordinates)-1):
                x = coordinates[i][0]
                next_x = coordinates[i+1][0]
                y = coordinates[i][1]
                next_y = coordinates[i+1][1]
                if (x-next_x) == 0:
                    return False
                elif (y-next_y)/(x-next_x) != slope:
                    return False
        return True
        
        
#         x=[]
#         y=[]
#         coor=coordinates
#         for i in coor:
#             x.append(i[0])
#             y.append(i[1])
#         x.sort()
#         y.sort()
#         difx=(x[1]-x[0])
#         dify=(y[1]-y[0])
#         x0=x[0]
#         xflag=True
#         for i in x:
#             if i!=x0:
#                 xflag=False
        
#         if xflag:
#             return True
#         y0=y[0]
#         flagy=True
#         for i in y:
#             if i!=y0:
#                 flagy=False
#         if flagy:
#             return True
#         slop=dify/difx
        
#         for i in range(len(x)-1):
#             t_difx=x[i+1]-x[i]
#             t_dify=y[i+1]-y[i]
#             if t_difx>0:
#                 if t_dify/t_difx!=slop:
                    
#                     return False
#         return True
            

        
