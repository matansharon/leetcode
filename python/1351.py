class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res=0
        for i in grid:
            for j in i:
                if j<0:
                    res+=1
        return res
        
