class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in arr1:
            if i in arr2 and i in arr3:
                res.append(i)
        return res
        
