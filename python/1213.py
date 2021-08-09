# Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

 

# Example 1:

# Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
# Output: [1,5]
# Explanation: Only 1 and 5 appeared in the three arrays.
# Example 2:

# Input: arr1 = [197,418,523,876,1356], arr2 = [501,880,1593,1710,1870], arr3 = [521,682,1337,1395,1764]
# Output: []


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
        
