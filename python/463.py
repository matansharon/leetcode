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
