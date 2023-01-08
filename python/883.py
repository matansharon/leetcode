class Solution(object):
    def get_coloumn(self,pos,mat):
        arr=[]
        for row in mat:
            arr.append(row[pos])
        return arr
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        top=0
        side=0
        front=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!=0:
                    top+=1
        for i in grid:
            side+=max(i)
        
        for i in range(len(grid[0])):
            front+=max(self.get_coloumn(i,grid))
        return top+side+front
