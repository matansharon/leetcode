class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxcandie=-1
        res=[]
        for i in candies:
            if i>maxcandie:
                maxcandie=i
        for i in candies:
            if i+extraCandies>=maxcandie:
                res.append(True)
            else:
                res.append(False)
        return res
