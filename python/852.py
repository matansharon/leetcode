class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res=-1
        for i in range(1,len(arr)-1):
            if arr[i-1]<arr[i]>arr[i+1]:
                return i
