class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1=set()
        set2=set()
        for i in nums1:
            set1.add(i)
        for i in nums2:
            set2.add(i)
        return set1.intersection(set2)
