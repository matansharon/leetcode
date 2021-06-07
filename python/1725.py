class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        arr=[]
        for i in rectangles:
            t=min(i)
            arr.append(t)
        m=max(arr)
        res=arr.count(m)
        return res
        
