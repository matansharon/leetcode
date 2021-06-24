class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        temp=sorted(heights)
        res=0
        for i in range(0,len(temp)):
            if heights[i]!=temp[i]:
                res+=1
        return res
        
