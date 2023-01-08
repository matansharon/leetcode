class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in nums1:
            start=nums2.index(i)
            
            
            for j in nums2[start+1:]:
                
                if j>i:
                    res.append(j)
                    break
                if j==nums2[-1]:
                    res.append(-1)
            if len(nums2[start+1:])==0:
                res.append(-1)
            
        return res
