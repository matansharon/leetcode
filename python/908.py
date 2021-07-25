class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        _min=min(nums)
        _max=max(nums)
        if _min+k>=_max-k:
            return 0
        if _min+k<=_max-k:
            return (_max-k)-(_min+k)
