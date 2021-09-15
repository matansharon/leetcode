# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

# Example 1:


# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
# Example 2:

# Input: grid = [[1]]
# Output: 4
# Example 3:

# Input: grid = [[1,0]]
# Output: 4




class Solution(object):
# '----------------------------------------------------------'
    def check_north(self,row,col,grid):
        
        if row==0 and grid[row][col]==1:
            return True
        elif grid[row-1][col]==0:
            return True
        else:
            return False
# '----------------------------------------------------------'
    def check_west(self,row,col,grid): 
        if col==len(grid[0])-1 and grid[row][col]==1:
            return True
        elif grid[row][col+1]==0:
            return True
        else:
            return False
# '----------------------------------------------------------'
    
    def check_east(self,row,col,grid):
        
        if col==0 and grid[row][col]==1:
            return True
        elif grid[row][col-1]==0:
            return True
        else:
            return False
    
# '----------------------------------------------------------'
    def check_south(self,row,col,grid):
        if row==len(grid)-1 and grid[row][col]==1:
            return True
        elif grid[row-1][col]==0:
            return True
        else:
            return False

# '----------------------------------------------------------'
    def check_all_borders(self,row,col,grid):
        res=0
        if self.check_north(row,col,grid):
            res+=1
        if self.check_south(row,col,grid):
            res+=1
        if self.check_east(row,col,grid):
            res+=1
        if self.check_west(row,col,grid):
            res+=1
        return res
# '----------------------------------------------------------'

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res=0
        for row in range(len(grid)):
            
            for col in range(len(grid[row])):
                
                if grid[row][col]==1:
                    res+=self.check_all_borders(row,col,grid)
        return res
