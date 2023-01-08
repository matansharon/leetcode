class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr1=[]
        arr2=[]
        for i in nums:
            if i%2==0:
                arr1.append(i)
            else:
                arr2.append(i)
        return arr1+arr2
